import shutil
import os
import importlib.util
import sys
from setuptools import setup

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.pih import PIH

#for facade
#prettytable
#colorama
#protobuf
#grpcio (six)
#pyperclip
#win32com -> pywin32 (!!!)

#MC
#pywhatkit

#for orion
#myssql

#for log
#telegram_send

#for dc2
#docs:
    #mailmerge (pip install docx-mailmerge)
    #xlsxwriter
    #xlrd
    #python-barcode
    #Pillow
#ad:
    #pyad
    #pywin32 (!!!)
    #wmi
#transliterate

#for data storage
#pysos
#lmdbm

#for printer (dc2)
#pysnmp

#for polibase
#cx_Oracle

if PIH.VERSION.local() <= PIH.VERSION.remote():
    raise Exception("PIH version is same as version from PyPi")

#########################################################################################################
"""
1. python pih_setup.py sdist --dist-dir pih_dist bdist_wheel --dist-dir pih_dist build --build-base pih_build
2. twine upload --repository pypi pih_dist/*
3. pip install pih -U
"""
folder = "//pih/facade/pih_dist"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

# This call to setup() does all the work
setup(
    name=PIH.NAME,
    version=f"{PIH.VERSION.local()}",
    description="PIH library",
    long_description_content_type="text/markdown",
    url="https://pacifichosp.com/",
    author="Nikita Karachentsev",
    author_email="it@pacifichosp.com",
    license="MIT",
    classifiers=[],
    packages=[PIH.NAME],
    include_package_data=True,
    install_requires=["prettytable", "colorama", "grpcio", "protobuf", "requests", "transliterate"]
)