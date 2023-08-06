"""
    FTP 文件、文件列表、文件夹下载

    示例：
        downloader = FTPDownloader(**连接配置, save_path='')
        downloader.download_file()
        downloader.download_list()
        downloader.download_dir()
"""
import os
import queue
import threading
import traceback
from pathlib import Path
from loguru import logger
from typing import Callable
from gftp.conn import FTPConn
from concurrent.futures import ThreadPoolExecutor


class FTPDownloader:
    def __init__(
            self,
            host: str,
            user: str,
            passwd: str,
            save_path: str,
            port: int = 21,
            timeout: int = 30,
            encoding: str = 'gbk',
            threads: int = 1,
            retry: int = 3,
            keep_structure: bool = True,
    ):
        """
        FTP 文件下载器

        :param threads: 下载线程数，每个线程一个连接
        :param retry: 最大下载重试次数
        :param save_path: 本地保存文件夹
        :param keep_structure: 保留目录结构：在 save_path 基础上，后续目录结构与 ftp 一致（默认保留）
        """
        # ftp 连接配置
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._timeout = timeout
        self._encoding = encoding

        # ftp 下载配置
        self._retry = retry
        self._threads = threads
        self._save_path = save_path
        self._keep_structure = keep_structure
        Path(self._save_path).mkdir(parents=True, exist_ok=True)

        # ftp 下载前配置
        self._record = {}
        self._queue_conn = queue.Queue()
        self._download_pool = ThreadPoolExecutor(self._threads)
        self._callback_pool = ThreadPoolExecutor(self._threads)
        self._new_connection()

    def _new_connection(self, count: int = None) -> None:
        """
        创建执行数量的连接

        :return:
        """
        count = count or self._threads

        for _ in range(count):
            self._queue_conn.put(FTPConn(
                host=self._host, port=self._port, user=self._user, passwd=self._passwd,
                timeout=self._timeout, encoding=self._encoding
            ))

    def _get_connection(self) -> FTPConn:
        """
        获取连接

        :return:
        """
        return self._queue_conn.get()

    def _recycle_connection(self, conn: FTPConn) -> None:
        """
        回收连接，并重置位置

        :param conn:
        :return:
        """
        try:
            conn.connection.cwd('/')
            self._queue_conn.put(conn)
        except:
            self._new_connection(count=1)

    def download_file(self, ftp_path: str, callback: Callable = None) -> dict:
        """
        下载指定文件

        :param ftp_path: 待下载文件路径
        :param callback: 回调函数，返回结果，ftp 路径，结果路径
        :return: 下载是否成功的布尔值
        """
        # 构造目录
        callback = callback or self.callback
        file_name = str(Path(ftp_path).name)  # 文件名
        if self._keep_structure:
            file_download_path = str(Path(self._save_path).joinpath(ftp_path[1:]))  # 本地文件目录
            Path(file_download_path).parent.mkdir(parents=True, exist_ok=True)  # 创建本地保存目录
        else:
            file_download_path = str(Path(self._save_path).joinpath(file_name))  # 本地文件目录

        # 创建记录
        if ftp_path not in self._record:
            self._record[ftp_path] = {
                'success': False,
                'failed_times': 0,
                'file_download_path': file_download_path,
            }

        # 尝试下载
        try:
            self._downloader(ftp_path=ftp_path, file_download_path=file_download_path, file_name=file_name)
            self._callback_pool.submit(callback, args=(True, ftp_path, file_download_path))
            self._record[ftp_path]['success'] = True

        except Exception as e:
            if "No such file or directory" in e.args[0]:
                logger.error("ftp 不存在该文件：{}", ftp_path)
                return self._record

            traceback.print_exc()

            # 下载错误记录
            if self._record[ftp_path]['failed_times'] < self._retry:
                self._record[ftp_path]['failed_times'] += 1
                logger.warning(f'下载错误，即将重试：{ftp_path}')

                return self.download_file(ftp_path=ftp_path, callback=callback)
            else:
                logger.error(f'下载重试达到最大次数，已终止下载：{ftp_path}')
                self._callback_pool.submit(callback, args=(False, ftp_path, file_download_path))

        return self._record

    def download_list(self, ftp_path_list: list, callback: Callable = None) -> dict:
        """
        循环下载文件列表

        :param ftp_path_list: 待下载文件路径列表
        :param callback: 回调函数，返回结果，ftp 路径，结果路径
        :return:
        """
        for ftp_path in ftp_path_list:
            self._download_pool.submit(self.download_file, ftp_path, callback)

        self._pool_shutdown()

        return self._record

    def download_dir(self, dir_path: str, callback: Callable = None) -> dict:
        """
        根据文件夹进行下载

        注意：因为需要不停去迭代文件夹，所以需要占用一段时间的连接名额

        :param dir_path: 文件夹路径
        :param callback: 回调函数，返回结果，ftp 路径，结果路径
        :return:
        """
        if self._threads == 1:
            self._new_connection(count=1)
        conn = self._get_connection()

        try:
            for ftp_path in conn.connection.iter_dir(dir_path=dir_path, only_file=True):
                self._download_pool.submit(self.download_file, ftp_path, callback)
        finally:
            self._recycle_connection(conn)

        self._pool_shutdown()

        return self._record

    def _downloader(self, ftp_path: str, file_name: str, file_download_path: str) -> bool:
        """
        下载指定文件

        :param ftp_path: 待下载文件路径
        :param file_name: 文件名
        :param file_download_path: 本地文件路径含文件名
        :return:
        """
        conn = self._get_connection()

        try:
            file_remote_parent_path = str(Path(ftp_path).parent).replace('\\', '/')  # 远程文件父目录
            conn.connection.cwd(file_remote_parent_path)

            # 检测是否需要断点续传
            if os.path.exists(file_download_path):
                f = open(file_download_path, 'ab')
                logger.debug(f'本地文件存在将断点续传：{file_download_path}')
            else:
                f = open(file_download_path, 'wb')
                logger.debug(f'正在下载：{file_download_path}')

            # 下载文件
            try:
                file_download_size = os.path.getsize(file_download_path)
                conn.connection.retrbinary(cmd='RETR ' + file_name, callback=f.write, rest=file_download_size)
                logger.debug(f'下载完成：{ftp_path}')
                return True
            finally:
                f.close()
        finally:
            self._recycle_connection(conn=conn)

    def _pool_shutdown(self):
        """
        等待线程执行完毕

        :return:
        """
        self._download_pool.shutdown()
        self._callback_pool.shutdown()

    @staticmethod
    def callback(success: bool, ftp_path: str, file_download_path: str):
        """
        回调，这是单独的线程

        :param success: 是否成功
        :param ftp_path: ftp 文件路径
        :param file_download_path: 下载的本地路径
        :return:
        """
        if success:
            logger.debug(f'下载成功：{ftp_path}')
        else:
            logger.debug(f'下载失败：{ftp_path}')

    def __del__(self):
        self._pool_shutdown()
