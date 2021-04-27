# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:41:47 2021

@author: SHAMBHAVI
"""

import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print (geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_nmber= phonenumbers.parse(number, "RO")
print (carrier.name_for_number(service_nmber, "en"))
