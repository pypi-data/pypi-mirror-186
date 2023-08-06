Settings
========

:mod:`parmesan` has a couple of settings altering its behaviour.

Checking Units
++++++++++++++

Getting the units right is fundamental when performing physics calculations.
:mod:`parmesan` uses :mod:`pint` to handle units.

The physical calculation functions in :mod:`parmesan` wrapped with
:any:`units.ensure` handle units transparently. This means that if you don't
specify the unit for an argument, a default unit is assumed:

.. code-block:: python

    from parmesan.units import units
    from parmesan.gas.conversion import potential_temperature

    potential_temperature(
        temperature=300, # assumed you mean 300 Kelvin
        pressure=990*units.hPa
    )
    # 300.8625712894093 kelvin

This however can lead to confusion and wrong results if a different unit is
used accidentally. :mod:`parmesan` has a **unit mode**, which when set to
``explicit`` raises an error if a value without unit is given as argument.
Explicit unit mode can be dis-/enabled globally with

.. code-block:: python

    import parmesan

    parmesan.units.mode.state = None # disable unit checking
    parmesan.units.mode.state = "explicit" # strict unit checking
    parmesan.units.mode.state = "implicit" # automatic unit conversion

Or it can be dis-/enabled only for a block of code:

.. code-block:: python

    import parmesan

    with parmesan.units.mode("implicit"):
        # ...
        # code here is executed with automatic unit conversion

    with parmesan.units.mode("explicit"):
        # ...
        # code here is executed with explicit unit checking

    with parmesan.units.mode(None):
        # ...
        # code here is executed without unit checking

.. warning::

   It is strongly recommended to enable **unit mode** ``"explicit"``. For
   convenience unit mode defaults to ``"implicit"``.


Bounds Checking
+++++++++++++++

Some functions have bounds on their input and output values. For example,
:any:`saturation_water_vapour_pressure_over_water_magnus` is only applicable
in a certain temperature range.

With the :any:`bounds.mode`, the behaviour for outliers in input and output
values can be specified:

.. code-block:: python

    import parmesan

    parmesan.bounds.mode.state = None      # disable bounds checking
    parmesan.bounds.mode.state = "strict"  # error for outliers
    parmesan.bounds.mode.state = "warning" # warning for outliers

Or it can be dis-/enabled only for a block of code:

.. code-block:: python

    import parmesan

    with parmesan.bounds.mode("warning"):
        # ...
        # code here shows warnings for outliers

    with parmesan.bounds.mode("strict"):
        # ...
        # code here raises an error for outliers

    with parmesan.bounds.mode(None):
        # ...
        # code here is executed without bounds checking

.. warning::

   It is strongly recommended to enable **bounds mode** ``"strict"``. For
   convenience bounds mode defaults to ``"warning"``.

