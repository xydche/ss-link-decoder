# -*- coding: utf-8 -*-

import base64
import json
import sys


def base64decode(s):
    # transtab = str.maketrans('-_', '+/')
    # s = s.translate(transtab)
    if len(s) % 4 != 0:
        s = s + (4 - len(s) % 4)*'='
    return base64.urlsafe_b64decode(s.encode())


def decode_ss(ss):
    code_base64 = ss[5:ss.find('@')]
    method_pwd = base64decode(code_base64)
    method_b, pwd_b = method_pwd.split(b':', 1)
    server = ss[ss.find('@')+1:ss.rfind(':')]
    if ss.find('#') == -1:
        port = ss[ss.rfind(':')+1:]
    else:
        port = ss[ss.rfind(':')+1:ss.find('#')]
    ss_conf = {'server': server, 'server_port': int(port),
               'password': pwd_b.decode(), 'method': method_b.decode()}
    print(json.dumps(ss_conf, indent=4))

    pwd_base64 = base64.urlsafe_b64encode(pwd_b)

    ssr = [server, port, 'origin', method_b.decode(), 'plain',
           pwd_base64.decode()]
    ssrlink = ':'.join(ssr) + '/?obfsparam=&protoparam=&remarks='
    ssrlink_base64 = base64.urlsafe_b64encode(ssrlink.encode())
    ssrlink_output = 'ssr://' + ssrlink_base64.decode()
    print(ssrlink_output)


def decode_ssr(ssr):
    first_b = base64decode(ssr[6:])
    ssr_conf = {'server': '', 'server_port': ''}
    print(first_b.decode())


def main(s):
    is_ss = s.find('ss://')
    is_ssr = s.find('ssr://')
    if is_ss != -1:
        ss = s[is_ss:].strip()
        decode_ss(ss)
    elif is_ssr != -1:
        ssr = s[is_ssr:].strip()
        decode_ssr(ssr)
    else:
        print('链接格式不正确！')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('参数不正确！')
    else:
        main(sys.argv[1])
