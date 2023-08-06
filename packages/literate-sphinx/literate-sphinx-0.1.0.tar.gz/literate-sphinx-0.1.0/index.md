# Literate Sphinx

Literate Sphinx is a [literate
programming](https://en.wikipedia.org/wiki/Literate_programming) extension for
[Sphinx](https://www.sphinx-doc.org/).  Literate programming is a method for
writing code interleaved with text.  With literate programming, code is
intended to be written in an order that makes sense to a human reader, rather
than a computer.

Producing the human-readable document from the document source is called
"weaving", while producing the computer-readable code is called "tangling".  In
this extension, the weaving process is the normal Sphinx rendering process.
For tangling, this extension provides a `tangle` builder — running
`make tangle` will output the computer-readable files in `_build/tangle`.

As is customary with literate programming tools, the extension is also [written
in a literate programming style](#code).

## Usage

Install the extension in a place where Sphinx can find it, and add `'literate_sphinx'`
to the `extensions` list in your `conf.py`.

Code chunks are written using the `literate-code` directive, which takes the
name of the chunk as its argument.  It takes the following options:

* `lang`: the language of the chunk.  Defaults to `highlight_language`
  specified in `conf.py`
* `file`: (takes no value) present if the chunk is a file.  If the chunk is a
  file, then the code chunk name
* `class`: a list of class names separated by spaces to add to the HTML output
* `name`: a target name that can be referenced by `ref` or `numrf`.  This
  should not be confused with the code chunk name.

e.g in ReST

```rst
.. literate-code:: code chunk name
   :lang: python

   def hello():
       print("Hello world")
```

or in Markdown using [MyST
parser](https://myst-parser.readthedocs.io/en/latest/index.html)

~~~markdown
```{literate-code} code chunk name
:lang: python

def hello():
    print("Hello world")
```
~~~

To include another code chunk, enclose it between `{{` and `}}` delimiters.
Only one code chunk is allowed per line.  The code chunk will be prefixed with
everything before the delimiters on the line, and suffixed by everything after
the delimiters.

For example,

```rst
.. literate-code:: file.py
   :file:
   # before
   {{code chunk name}}
   # after
```

will produce a file called `file.py` with the contents

```python
# before
def hello():
    print("Hello world")
# after
```

and

```rst
.. literate-code:: file.py
   :file:
   # before
   class Hello:
       {{code chunk name}} # suffix
   # after
```

will produce

```python
# before
class Hello:
    def hello(): # suffix
        print("Hello world") # suffix
# after
```

The delimiters can be changed by setting the `literate_delimiters` option in
`conf.py`, which takes a tuple, where the first element is the left delimiter
and the second element is the right delimiter.  For example:

```python
literate_delimiters = ('<<', '>>')
```

The same code chunk name can be used for multiple chunks; they will be included
in the same order that they appear in the document.  If the document is split
across multiple files, they will be processed in the same order as they appear
in the table of contents as defined in the `toctree` directive.

## Code

Here is the implementation of the extension.

### `literate-code` directive

First, we define the `literate-code` directive:

```{literate-code} classes
class LiterateCode(SphinxDirective):
    """Parse and mark up content of a literate code chunk.

    The argument is the chunk name
    """
    {{LiterateCode variables}}

    {{LiterateCode methods}}
```

The directive takes one argument, which is required, and may contain
whitespace.

```{literate-code} LiterateCode variables
required_arguments = 1
final_argument_whitespace = True
```

The options are as defined above.  The `directives.*` values below specify how
the option values are validated.

```{literate-code} LiterateCode variables
option_spec = {
    'class': directives.class_option,
    'file': directives.flag,
    'lang': directives.unchanged,
    'name': directives.unchanged,
}
```

Obviously, code chunks need to have content.

```{literate-code} LiterateCode variables
has_content = True
```

Directives need one method: a `run` method that outputs a list of docutils
nodes to insert into the document.  Our `run` method will have three phases:
options processing, creating the `literal_block` to contain the code, and
creating a `container` node around the `literal_block` to add a caption.

```{literate-code} LiterateCode methods
def run(self) -> list[nodes.Node]:
    {{process literate-code options}}

    {{create literal_block}}

    {{create container node}}
```

First, we do some standard options processing from docutils.
(`normalized_role_options` is imported from `docutils.parsers.rst.roles`).

```{literate-code} process literate-code options
options = normalized_role_options(self.options)
```

Next, we determine the language used for syntax highlighting.  If a `:lang:`
option is given, we will use that value.  Otherwise, we use the
`highlight_language` config option.

```{literate-code} process literate-code options
language = options['lang'] if 'lang' in options else \
    self.env.temp_data.get('highlight_language', self.config.highlight_language)
```

If the `file` option is given, then the chunk represents a file.

```{literate-code} process literate-code options
is_file = 'file' in options
```

The chunk name is the arguments given to the directive.

```{literate-code} process literate-code options
chunk_name = self.arguments[0]
```

The code is the contents given to the directive.  The contents are given as a
list of lines, so we join them together with `\n`.

```{literate-code} process literate-code options
code = '\n'.join(self.content)
```

The code will be displayed in a `literal_block` (a mono-spaced block), and we
will add some attributes to store the options that were given.  The
`code-chunk-name` and `code-chunk-is-file` attributes will be used for
tangling.  The `language` attribute is used for syntax highlighting, and the
`classes` attribute is used for rendering the document.

```{literate-code} create literal_block
literal_node = nodes.literal_block(code, code)

literal_node['code-chunk-name'] = chunk_name
if is_file:
    literal_node['code-chunk-is-file'] = True
literal_node['language'] = language
literal_node['classes'].append('literate-code') # allow special styling of literate blocks
if 'classes' in options:
    literal_node['classes'] += options['classes']
```

We also call `set_source_info` from the parent class to set the source file and
line number for the node.

```{literate-code} create literal_block
self.set_source_info(literal_node)
```

The `literal_block` will be placed in a `container` node, along with a
`caption`.  We will use the code chunk name, followed by a `:`, as the caption,
so that readers can see the name.  If the code chunk is a file, we make the
caption monospaced.  The following code is based on the source code of
`sphinx.directives.code.container_wrapper`.

```{literate-code} create container node
container_node = nodes.container(
    '', literal_block=True,
    classes=['literal-block-wrapper', 'literate-code-wrapper']
)

if is_file:
    caption_node = nodes.caption(
        chunk_name + ':',
        '',
        nodes.literal(chunk_name, chunk_name),
        nodes.Text(':'),
    )
else:
    caption_node = nodes.caption(chunk_name + ':', chunk_name + ':')

self.set_source_info(caption_node)

container_node += caption_node
container_node += literal_node
```

We will add the name given in the `name` option (if any) to the container node,
so that references will link there.

```{literate-code} create container node
self.add_name(container_node)
```

And finally, we return a list containing the container node, since that is the
node to be added to the document.

```{literate-code} create container node
return [container_node]
```

### `tangle` builder

We now create a Sphinx `Builder` to "tangle" the document, that is, extract the
code chunks and produce the computer-readable source files.

```{literate-code} classes
class TangleBuilder(Builder):
    {{TangleBuilder variables}}

    {{TangleBuilder methods}}
```

We give our builder the name `tangle`, so the tangling can be done by running
`make tangle`, or using `sphinx-build -b tangle ...`.

```{literate-code} TangleBuilder variables
name = 'tangle'
```

When the builder completes, we will tell the user where the tangled files can
be found.

```{literate-code} TangleBuilder variables
epilog = 'The tangled files are in %(outdir)s.'
```

Builders need to implement several methods, some of which do not really apply
to us.

Since the output files don't correspond to input files, we tell Sphinx to read
all the inputs.

```{literate-code} TangleBuilder methods
def get_outdated_docs(self) -> str:
    return 'all documents'
```

We don't need to worry about generating URIs for our documents, since we will
not be creating references, so we just return an empty string.

```{literate-code} TangleBuilder methods
def get_target_uri(self, docname: str, typ: str = None) -> str:
    return ''
```

Now, we need a method that will give us the entire document as a single tree.
This function is taken from `sphinx.builders.singlehtml.SingleFileHTMLBuilder`.

```{literate-code} TangleBuilder methods
def assemble_doctree(self) -> nodes.document:
    master = self.config.root_doc
    tree = self.env.get_doctree(master)
    tree = inline_all_toctrees(self, set(), master, tree, darkgreen, [master])
    return tree
```

With this, we define the method that will write the source files.  This method
would normally be called with several arguments, but they are irrelevant to us,
so we will ignore them.  First, we will walk the document tree, looking for all
the code chunks.  We will record the chunks with their names, and if they
represent files, record their names in a list.  After all the chunks are
recorded, we will go through the list of files and write the files, expanding
the code chunk references as necessary.

```{literate-code} TangleBuilder methods
def write(self, *ignored: any) -> None:
    chunks = {} # dict of chunk name to list of chunks defined by that name
    files = [] # the list of files

    doctree = self.assemble_doctree()

    {{find code chunks in document}}

    {{write files}}
```

To look for code chunks, we walk the document tree, and find any
`literal_block` nodes that have a `code-chunk-name` attribute.  If the node
also has a `code-chunk-is-file` attribute, then we record the chunk name in the
`files` list.

```{literate-code} find code chunks in document
for node in doctree.findall(nodes.literal_block):
    if 'code-chunk-name' in node:
        name = node['code-chunk-name']
        chunks.setdefault(name, []).append(node)
        if 'code-chunk-is-file' in node:
            files.append(name)
```

Before we write the part of the function that will write out the files, we
first create a function that will process a single line from a code chunk and
write it out to a file.  If the line contains a reference to another code
chunk, it will expand the reference, otherwise it will write the line with any
necessary prefix or suffix.

The function will be passed the file to write to, the line to write, the
dictionary of chunks, the prefix and suffix to add to the line, and the left
and right delimiters used to enclose code chunk references.

```{literate-code} functions
def _write_line(
        f: io.IOBase,
        line: str,
        chunks: dict[str, Any],
        prefix: str,
        suffix: str,
        ldelim: str,
        rdelim: str,
) -> None:
    # check if the line contains the left and right delimiter
    s1 = line.split(ldelim, 1)
    if len(s1) == 2:
        s2 = s1[1].rsplit(rdelim, 1)
        if len(s2) == 2:
            # delimiters found, so find the code chunks belonging to that name
            for ins_chunk in chunks[s2[0].strip()]:
                for ins_line in ins_chunk.astext().splitlines():
                    # recursively call this function with each line of the
                    # referenced code chunks
                    _write_line(f, ins_line, chunks, prefix + s1[0], s2[1] + suffix, ldelim, rdelim)
            return

    # delimiters not found, so just write the line
    f.write(prefix + line + suffix + '\n')
```

Now for each output file, we create the file, look up the code chunks for the
file, get the contents of each chunk, split into lines, and use our function
above to write the lines.

```{literate-code} write files
# get the delimiters from the config
(ldelim, rdelim) = self.config.literate_delimiters

for filename in files:
    # some basic sanity checking for the file name
    assert '..' not in filename and not os.path.isabs(filename)
    # determine the full path, and make sure the directory exists before
    # creating the file
    fullpath = os.path.join(self.outdir, filename)
    dirname = os.path.dirname(fullpath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    with open(fullpath, 'w') as f:
        for chunk in chunks[filename]:
            for line in chunk.astext().splitlines():
                _write_line(f, line, chunks, '', '', ldelim, rdelim)
```

### Wrapping up

Now we need to tell Sphinx about our new directive, builder, and configuration
option, as well as some information about the extension.

```{literate-code} functions
def setup(app: Sphinx) -> dict[str, Any]:
    app.add_directive('literate-code', LiterateCode)

    app.add_builder(TangleBuilder)

    app.add_config_value(
        'literate_delimiters',
        ('{{', # need to split this across two lines, or else when we tangle
        '}}'), # this file, it will think it's a code chunk reference
        'env',
        [tuple[str, str]],
    )

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
```

And we put it all together in a Python file.

```{literate-code} literate_sphinx.py
:file:

# {{copyright license}}

'''A literate programming extension for Sphinx'''

__version__ = '0.1.0'

import io
import os
import re
from typing import Any, Iterator

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import normalized_role_options
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.util.console import darkgreen  # type: ignore
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import inline_all_toctrees


{{classes}}

{{functions}}
```

## Future plans

- link code chunks together
  - link to where code chunks are used
  - link to code chunk definitions
  - link to continued/previous definitions
- format code chunk references better (e.g. avoid syntax highlighting)
- warn about unused chunks
- guard against loops in chunk references
- allow multiple single-line chunks on a line
- add file names/line numbers in tangled files (when possible, for supported
  languages)

## License

This software may be redistributed under the same license as Sphinx.

```{literate-code} copyright license
:lang: text

Copyright Hubert Chathi

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

SPDX-License-Identifier: BSD-2-Clause
```
