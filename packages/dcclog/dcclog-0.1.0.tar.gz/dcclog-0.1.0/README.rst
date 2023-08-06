dcclog
======

``dcclog`` is a simple wrapper around the python logging module that makes it easy to colorize and encrypt log messages.

Installation
============

From pypi:
~~~~~~~~~~

.. code-block:: console

    $ pip install dcclog

with built-in ciphers:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ pip install 'dcclog[cipher]'

From github:
~~~~~~~~~~~~

.. code-block:: console

    $ git clone https://github.com/jamazi/dcclog.git
    $ cd dcclog
    $ pip install '.[all]'

How To use dcclog
==================

.. code-block:: python

    import dcclog
    from dcclog.cipher.aes import AESEncryption

    # log all levels to encrypted file
    encrypted_fmt = dcclog.Formatter(cipher=AESEncryption("long_complex_password"))
    encrypted = dcclog.FileHandler(".logs/data.log")
    encrypted.setFormatter(encrypted_fmt)

    # log only to info level to plain file
    plain = dcclog.FileHandler(
        ".logs/module.log", formatter=dcclog.Formatter(), level=dcclog.INFO
    )

    # log only warning level to console
    console = dcclog.ConsoleHandler(level=dcclog.WARNING)
    console.setFormatter(dcclog.Formatter(color=True))


    logger = dcclog.getLogger(level=dcclog.NOTSET, handlers=(encrypted, console))
    logger.critical("critical")
    logger.error("error")
    logger.warning("warning")
    logger.info("info")
    logger.debug("debug")

    some_module_logger = dcclog.getLogger(__name__, handlers=plain)
    some_module_logger.critical("critical")
    some_module_logger.error("error")
    some_module_logger.warning("warning")
    some_module_logger.info("info")
    some_module_logger.debug("debug")

    # test decrypting log file
    for log in dcclog.read(".logs/data.log", AESEncryption("long_complex_password")):
        print(log)


