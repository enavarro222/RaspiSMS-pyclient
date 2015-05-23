# RaspiSMS-pyclient: Python client for RaspiSMS API

Small client for [RaspiSMS](http://raspisms.raspbian-france.fr/) server. It simply propose a trivial interface to send SMS from a python script or from command line.

See: 
* http://raspisms.raspbian-france.fr/
* https://github.com/RaspbianFrance/RaspiSMS

Licence : GNU LGPL (see LICENCE.txt)

## Install

    $ pip install git+https://github.com/enavarro222/RaspiSMS-pyclient.git


## Python module usage

```python
from raspisms import RaspiSMS
rsms = RaspiSMS("http://URL_TO/RaspiSMS", email="ADMIN@EMAIL.DD", password="PASSWORD")
rsms.send("PHONENUMBER", "SMS text !")
```

## Command-line tool

A command line tool `raspisms-send` is provided, you can use it this way:

    $ raspisms-send -u http://URL_TO/RaspiSMS -e ADMIN@EMAIL.DD -p ADMIN_PASSWORD  PHONENUMBER "SMS text"

See also `-h` for some help.

## TODO

See #TODO in [raspisms.py](raspisms.py), don't hesitate to send a push request !
