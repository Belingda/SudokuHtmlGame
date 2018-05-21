# coding=utf-8
from flask import Flask, request
from flask import render_template
import json
import time

from Log import WriteToRecordFile
from RealNum import GetSuduInit

app = Flask(__name__)


@app.route('/')
def getIndexHtml():
    return render_template('index.html')


@app.route('/getSuduRect')
def getSuduRect():
    return GetSuduInit()


@app.route('/recordJoin')
def recordJoin():
    connectIp = request.remote_addr
    clickTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    WriteToRecordFile(connectIp, clickTime)
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
