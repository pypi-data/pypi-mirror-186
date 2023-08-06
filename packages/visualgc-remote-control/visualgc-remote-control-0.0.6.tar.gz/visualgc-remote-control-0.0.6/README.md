# VisualGC Remote Control
  
## Dependencies
 
## Installation

Before installing the adapter itself, install all the dependencies.

```bash
# example:
dpkg -i  
```

**Install from package**

Install the package with the following command:

```bash
# example:
dpkg -i *_all.deb
```
*Note: If you don't have the `*.deb` package available,
take a look to the [Building](#building) section*

After installation you can execute the script
```bash
 
```

## Building

As this adapter is written in python, there's no real build needed. However the
debian package can be created with the following commands.

```bash
debuild -us -uc
```

## Repository Structure

**/**

This is the main folder of the projects and contains configuration and source code of
the *visualgc-remote-control*.

**debian/**

This directory contains all packaging related information such as the *control* or the *rules* file
    
**docs/**

The *docs/* directory contains the documentations. It is written in *reStructuredText* and intended to be transformed
into a HTML-Documentation page or a PDF with Sphinx<sup>1</sup>. Be aware that the output and source is splitted into
separate directories (Source: *docs/source/*, Output: *docs/build/*).

## Pip package

In order to build and deploy pip packages to pip do the following

Build wheel package:

    python3 setup.py sdist bdist_wheel

Check wheel package:

    twine check dist/*

Upload package to test.pypi.org

    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Upload package to pypi.org

    twine upload dist/*

# Install
pip install --upgrade  --trusted-host pypi.org --trusted-host files.pythonhosted.org visualgc-remote-control

## Contributors
- Luis Coelho <luis.miguel.coelho@schindler.com>

## License

**This software is *not* licensed under any public licenses!**

> This software is the confidential and proprietary information of
> Schindler Elevator Ltd. ("Confidential Information"). You shall not disclose
> such confidential information and shall use it only in accordance with
> the terms of the license agreement you entered into with Schindler Ltd.

<sup>1</sup> *Sphinx* is a great way to document your project. It is able to transform your *reStructuredText* into HTML
    sites with really cool templates, into PDF's or even EPUB's.
    Take a look at the [Sphinx page](http://www.sphinx-doc.org/) for further information.
 