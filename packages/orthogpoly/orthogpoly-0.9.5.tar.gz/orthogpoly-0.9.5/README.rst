##########
orthogpoly
##########

|build| |pyversions| |pypi| |license|

The Python package for orthogonal polynomials.

This package is simply a re-purposed mirror of one of the last open-sourced versions of the `orthopy <https://pypi.org/project/orthopy/>`_ Python package, `orthopy version 0.9.5 <https://zenodo.org/record/5751934>`_ (under the GNU GPLv3 license) in late December 2021/early January 2022. The only difference between ``orthogpoly`` and `orthopy version 0.9.5 <https://zenodo.org/record/5751934>`_ is that ``orthogpoly`` has no plotting clients -- plotting clients have been completely disabled. I do not intend to alter the contents of ``orthogpoly`` whatsoever going forward.

************
Installation
************

This package can be installed using ``pip`` via the `Python Package Index <https://pypi.org/project/orthogpoly/>`_ (PyPI),

::

    pip install orthogpoly

Alternatively, a branch can be directly installed using

::

    pip install git+https://github.com/jasonmulderrig/orthogpoly.git@<branch-name>

or after cloning a branch, moving to the main project directory (where the setup and configuration files are located), and executing ``pip install -e .`` for an editable installation or ``pip install .`` for a standard installation.

***********
Information
***********

- `License <https://github.com/jasonmulderrig/orthogpoly/LICENSE>`__
- `Releases <https://github.com/jasonmulderrig/orthogpoly/releases>`__
- `Repository <https://github.com/jasonmulderrig/orthogpoly>`__

..
    Badges ========================================================================

.. |build| image:: https://img.shields.io/github/checks-status/jasonmulderrig/orthogpoly/main?label=GitHub&logo=github
    :target: https://github.com/jasonmulderrig/orthogpoly

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/orthogpoly.svg?logo=python&logoColor=FBE072&color=4B8BBE&label=Python
    :target: https://pypi.org/project/orthogpoly/

.. |pypi| image:: https://img.shields.io/pypi/v/orthogpoly?logo=pypi&logoColor=FBE072&label=PyPI&color=4B8BBE
    :target: https://pypi.org/project/orthogpoly/

.. |license| image:: https://img.shields.io/github/license/jasonmulderrig/orthogpoly?label=License
    :target: https://github.com/jasonmulderrig/orthogpoly/LICENSE