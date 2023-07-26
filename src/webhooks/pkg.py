# app.py

import os
from flask import Flask, request, send_file

app_pkg = Flask(__name__)

# Directory where you want to store uploaded packages
UPLOAD_DIRECTORY = "/mnt/pypi"

@app_pkg.route("/simple/<package_name>/")
def simple_index(package_name):
    # Replace this with your own logic to fetch package information from the repository
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{package_name}</title>
    </head>
    <body>
        <h1>{package_name}</h1>
    </body>
    </html>
    """

@app_pkg.route("/simple/<package_name>/<version>/")
def simple_detail(package_name, version):
    # Replace this with your own logic to fetch package information from the repository
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{package_name} {version}</title>
    </head>
    <body>
        <h1>{package_name} {version}</h1>
    </body>
    </html>
    """

@app_pkg.route("/simple/")
def simple():
    # Replace this with your own logic to list available packages from the repository
    return "List of available packages"

@app_pkg.route("/simple/upload/", methods=["POST"])
def upload_package():
    # Handle package upload and save it to the upload directory
    package = request.files.get("package")
    if package:
        package.save(os.path.join(UPLOAD_DIRECTORY, package.filename))
        return "Package uploaded successfully."
    return "Package upload failed.", 400

@app_pkg.route("/<path:filename>")
def download_package(filename):
    # Serve package files for download
    return send_file(os.path.join(UPLOAD_DIRECTORY, filename), as_attachment=True)
