===============
Getting Started
===============

This tools is something I created for myself for quickly searching for some unicode characters without having to open my browser everytime.

.. _getting_started-installation:

Installation
------------
Anicode is available on `PyPi <https://pypi.org/>`_.
So you can easily install the anicode package with the following command:

.. code-block:: bash

   pip install --user anicode


This will install the Anicode package as well as give you access to the embeded command line utility!

.. note:: If you do not have access to the anicode command line utility after using the above command, make sure that the ``~/.local/bin/`` directory is included in your ``$PATH`` environment varaible.

.. important:: Anicode requires `Python 3.5+ <https://www.python.org/downloads/>`_!
   If you haven't yet started using Python 3, you should definitely start since **many** projects are fully dropping support for Python 2.7.


.. _getting_started-command-line:

Command Line
------------
Using Anicode from the command line is really simple.
After installing Anicode from pip, the ``anicode`` tool should be accessible from the shell.

.. image:: ./_static/usage.gif
    :align: center


You should be able to search for unicode characters using the following command:

.. code-block:: bash

    anicode search "query"


After searching, the tool will prompt you to select the character you want.

.. note:: This tool only searches for proper unicode character names.
    Fuzzy unicode character matches are not yet supported.
