#coding: utf-8
# +-------------------------------------------------------------------
# | 宝塔Linux面板 
# +-------------------------------------------------------------------
# | Copyright (c) 2015-2099 宝塔软件(http://bt.cn) All rights reserved.
# +-------------------------------------------------------------------
# | Author: 黄文良 <287962566@qq.com>
# +-------------------------------------------------------------------
from os import environ
from BTPanel import app,socketio,sys

if __name__ == '__main__':
    
    PORT = 8888
    HOST = '0.0.0.0'
    socketio.run(app,host=HOST,port=PORT)
