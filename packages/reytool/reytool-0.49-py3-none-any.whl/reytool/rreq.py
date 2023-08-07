# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022/12/08 11:07:25
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's request methods
══════════════════════════════
"""


import faker
import requests
from requests import Response, JSONDecodeError

from .rbasic import check_parm, error


fake = faker.Faker("zh_CN")
code_fields = ["code", "errno", "success"],
success_codes = [200, 0, True]

def fake_headers() -> "dict":
    """
    Fake request headers.

    Returns
    -------
    dict
        Fake request headers.
    """

    headers = {}
    headers['user_agent'] = fake.android_platform_token()
    return headers

def check_response(
        response: "Response",
        code_fields: "list"=code_fields,
        success_codes: "list"=success_codes,
        throw_error: "bool"=True
    ) -> "tuple":
    """
    Check whether reponse is successful

    Parameters
    ----------
    response : Response object
        Object from requests package.
    code_fields : list(str,)
        Possible field names of Response code in Response data.
    success_codes : list(object,)
        Successful codes.
    throw_error : bool
        Whether throw error.

    Returns
    -------
    tuple(int, str)
        Response code and Response message
    """

    check_parm(response, Response)
    check_parm(throw_error, bool)
    check_parm(code_fields, list)
    check_parm(success_codes, list)

    reponse_code = response.status_code
    if reponse_code != 200:
        check_info = reponse_code, response.text
        return error(throw_error, check_info)
    else:
        try:
            response_data = response.json()
        except JSONDecodeError:
            return 200, "success"
        success_codes_str = [str(code) for code in success_codes if type(code) == int]
        success_codes.extend(success_codes_str)
        if type(response_data) == dict:
            for field in code_fields:
                if field in response_data:
                    code = response_data[field]
                    if code in success_codes:
                        break
                    else:
                        check_info = code, response_data
                        return error(throw_error, check_info)
    return 200, "success"

def request(
    url: "str",
    data: "dict"=None,
    json: "dict"=None,
    headers: "dict | str"=None,
    method: "str"=None,
    check: "bool"=True,
    code_fields: "list"=code_fields,
    success_codes: "list"=success_codes
    ) -> "Response":
    """
    Send HTTP request.

    Parameters
    ----------
    url : str
        Request URL.
    data : dict or None
        Request data. Parameter data and json conflict.
    json : dict or None
        request data in JSON format. Parameter data and json conflict.
    headers :  None or dict or str {'fake'}
        Request header.
        
        - None : No request header.
        - dict : Use dict as request header.
        - 'fake' : Use fake request header.

    method : None or str {'get', 'post'}
        Request method.

        - None : Auto judge.
            * When parameter data or json not has value, then request method is get.
            * When parameter data or json has value, then request method is post.
        - 'get' : Request method is get.
        - 'post' : Request method is post.

    check : bool
        Whether check response.
    code_fields : list(str,)
        Possible field names of Response code in Response data.
    success_codes : list(object,)
        Successful codes.

    Returns
    -------
    Response object
        Object from requests package.
    """

    check_parm(url, str)
    check_parm(data, dict, None)
    check_parm(json, dict, None)
    check_parm(headers, dict, "fake", None)
    check_parm(method, "get", "post", None)
    check_parm(check, bool)
    check_parm(code_fields, list)
    check_parm(success_codes, list)
    
    if method == None:
        if data == None and json == None:
            method = "get"
        else:
            method = "post"
    if headers == "fake":
        headers = fake_headers()
    if method == "get":
        response = requests.get(url, data=data, json=json, headers=headers)
    elif method == "post":
        response = requests.post(url, data=data, json=json, headers=headers)
    if check:
        check_response(response, code_fields, success_codes)
    return response