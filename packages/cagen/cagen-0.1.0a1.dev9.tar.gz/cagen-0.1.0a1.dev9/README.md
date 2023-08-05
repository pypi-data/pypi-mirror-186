# cagen

## About

cagen is a static site generator intented for [cmpalgorithms project](https://sr.ht/~somenxavierb/cmpalgorithms/). So it's very rare you are interested in that.

## License

The software is distributed under [GPL2-only license](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).

## How it runs

It assumes your documents are in markdown syntax. It is capable of convert those documents in any other format, using [pandoc](https://pandoc.org/) (specifically [pypandoc](https://github.com/JessicaTegner/pypandoc) wrapper) and [Mako Templating System](https://www.makotemplates.org/).

The reason to use "external" templating sytem instead of built-in pandoc templat system is because pandoc templates [are not capable to make conditions with values](https://pandoc.org/MANUAL.html#conditionals) (something like `$if(author=='me') Print full name here $endif$`).

The program just convert markdown files to HTML ones by default in the same directory. There is no predefined structure by default unlike many other static site generators do: no `assets` directory nope `site` directory. By default, all generated files are in the same directory than the source files. Obviously, you can modify it if you want.

We provide:

- a [library](https://git.sr.ht/~somenxavierb/cagen/tree/main/item/src/cagen/libcagen.py)
- a [command line program](https://git.sr.ht/~somenxavierb/cagen/tree/main/item/src/cagen/cagen.py) for convert documents
- a script called [`cagen-make`](https://git.sr.ht/~somenxavierb/cagen/tree/main/item/src/cagen/cagen-make.py) to generate a Makefile to convert automatically all markdown files to HTML ones.

The software is implemented in [python](https://www.python.org/) because it's easy to program (I'm very language-neutral). If you want some really fast static site generator, be free to fork the project and program with any compiled language.

## Installation

You can install via [pip](https://pypi.org/project/cagen/):

```
pip install cagen
```

## Issue tracker

You can see the [issue tracker](https://todo.sr.ht/~somenxavierb/cagen-tasks) and contribute if you want suggesting new features or reporting a bug.
