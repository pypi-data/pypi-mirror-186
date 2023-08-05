from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='rummy_circl_otp',
    version='0.1',
    py_modules=['rummy_circl_otp'],
    install_requires=[
        'requests',

    ],

    long_description=long_description,
    long_description_content_type="text/markdown",
)
