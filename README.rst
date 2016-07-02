Ntvapi
======

N television program API


Install
-------

```
$ pip install ntv.api
```


Devserver
---------
```
$ ntv-ctl
```


Prodserver
----------

```
$ pip install gunicorn
$ gunicorn -w 4 ntv.cli.wsgi
```
