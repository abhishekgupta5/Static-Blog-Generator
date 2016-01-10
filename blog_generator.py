#!/usr/bin/env python3

from markdown2 import Markdown
from os import listdir

#Static Blog Generator
def generate_post(source, destination):
    fobj_read = open(source)
    fobj_write = open(destination, 'w')

    markdown_object = Markdown()
    html_converted = markdown_object.convert(fobj_read.read())
    fobj_write.write(html_converted)

    fobj_read.close()
    fobj_write.close()

def convert_all_md(source, destination):

    markdown_object = Markdown()
    i = 1
    for fil in listdir(source):
        if fil.endswith('.md'):
            fobj_read = open(source+fil)
            html_converted = markdown_object.convert(fobj_read.read())
            fobj_write = open(destination+"markdown_converted_%d.html" % i , 'w')
            fobj_write.write(html_converted)
            i+=1
            fobj_read.close()
            fobj_write.close()
