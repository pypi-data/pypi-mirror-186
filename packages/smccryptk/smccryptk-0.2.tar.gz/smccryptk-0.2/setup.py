from setuptools import setup, find_packages


setup(
    name='smccryptk',
    version='0.2',
    license='MIT',
    author="tsy",
    author_email='torkus88@hotmail.com',
    packages=find_packages(),
    package_dir={'src': 'src'},
    url='http://www.example.com',
    keywords='smc, secure, server, cryptography, crypt, Secure multiparty computation',
    install_requires=['pycrypto', 'rsa'],

)
