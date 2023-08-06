pyworldzipcode
=============

|PyPI version| |License| |Python Versions| |Build Status| |Requirements Status|

:Author: Dalwinder singh

.. contents::
    :backlinks: none

.. sectnum::

What is it?
-----------

Extract meta data like

-  ``postal_code``
-  ``coutry_code``
-  ``state_code``
-  ``state_name``
-  ``admin_name2``
-  ``admin_name3``
-  ``place_name``



-  Appropriate boundaries for that area

by just using the ``postal_code`` and `Country code <https://github.com/dalwindr/inferzipcode/tree/main/worldpostalcode/country_files/*.py>`__

Features
--------

-  Written in uncomplicated ``python``
-  Supports all the Country codes specified in the ISO specification i.e
   all **264 countries** where they have a pin code.

   You can find a list of all the country codes at `the Wiki page <https://github.com/dalwindr/inferzipcode/tree/main/worldpostalcode/country_files/*.py>`__
-  Gives ouput in a ``dict`` form or a ``JSON`` format
-  Fast and easy to use


Installation
------------

Option 1: installing through `pip <https://pypi.python.org/pypi/worldpostalcode>`__ (Suggested way)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.python.org/pypi/worldpostal>`__

``$ pip install pyworldzipcode``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install pyworldzipcode``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/dalwindr/inferzipcode.git
    $ cd worldpostal/
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----

``bulkget()``
~~~~~~~~~

from pyworldzipcode.pyinferzipcode import WorldPostalSearch

import pandas as pd
import sys


class MyEng:
    def infer_missing_fields_pypostal_search_engine(
            self, address1, address2, city, state_or_province, _postal_code, _country_code
    ):
        if all([_postal_code and _country_code]):
            se = WorldPostalSearch()
            valid_countries = se.valid_countries()
        else:
            return address1, address2, city, state_or_province, _postal_code, _country_code
        if all([_country_code in valid_countries, _postal_code]) and not all([city, state_or_province]):
            out_val = se.bulkget([(_postal_code, _country_code)])
            if bool(out_val[0]):
                state_code = list(set(i["state_code"] for i in out_val))
                admin_name2 = list(set([i["admin_name2"] for i in out_val]))
                admin_name3 = list(set(i["admin_name3"] for i in out_val))
                place_name = list(set(i["place_name"] for i in out_val))
                _ = admin_name2.remove("nan") if "nan" in admin_name2 else None
                _ = admin_name3.remove("nan") if "nan" in admin_name3 else None
                _ = place_name.remove("nan") if "nan" in place_name else None
            else:
                return address1, address2, city, state_or_province, _postal_code, _country_code

            state_or_province = state_code[0] if len(state_code) > 0  else None
            admin_name2 = admin_name2[0] if len(admin_name2) > 0 else None
            admin_name3 = admin_name3[0] if len(admin_name3) > 0 else None
            place_name = place_name[0] if len(place_name) > 0 else None
            city = admin_name3 if bool(admin_name3) and not bool(city) else None
            city = admin_name2 if bool(admin_name2) and not bool(city) else city
            city = place_name if bool(place_name) and not bool(city) else city

            ret = address1, address2, city, state_or_province, _postal_code, _country_code
        else:
            ret = address1, address2, city, state_or_province, _postal_code, _country_code
        return ret


address1, address2, city, state_or_province, postal_code, country_code = "house no 10", None, None, None, "110018", "IN"
val = MyEng().infer_missing_fields_pypostal_search_engine(address1, address2, city, state_or_province, postal_code, country_code)
print(val)

address1, address2, city, state_or_province, postal_code, country_code = "house no 10", None, None, None, "10006", "US"
val = MyEng().infer_missing_fields_pypostal_search_engine(address1, address2, city, state_or_province, postal_code, country_code)
print(val)

address1, address2, city, state_or_province, postal_code, country_code = "house no 10", None, None, None, "560004", "IN"
val = MyEng().infer_missing_fields_pypostal_search_engine(address1, address2, city, state_or_province, postal_code, country_code)
print(val)

address1, address2, city, state_or_province, postal_code, country_code = "house no 10", None, None, None, "L0P", "CA"
val = MyEng().infer_missing_fields_pypostal_search_engine(address1, address2, city, state_or_province, postal_code, country_code)
print(val)

address1, address2, city, state_or_province, postal_code, country_code = "house no 10", None, None, None, "3000", "CH"
val = MyEng().infer_missing_fields_pypostal_search_engine(address1, address2, city, state_or_province, postal_code, country_code)
print(val)

