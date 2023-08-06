from setuptools import setup

from cookiedbserver.__init__ import __version__

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='cookiedb-server',
    description='Server for the CookieDB database',
    long_description=readme,
    long_description_content_type='text/markdown',
    version=__version__,
    packages=['cookiedbserver'],
    url='https://github.com/jaedsonpys/cookiedb-server',
    license='Apache 2.0',
    keywords=['server', 'database', 'cookiedb', 'socket'],
    install_requires=['cookiedb==6.0.0'],
    entry_points={
        'console_scripts': [
            'cookiedbserver = cookiedbserver.__main__:main'
        ]
    }
)
