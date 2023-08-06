# Test pluglet for mkdocs-macros

## What it is
This is a test **pluglet** for mkdocs-macros.
Its purpose is to serve as a template
for pluglets.

It exports three macros, which can be used in markdown pages, and aren't particularly
interesting:

- `test_fn(x:float)`: an arithmetic expression.
- `say_hello(s:str)`: displays Hello followed by the string, in italics.
- `test_fn2(s:str)`: same as `say_hello()`but does it slightly differently

For example, you could write:

    He said {{ say_hello('Joe') }}.

Which will be translated into HTML as:

    He said <i>Hello Joe</i>

## How to install it

Directly from pypi:
`pip install mkdocs-macros-test`

Or directly from the github repository: download
the package and run:
`python setup.py install`

## How to call it from an MkDocs project

In the config (`mkdocs.yml`) file:

```yaml
plugins:
  - search
  - macros:
      modules: ['mkdocs_test`] 
```


### Notes
https://github.com/fralau/mkdocs_macros_plugin
question - can this plugin be used to change the jinja2 environment that mkdocs uses?

use case:
i would like to be able to install a jinja2 extension and then use that extension in my custom mkdocs theme

in particular: 
https://github.com/danielchatfield/jinja2_markdown

https://github.com/fralau/mkdocs_macros_plugin/blob/master/mkdocs_macros/plugin.py#L583