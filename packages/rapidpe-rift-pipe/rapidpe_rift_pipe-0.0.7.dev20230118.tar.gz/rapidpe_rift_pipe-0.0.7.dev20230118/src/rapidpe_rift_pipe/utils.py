#!/usr/bin/env python3
import textwrap


def print_output(fileobj, *args, **kwargs):
    """
    saving print statemets to html_file
    """
    print(textwrap.dedent(*args), file=fileobj, **kwargs)
