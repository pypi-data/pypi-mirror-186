import types
import os
from html import escape
from distutils.version import LooseVersion


# http://192.168.0.8:18003/unit_test
def all_test():
    result_txt = ""
    print(os.getpid(), '[jennifer]', 'info', 'all_test')

    result_txt += check_intercept()
    return result_txt


def check_intercept():
    import sys

    result = ""

    must_be = [
        ('jennifer.hooks.app_flask', check_flask),
        ('jennifer.hooks.external_requests', check_requests),
        ('jennifer.hooks.external_urllib', check_urllib),
        ('jennifer.hooks.external_urllib3', check_urllib3),
        # ('jennifer.api.proxy', None),
        ('jennifer.hooks.db_pymongo', check_pymongo),
        ('jennifer.hooks.db_redis', check_redis),
        ('jennifer.hooks', check_builtins),
    ]

    for module in must_be:
        if module[0] not in sys.modules.keys():
            result += "EXCEPTION: NO JENNIFER MODULE: " + module[0] + "<br />\n"
        else:
            target_module = __import__(module[0])
            result += "info: " + module[0] + " imported: " + target_module.__package__ + "<br />\n"

            func = module[1]
            if func is not None:
                result += module[1](target_module)

    result += test_info()

    for key in sys.modules.keys():
        # result += "info: " + key + ", " + "<br />\n"
        pass

    return result


def test_info():
    text = ""

    try:
        text = "info: " + str(os.getpid()) + ' ' + os.environ['DIR_ROOT'] + "<br />\n"
    except Exception as e:
        text = "info: " + str(os.getpid()) + " local_test<br />\n"

    return text


def check_builtins(module):
    import socket

    check_funcs = [
        (__builtins__['open'], "_wrap_file_open.<locals>._handler"),
        (socket.socket.connect, "_wrap_socket_connect.<locals>._handler"),
        (socket.socket.connect_ex, "_wrap_socket_connect.<locals>._handler"),
    ]

    return check_funcs_all(check_funcs)


def check_urllib(module):
    import urllib

    check_funcs = [
        (urllib.request.urlopen, "wrap_urlopen.<locals>.handler"),
    ]

    return check_funcs_all(check_funcs)


def check_urllib3(module):
    import urllib3

    check_funcs = [
        (urllib3.poolmanager.PoolManager.request, "wrap_request.<locals>.handler"),
        (urllib3.poolmanager.PoolManager.urlopen, "wrap_request.<locals>.handler"),
    ]

    return check_funcs_all(check_funcs)


def check_requests(module):
    import requests

    check_funcs = [
        (requests.Session.send, "wrap_send.<locals>.handler"),
    ]

    return check_funcs_all(check_funcs)


def check_flask(module):
    import flask

    check_funcs = [
        (flask.Flask.wsgi_app, "_wrap_wsgi_handler.<locals>.handler"),
        (flask.Flask.dispatch_request, "wrap_dispatch_request.<locals>.handler"),
    ]

    return check_funcs_all(check_funcs)


def check_pymongo(module):
    import pymongo

    current_ver = LooseVersion(pymongo.__version__)
    base_ver = LooseVersion("3.12.3")
    check_funcs = None

    if current_ver <= base_ver:
        check_funcs = [
            (pymongo.MongoClient, "hook.<locals>.MongoClientWrap3"),
        ]
    else:
        check_funcs = [
            (pymongo.MongoClient, "hook.<locals>.MongoClientWrap4"),
        ]

    return check_funcs_all(check_funcs)


def check_redis(module):
    import redis

    check_funcs = [
        (redis.Redis.execute_command, "wrap_execute_command.<locals>.handler"),
    ]

    return check_funcs_all(check_funcs)


def func_name_check(func, func_name):
    import dis
    if func.__qualname__ == func_name:
        return "info: Intercepted: " + escape(func_name, "<")

    return "exception: NOT INTERCEPTED: " + escape(func_name, "<") + ", " + escape(func.__qualname__, "<")


def check_funcs_all(check_funcs):

    result = ""
    for func_item in check_funcs:
        result += func_name_check(func_item[0], func_item[1]) + "<br />\n"

    return result
