from setuptools import find_packages, setup

setup(
    name='sigmaSMSApi',
    packages=find_packages(include=['sigmaSMSApi']),
    install_requires=('pydantic', 'requests'),
    version='0.1.0',
    description='Tool for integration with SigmaSMS API',
    author='Tabunchik (Erdman) Kristina',
    author_email='erdmakristina8@gmail.com',
    url='https://github.com/KristinaErdman/sigmaSMSApi',
    download_url='https://github.com/KristinaErdman/sigmaSMSApi/blob/main/dist/sigmaSMSApi-0.1.0-py3-none-any.whl',
    keywords=['sigmaSMS', 'SMS', 'FastApi', 'pydantic'],
    license='MIT',
)
