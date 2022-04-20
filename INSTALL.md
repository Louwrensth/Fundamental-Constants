
# Installation

Installing the Fundamental Constants package requires zero dependencies beyond basic tools like 
`make`, it will simply copy pre-generated header files and pkg-config files to the installation 
directories.

The installation directories are the [conventional ones][1], but the directory variables can be 
modified, see [`Makefile.common`](Makefile.common).

For example:

```
make prefix=/opt docdir=/opt/docs
```

would install everything (include headers and pkg-config files) below `/opt`, but use a slightly 
different directory to copy the documentation to (which is this file and [`README.md`](Readme.md)).

[1]: https://www.gnu.org/software/make/manual/html_node/Makefile-Conventions.html
