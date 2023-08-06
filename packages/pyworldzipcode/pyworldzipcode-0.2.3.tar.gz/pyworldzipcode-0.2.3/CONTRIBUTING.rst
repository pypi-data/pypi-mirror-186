Contributing
============

1. Fork it.

2. Clone it 

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__ 

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/worldpostal.git
    (develop)$ cd worldpostal
    (develop)$ pip install -r requirements.txt  # Install requirements for 'pyworldzipcode' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/worldpostal.git
    (develop)$ cd worldpostal
    (develop)$ pip install -r requirements.txt  # Install requirements for 'pyzipcode-cli' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

5. Run tests

.. code:: bash

    (develop) $ ./tests.py -v

Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature 

6. Push to the branch (``$ git push origin my-new-awesome-feature``)

7. Create new Pull Request

Hack away! 

Tests
~~~~~

``inferzipcode`` uses ``unittesting`` for testing purposes.

Running the test cases

.. code:: bash

   $ ./tests.py -v
   test_get__pincode (__main__.TestModule) ... ok
   test_get__pincodelist (__main__.TestModule) ... ok
   test_bulkget_pincode (__main__.TestModule) ... ok
   test_get_invalid_pincode (__main__.TestModule) ... ok
ok
   ----------------------------------------------------------------------
   Ran 6 tests in 11.141s

   OK