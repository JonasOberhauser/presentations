# -*- coding: utf-8 -*-
"""
Patch .pdf_tex files through Inkscape's --export-latex option.

Usage:
$ python patch-export-latex.py <.pdf_tex filepath>

Examples:
$ inkscape -D -z --file=foobar.svg --export-pdf=figures/foobar.pdf --export-latex
$ python patch-export-latex.py figures/foobar

Copyright (C) 2016 Donghyeon "STUPID IDIOT" Lee
"""

import sys
import os.path
import re

def line_patcher(pages):
    def patcher(match):
        if int(match.group(1)) <= pages:
            return match.group(0)
        else:
            return ''
    return patcher
    
def patch(name, pages):
    pdftex = name + '.pdf_tex'
    with open(pdftex, 'r') as f:
        content = f.read()
    content = re.sub('.*\\\\put\(0\,0\)\{\\\\includegraphics\[width=\\\\unitlength\,page=(\d+).*', line_patcher(pages), content)
    with open(pdftex, 'w') as f:
        f.write(content)
    print 'fin'

#patch("RMWrace",4)
##patch("misalignedCASrace",4)
##patch("GengPartialHit",3)
##patch("Insertion",5)
##patch("ICBLOCKCompl",4)
##patch("BlockSuspensionInsert",8)
# patch("InsertionAndParallel",10)
# patch("MutableAndDirty",11)
# patch("ReorderIP",2)
# patch("ReorderS",5)
# patch("ReorderL",4)
patch("ReorderL",4)














