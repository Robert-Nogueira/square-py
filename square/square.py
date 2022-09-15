"""This module is an unofficial wrapper for using the SquareCloud API"""
from typing import Any
import requests
from requests.models import Response

from .logs import logger


_BASE_URL = 'https://api.squarecloud.app/v1/public'

def _raise_request_error(
    request: Response, 
    extra: dict[Any, Any] | None=None
) -> None:
    try:
        request.raise_for_status()
    except requests.HTTPError as exc:
        data = request.json()
        msg = data['code']
        logger.error(msg=msg, extra=extra)
        raise exc

def _get_response(request: Response) -> dict[str, Any]:
    """takes the response of the resquest

    Parameters
    ----------
    request : Response
        a request object

    Returns
    -------
    dict[str, Any]
        a dictionary containing the request response
    """
    data = request.json()
    response = data['response']
    return response

def _request_get(
    path: str,
    api_key: str,
    extra: dict[Any, Any] | None=None,
    try_raise: bool=True
) -> Response:
    """make a get request to SquareCloudAPI and return the data

    Parameters
    ----------
    path : str
        the path to be used with the base url
    api_key : str
        the api key to acess the api

    Returns
    -------
    Any
        return the request response
    """
    headers = {'Authorization': api_key}
    request = requests.get(url=f'{_BASE_URL}/{path}', headers=headers, timeout=60)
    if try_raise:
        _raise_request_error(request=request, extra=extra)
    return request

def _request_post(
    path: str, 
    api_key: str, 
    extra: dict[Any, Any] | None=None, 
    try_raise: bool=True
) -> Response:
    """make a post request to SquareCloudAPI and return the data

    Parameters
    ----------
    path : str
        the path to be used with the base url
    api_key : str
        the api key to acess the api

    Returns
    -------
    Any
        return the request response
    """
    headers = {'Authorization': api_key}
    request = requests.post(url=f'{_BASE_URL}/{path}', headers=headers, timeout=60)
    if try_raise:
        _raise_request_error(request=request, extra=extra)
    return request


class SquareApp:
    """represents a square application"""
    def __init__(self, api_key: str, app_id: int) -> None:
        self.api_key = api_key
        self.app_id = app_id

    def info_dict(self) -> dict[str, Any]:
        """a method to get your app status

        Parameters
        ----------
        app_id : int
            the application id

        Returns
        -------
        Any
            a dictionary with your app status
        """
        path = f'status/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra)
        info = request.json()
        return info

    def logs(self) -> str | None:
        """get a resume of your application logs

        Parameters
        ----------
        app_id : int
            your application id

        Returns
        -------
        str
            a string with your logs
        """
        path = f'logs/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra, try_raise=False)
        if request:
            response = _get_response(request=request)
            logs = response['logs']
            return logs

    def logs_complete(self) -> str | None:
        """get a url with the full logs

        Returns
        -------
        str
            a string with the logs url
        """
        path = f'logs-complete/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra, try_raise=False)
        if request:
            response = _get_response(request=request)
            logs = response['logs']
            return logs

    def is_running(self) -> bool:
        """check if the applications is running

        Returns
        -------
        bool
            a boolean
        """
        path = f'status/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra)
        response = _get_response(request=request)
        running = response['running']
        return running

    def backup(self) -> str:
        """made a backup

        Returns
        -------
        str
            the beckup url
        """
        path = f'backup/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra)
        data = _get_response(request=request)
        url = data['downloadURL']
        msg = f'a new backup has been made: \033[4;33m{url}\033[m'
        logger.info(msg=msg, extra=extra)
        return url

    def start(self) -> bool:
        """start the application

        Returns
        -------
        bool
            return a boolean
        """
        path = f'start/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_post(path=path, api_key=self.api_key, extra=extra)
        data = request.json()
        msg = f'STARTED {data["message"]}'
        logger.info(msg=msg, extra=extra)
        return bool(request)

    def stop(self) -> bool:
        """stop the application

        Returns
        -------
        bool
            return a boolean
        """
        path = f'stop/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_post(path=path, api_key=self.api_key, extra=extra)
        data = request.json()
        msg = f'STOPPED {data["message"]}'
        logger.info(msg=msg, extra=extra)
        return bool(request)
    
    def restart(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        path = f'start/{self.app_id}'
        extra = {'id': self.app_id}
        request = _request_post(path=path, api_key=self.api_key, extra=extra)
        data = request.json()
        msg = f'RESTARTED {data["message"]}'
        logger.info(msg=msg, extra=extra)
        return bool(request)


class Api:
    """the square api"""
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_app(self, app_id: int) -> SquareApp:
        """get an application object

        Parameters
        ----------
        app_id : int
            the application id

        Returns
        -------
        SquareApp
            returns an application object
        """
        return SquareApp(self.api_key, app_id)

    def user_info(self, user_id: int | None=None) -> dict[str, Any]:
        """show informations about a user

        Parameters
        ----------
        user_id : int
            the user id

        Returns
        -------
        dict[str, Any]
            a dictionary containing the informations
        """
        path = f'user'
        extra = {'id': user_id}
        request = _request_get(path=path, api_key=self.api_key, extra=extra)
        response = _get_response(request=request)
        return response
