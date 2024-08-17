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

### Auto-build and host the docs locally

The generated html files in the *build* folder can be opened as-is, but any embedded Javascript will not be executed.

To read the docs in their final form, from the top folder, run:
````bash
sphinx-autobuild docs/source docs/build/html
````

This will make the docs continuously every time you save changes to the source files *and* launch a local server to host them at [](http://127.0.0.1:8000/).

### Deploying the docs online
Github Actions have been setup such that pushes to the main branch will trigger the website to regenerate online.


## Conventions

### Images
For locally-hosted images, keep them small by using \*.AVIF format ([AVIF converter](https://convertio.co/avif-converter/)).

On Linux, you can re-encode an image with:
````bash
avifenc <input_image_name>.<extension> <output_image_name>.avif
````
On Windows, modern Gimp (2.10.38) supports avif file export.

Prefer removing background where possible.

Prefer a dark-and-light mode compatible image.
If removing the background from an image is not sufficient to make it usable on both modes, consider uploading separate dark and light-mode specific images.

### Colors
Use an accessible color palette. Check against [Viz-Palette](https://projects.susielu.com/viz-palette)
