# Code

Here is the implementation of the extension.

## `literate-code` directive

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

## `tangle` builder

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

We also pass in two structures for bookkeeping.  The first is a `set` called
`unused`, which is set of all the chunk names that have not been used yet.
When we use a chunk, we will remove it from the set.  This will allow us to
report on chunks that have been defined, but not used.

The second is a `list` called `path`, which gives the path of chunk names, from
the root file, to the current chunk.  This will be used to detect cycles.  When
we encounter a chunk, we first check if the chunk name is already on the path,
and if so, a loop has been detected.  Otherwise, we push the chunk name onto
`path` before processing the referenced chunk.  After we have processed the
chunk, we will pop the chunk name from the list.

```{literate-code} functions
def _write_line(
        f: io.IOBase,
        line: str,
        chunks: dict[str, Any],
        prefix: str,
        suffix: str,
        ldelim: str,
        rdelim: str,
        unused: set[str],
        path: list[str],
) -> None:
    # check if the line contains the left and right delimiter
    s1 = line.split(ldelim, 1)
    if len(s1) == 2:
        s2 = s1[1].rsplit(rdelim, 1)
        if len(s2) == 2:
            # delimiters found, so get the chunk name
            chunk_name = s2[0].strip()
            # update bookeeping variables
            unused.discard(chunk_name)
            if chunk_name in path:
                path.append(chunk_name)
                raise ExtensionError(
                    'Loop found in chunks: {}'.format(' -> '.join(path)),
                    modname = __name__,
                )
            path.append(chunk_name)

            # write the chunks associated with the name
            try:
                ref_chunks = chunks[chunk_name]
            except KeyError:
                raise ExtensionError(
                    'Unknown chunk name: {}'.format(chunk_name),
                    modname = __name__,
                )
            for ins_chunk in ref_chunks:
                for ins_line in ins_chunk.astext().splitlines():
                    # recursively call this function with each line of the
                    # referenced code chunks
                    _write_line(
                        f,
                        ins_line,
                        chunks,
                        prefix + s1[0],
                        s2[1] + suffix,
                        ldelim,
                        rdelim,
                        unused,
                        path,
                    )

            path.pop()
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

# get all the chunk names; initially, all chunks are unused
unused = {name for name in chunks}

for filename in files:
    # some basic sanity checking for the file name
    if '..' in filename or os.path.isabs(filename):
        raise ExtensionError(
            "Chunk name is invalid file name: {}".format(filename),
            modname=__name__,
        )
    # determine the full path, and make sure the directory exists before
    # creating the file
    fullpath = os.path.join(self.outdir, filename)
    dirname = os.path.dirname(fullpath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    unused.discard(filename)

    with open(fullpath, 'w') as f:
        for chunk in chunks[filename]:
            for line in chunk.astext().splitlines():
                _write_line(f, line, chunks, '', '', ldelim, rdelim, unused, [filename])
```

After we've written all the file, we emit a warning for every unused chunk,
giving the file name and line where the chunk is defined.

```{literate-code} write files
for chunk_name in unused:
    for chunk in chunks[chunk_name]:
        logger.warning(
            '{0.source}:{0.line}: Code chunk "{1}" defined but not used'
                .format(chunk, chunk_name)
        )
```

## Wrapping up

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

__version__ = '0.1.1'

import io
import os
import re
from typing import Any, Iterator

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import normalized_role_options
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.errors import ExtensionError
from sphinx.util import logging
from sphinx.util.console import darkgreen  # type: ignore
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import inline_all_toctrees


logger = logging.getLogger(__name__)

{{classes}}

{{functions}}
```

## Future plans

- link code chunks together
  - link to where code chunks are used
  - link to code chunk definitions
  - link to continued/previous definitions
- format code chunk references better (e.g. avoid syntax highlighting)
- allow multiple single-line chunks on a line
- add file names/line numbers in tangled files (when possible, for supported
  languages)

