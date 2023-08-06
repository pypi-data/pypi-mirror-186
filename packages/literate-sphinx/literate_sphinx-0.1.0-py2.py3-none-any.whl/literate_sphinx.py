# Copyright Hubert Chathi
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# SPDX-License-Identifier: BSD-2-Clause

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


class LiterateCode(SphinxDirective):
    """Parse and mark up content of a literate code chunk.

    The argument is the chunk name
    """
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'class': directives.class_option,
        'file': directives.flag,
        'lang': directives.unchanged,
        'name': directives.unchanged,
    }
    has_content = True

    def run(self) -> list[nodes.Node]:
        options = normalized_role_options(self.options)
        language = options['lang'] if 'lang' in options else \
            self.env.temp_data.get('highlight_language', self.config.highlight_language)
        is_file = 'file' in options
        chunk_name = self.arguments[0]
        code = '\n'.join(self.content)
    
        literal_node = nodes.literal_block(code, code)
        
        literal_node['code-chunk-name'] = chunk_name
        if is_file:
            literal_node['code-chunk-is-file'] = True
        literal_node['language'] = language
        literal_node['classes'].append('literate-code') # allow special styling of literate blocks
        if 'classes' in options:
            literal_node['classes'] += options['classes']
        self.set_source_info(literal_node)
    
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
        self.add_name(container_node)
        return [container_node]
class TangleBuilder(Builder):
    name = 'tangle'
    epilog = 'The tangled files are in %(outdir)s.'

    def get_outdated_docs(self) -> str:
        return 'all documents'
    def get_target_uri(self, docname: str, typ: str = None) -> str:
        return ''
    def assemble_doctree(self) -> nodes.document:
        master = self.config.root_doc
        tree = self.env.get_doctree(master)
        tree = inline_all_toctrees(self, set(), master, tree, darkgreen, [master])
        return tree
    def write(self, *ignored: any) -> None:
        chunks = {} # dict of chunk name to list of chunks defined by that name
        files = [] # the list of files
    
        doctree = self.assemble_doctree()
    
        for node in doctree.findall(nodes.literal_block):
            if 'code-chunk-name' in node:
                name = node['code-chunk-name']
                chunks.setdefault(name, []).append(node)
                if 'code-chunk-is-file' in node:
                    files.append(name)
    
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
