sc_kernel
=========

:Author:
    bsnacks000

:Current Version: 0.0.2

This is a Jupyter wrapper kernel for SuperCollider3 (sclang). You can install this
language kernel in a virtualenv along with jupyter and use sclang like you would in
the SC3 IDE to control scsynth via a Jupyter notebook or console. The kernel code is mostly
based on the bash_kernel by takluyver, the ipython docs and a few other examples.

The current version is not quite ready for release, but to install the development branch
clone this repo and use the Makefile to install the dev dependencies in a virtualenv.

Assuming that you already have a version of SuperCollider3 installed:

```
$ make install_dev
```
This gives you jupyter as well so you can test in this environment.

After its activated the command line utility to install the kernel:
```
$ install_kernel
```
This should automatically install the kernel in your activated environment's share/jupyter directory

From there use jupyter notebook and select the SuperCollider kernel from the dropdown or
try it from the console.

```
$ jupyter console --kernel supercollider
```
