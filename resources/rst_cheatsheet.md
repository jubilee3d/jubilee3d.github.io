# Restructured Text Cheatsheet

## Comments

````rst
..
   This indented line following two '.'s is a comment

````
Avoid inline comments since they can be confused with sphinx directives and fail silently.
See [Stack Overflow answer](https://stackoverflow.com/a/4783854).

## Links
Note that theme directives that include links may have slightly different syntax.

### Internal Links

* This is a `` `:ref:`page_name` `` whose text will assume page's title text.
* This is a `` `:ref:`display name <page_name>` `` who's text will say: <ins>display name</ins>. Note that the space before the first `<` is required.
* This is a : `` `:ref:`/folder/page_name` `` with an absolute filepath.


* Note: *.rst file extension is omitted.
* Note: each page must be included in a `toctree`. It is not sufficient to refer to a page solely with an internal link. It must also be included in a `toctree` *somewhere* in the website's *.rst pages.

### Internal Links in TOC Trees
If the page is listed in a `toctree` that is not `:hidden:`, it will be displayed with the title of that page.

````rst
.. toctree::

   page_name
   page2_name
````

you can rename the link as it will appear on the webpage with:
````rst
.. toctree::

   page_name
   Displayed Name <page2_name>
````

### Internal Links to Subsections

### External Links

This is `` `an external link <https://google.com>`_ ``

* *Note*: the `_` at the end is required.

## Code

### Code Blocks

Generic code blocks:
````rst
.. code::

   def my_func():
       print("Hello, world!")
````

* *Note*: the empty space between the first line and start of the code is required.
* *Note*: indentation must be consistent within a block and requires at least 2 spaces. (Prefer 3 spaces since `toctree` directives explicitly require 3 spaces.)

For language-specific code with syntax highlighting, put the language *short name* after the `::` with a space in between.
(See [Supported languages](https://pygments.org/languages/) for the supported language *Short names*.)
````rst
.. code:: python

   def my_func():
       print("Hello, world!")
````

### Inline Code

Preformatted without syntax highlighting: `` :code:`a = b + c` ``

This language-specific code with syntax highlighting: `` :python:`a = b + c` ``


## References
* [Intro to Documentation with Sphinx and reStructuredText](https://sphinx-intro-tutorial.readthedocs.io/en/latest/rst_intro.htm)