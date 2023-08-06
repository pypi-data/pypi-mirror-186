import requests
from retrying import retry

from earth_brain_engine.config import cfg


@retry(stop_max_attempt_number=cfg.StopMaxAttemptNumber)
def request_url(url, method="POST", headers=None, params=None, timeout=cfg.RequestTimeout):
    """
    NOTE: request others url and retry
    :param url: url
    :param method: method
    :param headers: headers
    :param params: params
    :param timeout: 超时时间
    """
    try:
        if method in ["POST", "PUT"]:
            response = requests.post(url, headers=headers, json=params, timeout=timeout)
        else:
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        return response.json()
    except ConnectionError as con:
        return ConnectionError(f'Request: {url} Error: {con}')
    except Exception as error:
        raise error from Exception


@retry(stop_max_attempt_number=cfg.StopMaxAttemptNumber)
def request_url_auth(url, method="GET", params=None, timeout=cfg.RequestTimeout):
    """
    NOTE: request others url and retry
    :param url: url
    :param method: method
    :param headers: headers
    :param params: params
    :param timeout: 超时时间
    """
    if not cfg.UserAuthToken:
        raise RuntimeError("User Auth Token is None,Please Set 'cfg.UserAuthToken'")
    headers = {"Authorization": cfg.UserAuthToken}
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, json=params, timeout=timeout)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=params, timeout=timeout)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=timeout)
        elif method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        else:
            raise RuntimeError(f"Not Support Method: {method}")
        return response.json()
    except ConnectionError as con:
        return ConnectionError(f'Request: {url} Error: {con}')
    except Exception as error:
        raise error from Exception


def response_handler(response):
    """
    处理任务的返回函数
    """
    try:
        if isinstance(response, dict):
            if response.get("status"):
                return response.get("message")
            elif response['return_code'] in (1, 401):
                return response["return_message"]
            else:
                if response.get("beans"):
                    return response["beans"]
                else:
                    return response["return_message"]
        else:
            return response
    except Exception as e:
        raise e


def directory_handler(response):
    """
    处理算子目录服务的返回值
    """
    try:
        if isinstance(response, dict):
            if response['code'] != 200:
                return response['msg']
            else:
                return response['data']
        else:
            return response
    except Exception as e:
        raise e
