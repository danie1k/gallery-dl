#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2023 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Generate a document listing gallery-dl's command-line arguments"""

import os
import re
import sys

import util

import gallery_dl.util
gallery_dl.util.EXECUTABLE = True
from gallery_dl import option  # noqa E402


TEMPLATE = """# Command-Line Options

<!-- auto-generated by {} -->

{}"""


parser = option.build_parser()
parser.usage = ""

opts = parser.format_help()
opts = opts[8:]  # strip 'usage'
opts = re.sub(r"(?m)^(\w+.*)", "## \\1", opts)  # group names to headings
opts = opts.replace("\n  ", "\n    ")  # indent by 4


PATH = (sys.argv[1] if len(sys.argv) > 1 else
        util.path("docs", "options.md"))
with util.lazy(PATH) as fp:
    fp.write(TEMPLATE.format(
        "/".join(os.path.normpath(__file__).split(os.sep)[-2:]),
        opts,
    ))
