from config import *
import subprocess
import time
import base64


class InvalidASNorIP(Exception):
    pass


class NoGPGFingerprint(Exception):
    pass


def get_maintainer(asn_or_ip):
    data = subprocess.check_output(['whois', '-h', WHOIS_SERVER, asn_or_ip]).decode().strip()
    if data.endswith('% 404') or data.endswith('% This is the dn42 whois query service.'):
        raise InvalidASNorIP()
    mnt = [line.split('\n') for line in data.split('\n') if line.startswith('mnt-by:')][-1][0].strip().split(' ')[-1]
    asn = \
    [line.split('\n') for line in data.split('\n') if line.startswith('aut-num:') or line.startswith('origin:')][-1][
        0].strip().split(' ')[-1]
    return asn, mnt
