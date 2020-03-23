from setuptools import setup

setup(
    name="showme",
    version='0.1',
    py_modules=['myemail'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        email=myemail:cli
    ''',
)