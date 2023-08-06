# -* -coding: UTF-8 -* -
"""Request server, get response and return the response"""
import traceback
from functools import wraps

import requests

from earth_brain_engine.config import cfg
from earth_brain_engine.constant import OperatorTaskUrlMap, OperatorDirectoryUrlMap
from earth_brain_engine.tool import request_url, request_url_auth, response_handler, directory_handler


def reset(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        for k, v in OperatorTaskUrlMap.items():
            cfg.OperatorTaskServerURL[k] = f'{cfg.OperatorTaskServer}/{v}'
        for k, v in OperatorDirectoryUrlMap.items():
            cfg.OperatorDirectoryURL[k] = f'{cfg.OperatorDirectoryServer}/{v}'
        return func(*args, **kwargs)

    return wrapper


class BaseOperatorEngine:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f'operator name: {self.name}, version: {self.version}'

    @reset
    def _get_operator(self):
        try:
            server_data = request_url(
                url=cfg.OperatorDirectoryURL.query,
                params={"name": self.name, "version": self.version},
                method="GET"
            )
            return directory_handler(server_data)
        except Exception as e:
            raise e


class Model(BaseOperatorEngine):
    """模型"""

    @reset
    def predict(self, *args, **kwargs):
        """
        预测
        :return: 预测结果
        """
        try:
            config = self._get_operator()
            if isinstance(config, list) and config:
                config = config[0]['data']
                print(f'服务算子的信息如下: {config} ---- 开始预测... ...')
                headers = {'retoken': config['token']}
                if kwargs.get("headers"):
                    headers.update(kwargs["headers"])
                return requests.post(config['url'], *args, **kwargs, headers=headers)
            else:
                return config
        except Exception as e:
            raise e


class Task(BaseOperatorEngine):

    @reset
    def create(self, **kwargs):
        """任务类算子"""
        try:
            kwargs.update({'name': self.name, 'version': self.version})
            print(f'--->> 创建任务的请求参数: {kwargs}')
            if not cfg.OperatorTaskServerURL:
                raise RuntimeError('路由映射出现了错误... ...')
            _data = request_url_auth(url=cfg.OperatorTaskServerURL.task, params=kwargs, method="POST")
            print(_data)
            return response_handler(response=_data)
        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    @reset
    def status(sql_id):
        try:
            res = request_url_auth(url=cfg.OperatorTaskServerURL.status, params={'sql_id': sql_id})
            print(res)
            return response_handler(response=res)
        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    @reset
    def abort(sql_id):
        try:
            res = request_url_auth(url=cfg.OperatorTaskServerURL.task, params={'sql_id': sql_id}, method="PUT")
            print(res)
            return response_handler(response=res)
        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    @reset
    def delete(sql_id):
        try:
            res = request_url_auth(url=cfg.OperatorTaskServerURL.task, params={'sql_id': sql_id}, method="DELETE")
            print(res)
            return response_handler(res)
        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    @reset
    def log(sql_id):
        print(sql_id)
        try:
            res = request_url_auth(url=cfg.OperatorTaskServerURL.log, params={'sql_id': sql_id})
            return response_handler(res)
        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    @reset
    def event(sql_id):
        try:
            res = request_url_auth(url=cfg.OperatorTaskServerURL.event, params={'sql_id': sql_id})
            print(res)
            return response_handler(res)
        except Exception as e:
            print(e)
            traceback.print_exc()
