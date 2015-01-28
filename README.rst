Python client for McAfee ePolicy Orchestrator
=============================================

A straightforward wrapper around the ePO API.
Manages authentication, building requests, and interpreting responses.
Simply treat the client object as a callable function, passing the command name and parameters.

Install::

    $ pip install mcafee-epo

Use::

    >>> from mcafee_epo import Client
    >>> client = Client('https://localhost:8443', 'user', 'password')
    >>> systems = client('system.find', '')

Differences from "official" client
----------------------------------

This library was created in response to the fairly poor client distributed by McAfee, which didn't support Python 3 and
was generally a mess.
(You can find a cleaned up version of their client with Python 3 support in the first few commits.)

The official library required copying files into the Python location to "install" it.
This library is an actual package installed using ``pip``.

The official client uses low level url libraries and numerous workarounds to make http requests.
This library uses the `requests <http://python-requests.org/>`_ library to greatly simplify the work the previous code
was doing.

The official client used a dynamic command discovery and dispatch mechanism to make api calls seem like a nested set of
objects.
This library forgoes that complexity (which wasn't understood by IDEs anyway) for a more straightforward approach that
just accepts command names when calling.

Links
-----

* `PyPI releases <https://pypi.python.org/pypi/mcafee-epo>`_
* `Source code <https://bitbucket.org/davidism/mcafee-epo>`_
