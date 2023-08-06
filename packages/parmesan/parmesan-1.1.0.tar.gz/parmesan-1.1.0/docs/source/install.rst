Installation
============

From our Workgroup Repository
+++++++++++++++++++++++++++++

If you are using our `Manjaro Workgroup Repository
<https://gitlab.com/tue-umphy/workgroup-software/repository>`_, chances are you
already have :mod:`parmesan` installed. It is available in the repository as
``python-parmesan`` package. Install it with your favourite software installer,
e.g. ``pacman``:

.. code-block:: sh

   sudo pacman -Syu python-parmesan


From PyPI
+++++++++

You can install the latest tagged version of :mod:`parmesan` from from `PyPI <https://pypi.org/project/parmesan/>`_:

.. hint::

    Depending on your setup it might be necessary to install the :mod:`pip` module
    first:

    .. code-block:: sh

        # Debian/Ubuntu
        sudo apt-get install python3-pip
        # Manjaro/Arch
        sudo pacman -Syu python-pip

    Or see `Installing PIP`_.

    It is also a good idea to update :mod:`pip`:

    .. code-block:: sh

        pip install -U pip

    .. _Installing PIP: https://pip.pypa.io/en/stable/installing/

.. hint::

    Try ``python3 -m pip install --user -U`` if just using ``pip`` fails with a
    ``command not found``-like error.

.. code-block:: sh

    # This will install the latest tagged version from PyPI.
    # This might not be the latest development version, however.
    pip install -U parmesan


Directly From GitLab
++++++++++++++++++++

You can install the latest development version of :mod:`parmesan` via :mod:`pip`

.. code-block:: sh

    # make sure to have pip installed, see above
    pip install -U git+https://gitlab.com/tue-umphy/software/parmesan

This will install :mod:`parmesan` directly from GitLab.


If that doesn't work
--------------------

Try cloning the repository and install it from there:

.. code-block:: sh

    # clone the repository
    git clone https://gitlab.com/tue-umphy/software/parmesan
    # go into the repository
    cd parmesan
    # install from the repository (mind the dot at the end!)
    pip install .


If that doesn't work either
---------------------------

If installing from the repository didn't work, you can try downloading the latest built package from `here
<https://gitlab.com/tue-umphy/software/parmesan/-/jobs/artifacts/master/browse/dist?job=dist>`_:
Download the ``.tar.gz`` file and then execute

.. code-block:: sh

    pip install /path/to/the/file/parmesan.tar.gz

If even that doesn't work and the error message is not obvious, you probably
either got something wrong or your system configured in a weird way. Might be
some weird virtual environment or
Anaconda setup or a super old Python version, etc...


