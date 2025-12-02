#!/usr/bin/env python

import datetime
import re
import subprocess

from subprocess import CompletedProcess
from typing import Optional

from flask import Flask, render_template, request, Request

app = Flask("lg")
app.debug = True


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/", methods=["POST"])
def index_post() -> str:
    log(request)
    output = do(request.form.get("method", ""), request.form.get("target", ""))

    return render_template("index.html", results=output)


@app.route("/api")
def api() -> str:
    return render_template("api.html")


@app.route("/ping/<target>")
@app.route("/api/ping/<target>")
def api_ping(target: str) -> str:
    log(request, method="ping", target=target)
    return do("ping", target)


@app.route("/mtr/<target>")
@app.route("/api/mtr/<target>")
def api_mtr(target: str) -> str:
    log(request, method="mtr", target=target)
    return do("mtr", target=target)


def do(method: str, target: str) -> str:
    output = ""
    result = None

    target = sanitize(target)
    if target:
        if method == "ping":
            result = ping(target)
        elif method == "mtr":
            result = mtr(target)
        else:
            output = "You gave me an invalid method!"

        if result is not None:
            if result.stderr is not None:
                output += result.stderr.decode()
            if result.stdout is not None:
                output += result.stdout.decode()
    else:
        output = "Your target doesn't look like an IP address or a hostname."

    return output


def ping(dest: str, count: int = 5) -> CompletedProcess[bytes]:
    return subprocess.run(["ping", dest, "-c", str(count)], capture_output=True)


def mtr(dest: str, count: int = 5) -> CompletedProcess[bytes]:
    return subprocess.run(
        ["mtr", dest, "-r", "-w", "-c", str(count)], capture_output=True
    )


def sanitize(dirty_target: str) -> str:
    match = re.match(r"([\w\.\:\-\_]+)", dirty_target)
    if match:
        target = match.group(1)
    else:
        target = ""

    return target


def log(
    request: Request, method: Optional[str] = None, target: Optional[str] = None
) -> None:
    if not method:
        method = request.form.get("method")

    if not target:
        target = request.form.get("target")

    client_addr = request.headers.get("X-Forwarded-For", request.remote_addr)

    print(
        "[{0}] {1} - {2} - {3}".format(
            str(datetime.datetime.now()), client_addr, method, target
        )
    )


if __name__ == "__main__":
    app.run()
