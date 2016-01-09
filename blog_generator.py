#!/usr/bin/env python3
from markdown2 import Markdown

#Static Blog Generator
def generate_post(source, destination):
    fobj_read = open(source)
    fobj_write = open(destination, 'w')

    markdown_object = Markdown()
    html_converted = markdown_object.convert(fobj_read.read())
    fobj_write.write(html_converted)

    fobj_read.close()
    fobj_write.close()
