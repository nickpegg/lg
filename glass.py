#!/usr/bin/env python

import datetime
import re

import sh
from flask import Flask, render_template, request

app = Flask("lg")
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/go', methods=['POST'])
def go():
    result = None
    output = ''

    match = re.match("([\w\.\:\-\_]+)", request.form['target'])
    if match:
        target = match.group(1)
        method = request.form['method']

        log(request, method, target)

        if method == 'ping':
            result = ping(target)
        elif method == 'mtr':
            result = mtr(target)
        else:
            output = "You gave me an invalid method!"

        if result is not None:
            output = result.stderr + result.stdout
    else:
        output = "Your target doesn't look like an IP address or a hostname."

    return render_template('index.html', results=output)


def ping(dest, count=10):
    return sh.ping(dest, c=count, _ok_code=[0, 1, 2])


def mtr(dest, count=10):
    return sh.mtr(dest, r=True, w=True, c=count, _ok_code=[0, 1])


def log(request, method, target):
    print("[{0}] {1} {2} {3}".format(str(datetime.datetime.now()),
                                     request.remote_addr, method, target))


if __name__ == '__main__':
    app.run()
