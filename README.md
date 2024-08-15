# jubilee3d.github.io

Documentation website for the Jubilee ecosystem.


## Writing the Docs

Docs are built using [Sphinx](https://www.sphinx-doc.org/en/master/) using the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/) theme. 
Individual docs are written in Restructured Text format which has its own distinct syntax ([cheatsheet](https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst)).

### Installing the toolchain
With Python and pip installed, from this folder, invoke:
````bash
pip install -r requirements.txt
````

### Build the docs locally
From the top folder, invoke:
````bash
make html
````
(If you're running on Windows you may need to install Make for Windows.)

This will create another folder called *build* where the generated html files will exist.

### Read the docs locally

The generated html files in the *build* folder can be opened as-is, but javascript commands will not be executed.
To read the docs in their final form, you can launch a local server to host them.

To view the docs locally, from the top folder run:
````bash
sphinx-autobuild docs build/html
````

### Deploying the docs online
Github Actions have been setup such that pushes to the main branch will trigger the website to regenerate online.



## Conventions

* for locally-hosted images, keep them small by using *.AVIF format ([AVIF converter](https://convertio.co/avif-converter/)).
