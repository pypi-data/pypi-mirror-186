ESA Planning Timeline Request (PTR) Python package
==================================================

Since the [Rosetta mission](https://www.esa.int/Science_Exploration/Space_Science/Rosetta),
ESA developed an XML-like syntax to create Planning Timeline Request (PTR) files.
These files allow the mission team member to design custom attitude spacecraft pointing.
It is readable by `AGM` and `MAPPS` softwares to detect spacecraft constrains violations,
power conception and surface coverage. It can also be used to compute custom spacecraft
attitude (quaterions and `ck`).
This format will be re-used for the [JUICE mission](https://sci.esa.int/web/juice),
and can already be tested on the [JUICE pointing tool](https://juicept.esac.esa.int).

This python package implements an object oriented approach to help the creation and parsing
of PTR files for the user, as well an interface to check JUICE PTR validity with AGM.

> **Disclaimer:** This package is an early release and does not support all PTR implementations.
> Please, open an issue to report any issue you may accounter.
> Currently this tool in **beta stage, do not use it in critical environments**.

A detailed documentation can be found [here](https://esa-ptr.readthedocs.io/).

Installation
------------

This package is available on [PyPI](https://pypi.org/project/esa-ptr/) and could be installed like this:

```bash
python -m pip install esa-ptr
```

Even if this tool does not have any external dependencies, we recommend to use it in an isolated virtual environment (`venv` or `conda`).


Development and testing
-----------------------

If you want contribute to the development and tests your changes before submitting a merge request,
you need to install [Poetry](https://python-poetry.org/docs/) and clone this repository:

```bash
git clone https://juigitlab.esac.esa.int/python/ptr.git python-esa-ptr ;
cd python-esa-ptr/
```

Install the package and its dependencies:
```
poetry install
```

Then, after your edits, you need to check that both linters are happy:
```bash
poetry run flake8
poetry run pylint ptr tests/
```

and all the tests passed:
```bash
poetry run pytest
```


Documentation
-------------
* Rosetta Flight Dynamics: `RO-ESC-IF-5501_i3r4_RSGS_FD_ICD-2.pdf`
