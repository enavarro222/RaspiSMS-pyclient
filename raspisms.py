#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" Small client for RaspiSMS

see: http://raspisms.raspbian-france.fr/
"""
from __future__ import print_function
import os
import sys
import requests


cwd = os.path.abspath(os.path.dirname(__file__))
__version__ = open(os.path.join(cwd, 'VERSION.txt')).read()

class RaspiSMSError(RuntimeError):
    pass


class RaspiSMS(object):
    """ Minimal client for RaspiSMS API (http://raspisms.raspbian-france.fr)
    """
    def __init__(self, host, email, password):
        #TODO check host ok
        #TODO add options for a HTTP auth system
        self._host = host
        self._email = email
        self._password = password

    def send(self, num, text, date=None):
        #TODO manage date
        if date is not None:
            raise NotImplementedError("Need to be done... do it (and share it) or ask kindly on github")
        url = "%s/smsAPI/send/" % (self._host)
        data = {}
        data['email'] = self._email
        data['password'] = self._password
        data['numbers'] = num
        data['text'] = text
        res = requests.post(url, data=data)
        #TODO: check on a bien 200
        returns = res.json()
        if returns["error"] == 0:
            # every think ok
            pass
        elif returns["error"] == 1:
            raise RaspiSMSError("Invalid auth (email/password)")
        elif returns["error"] == 2:
            raise RaspiSMSError("Imposible to create this SMS")
        elif returns["error"] == 3:
            raise RaspiSMSError("Some arguments are missing")
        else:
            raise RaspiSMSError("Unknow error")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Send a SMS with throw a RaspiSMS server.')
    parser.add_argument("NUM", help="Destinataire phone number")
    parser.add_argument("TEXT", help="SMS it self !")
    parser_raspisms = parser.add_argument_group('RaspiSMS arguments')
    parser_raspisms.add_argument("-H", "--host", dest="host", help="RaspiSMS url", required=True)
    parser_raspisms.add_argument("-e", "--email", dest="email", help="RaspiSMS admin email", required=True)
    parser_raspisms.add_argument("-p", "--password", dest="password", help="RaspiSMS admin password", required=True)

    #TODO add .raspisms config file
    #TODO add interactive read of data

    args = parser.parse_args()

    rsms = RaspiSMS(args.host, email=args.email, password=args.password)
    try:
        rsms.send(args.NUM, args.TEXT)
    except RaspiSMSError as err:
        print("Error: %s" % err, file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())


