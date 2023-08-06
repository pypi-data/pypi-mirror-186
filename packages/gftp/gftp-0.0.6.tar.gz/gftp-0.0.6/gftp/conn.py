"""
    GFTP：新增了一些 FTP 没有的方法
        show_dir：列表形式返回文件夹下的所有文件、文件夹
        show_file：列表形式返回当前文件夹下的所有文件
        show_folder：列表形式返回当前文件夹下的所有文件夹
        iter_dir：遍历指定路径下的文件、文件夹并输出（迭代器）

    FTPConn：连接创建、快速重连

    ftp = FTPConn()
    ftp.connection.xxx
"""
import os
import re
import socket
from loguru import logger
from ftplib import FTP, error_perm


# 重写 FTP
class GFTP(FTP):
    def __init__(self):
        super().__init__()

    def show_dir(self, *args) -> list:
        """
        获取指定路径下的文件夹和文件

        :param args:
        :return:
        """
        base_path = self.pwd()

        cmd = 'LIST'
        line_list = []
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            if arg:
                cmd = cmd + (' ' + arg)
        self.retrlines(cmd, line_list.append)

        out_list = []
        for line in line_list:
            result = re.findall(r'[a-z-]+ +\d+ +\w+ +\w+ +\d+ +\w+ +\d+ +[0-9:]+ +(.+)', line)[0]
            if result and result not in ['.', '..']:
                out_list.append(os.path.join(base_path, result.strip()).replace('\\', '/'))
        return out_list

    def show_file(self) -> list:
        """
        获取路径下的文件列表

        :return:
        """
        base_path = self.pwd()

        return [os.path.join(base_path, file).replace('\\', '/') for file in self.nlst()]

    def show_folder(self) -> list:
        """
        获取路径下的文件夹列表

        :return:
        """
        base_path = self.pwd()

        folders = list(set(self.show_dir()).difference(set(self.show_file())))

        return [os.path.join(base_path, folder).replace('\\', '/') for folder in folders]

    def iter_dir(self, dir_path: str, only_file: bool = False) -> str:
        """
        迭代指定路径

        :param dir_path: 迭代的路径
        :param only_file: 只返回文件
        :return:文件路径
        """
        dir_path = dir_path.replace('\\', '/')
        self.cwd(dir_path)
        dir_list = []

        # 遍历当前文件夹
        for i in self.show_dir():
            path = os.path.join(dir_path, i).replace('\\', '/')
            if '.' in os.path.splitext(path)[-1]:
                yield path
            else:
                dir_list.append(path)
                if only_file:
                    continue
                yield path

        # 深度遍历文件夹
        for d in dir_list:
            for d2 in self.iter_dir(dir_path=d, only_file=only_file):
                yield d2


class FTPConn:
    def __init__(self, host: str, user: str, passwd: str, port: int = 21, timeout: int = 30, encoding: str = 'gbk'):
        """
        FTP 连接器

        :param timeout: 超时时间
        :param encoding: 编码
        """
        self._timeout = timeout
        self._encoding = encoding

        self._ftp = GFTP()
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._closed = True

        self._new_connection()

    def _new_connection(self) -> GFTP:
        """
        创建新连接

        :return:
        """
        try:
            self._ftp.set_pasv(True)
            self._ftp.encoding = self._encoding
            self._ftp.timeout = self._timeout
            self._ftp.connect(host=self._host, port=self._port)
            self._ftp.login(user=self._user, passwd=self._passwd)
            logger.debug(self._ftp.getwelcome())

            self._closed = False

            return self._ftp
        except(socket.error, socket.gaierror):
            self._closed = True
            logger.error(f'无法连接到：{self._host}:{self._port}！')
        except error_perm:
            self._closed = True
            logger.error('连接错误，检查登录信息！')

    def reconnection(self) -> GFTP:
        """
        根据上次连接进行重连

        :return:
        """
        self.close()

        return self._new_connection()

    @property
    def connection(self) -> GFTP:
        """
        ftp 连接对象

        :return:
        """
        return self._ftp

    def close(self):
        """
        关闭 ftp 连接

        :return:
        """
        if self._closed:
            return

        try:
            self.connection.quit()
        except:
            pass
        finally:
            self._closed = True
            print(f'连接已关闭：{self._host}:{self._port}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()
