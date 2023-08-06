# README

IPython custom cell magic to test code snippets typed into notebook cells.

## Installation

This package depends on IPython and RPy2, you may need to install them first.

### Install from PyPI

As of 2022-07-01, `tmagic` is available at `https://pypi.org/project/tmagic/`.
Install it as usual: `pip3 install tmagic`.

### Install from BitBucket

To install the package for yourself as user:

`pip install git+ssh://git@bitbucket.org/interquadrat/testmagic.git`

You will need to have the appropriate credentials to get this working.

### Install from a local repository

To get around BitBucket authentication issues, the trick is to install
from the _local_ Git repository.

Assuming that this local repo belongs to the user "teacher" that also has `sudo` rights,
then install the package for all users like this:

`sudo -H pip3 install git+file:///home/teacher/PROJECTS/training/testmagic`

where you may need to modify the path to the local repo.

## Preparation

Import the `ExerMagic` class and create an instance of it.
This instance stores exercise name / expected value pairs,
which can be passed either to the `ExerMagic()` constructor
or to the `register_tests()` method,
or be read from a JSON file.

In the example below we set up an exercise called `"answer"`
so that the correct value generated at the end should be `42`:

```
from tmagic import ExerMagic
magic = ExerMagic({"answer":42})
```

## Python exercises

Start a notebook cell with `%%pyexer <testname>` where `<testname>` is the name of the test
that you registered with the `ExerMagic` object (`"answer"` in the above example).
Then add one or more Python statements to the cell. 
The last statement must evaluate to the "expected value" (`42`) 
registered with the `"answer"` test.

The following exercise will fail:

```
%%pyexer answer
a = 6
b = 8
a*b
```

When executing this cell, the output will be:

```
Test failed :-(
48
```

This, however, will succeed:

```
%%pyexer answer
a = 6
b = 7
a*b
```

producing the output:

```
Test passed :-)
42
```
## R exercises

The R programming language exercises can be set up with the
`%%rexer` cell magic. These cells "see" the results of previous
notebook cells run with Rpy2's `%%R` magic. The above example
in R would look like this:

```
%%rexer answer
a <- 6
b <- 7
a*b
```

The response would be:

```
Test passed :-)
array([42.0,])
```

due to the peculiarities of the R<->Python variable mapping.