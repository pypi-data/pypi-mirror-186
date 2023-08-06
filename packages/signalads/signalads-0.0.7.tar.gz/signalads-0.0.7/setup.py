from setuptools import setup
import sys

requires = ['requests>=0.10.8']

if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name="signalads",
    py_modules=['signalads'],
    version="0.0.7",
    description="Signal Ads Python library",
    author="Iman Naseri",
    author_email="inaseri.20@gmail.com",
    keywords=["signalads", "sms", "signal"],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/signalads-co/signalads-python"
)
