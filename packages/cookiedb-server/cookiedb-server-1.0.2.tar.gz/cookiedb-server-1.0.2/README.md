# CookieDB Server

The **CookieDB Server** was created to provide remote access to the [CookieDB database](https://github.com/jaedsonpys/cookiedb) through a socket server, increasing security and maintaining your databases ***available when you need it***. To access this server, [use the CookieDB Client](https://github.com/jaedsonpys/cookiedb-client) for Python.

- [Project in PyPI](https://pypi.org/project/cookiedb-server)
- [Source code](https://github.com/jaedsonpys/cookiedb-server)

Install the `cookiedb-server` using the PIP Package Manager:

```
pip install cookiedb-server
```

Or manually download by cloning the repository and running the install:

```
git clone https://github.com/jaedsonpys/cookiedb-server.git
python3 setup.py install
```

## Configure the server

Configuration is simple, you just need to specify the password to access the server after running the `cookiedbserver` command on the command line. The input looks like this

```
[?] Set a password:
```

After setting your password, just run the `cookiedbserver` command again to run your server which can be accessed by [CookieDB Client for Python](https://github.com/jaedsonpys/cookiedb-client).

## License

```
Apache License Version 2.0
Copyright 2023 Jaedson Silva
```

This project uses the [Apache 2.0 License](https://github.com/jaedsonpys/cookiedb-server/blob/master/LICENSE). Please see the license file to more informations.