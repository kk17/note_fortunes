#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path as path

NOTES_DIR = "notes"
DATA_DIR = "data"


def note2data(note_filename):
    basename = path.basename(note_filename)
    base = path.splitext(basename)[0]
    # print base
    infilepath = path.join(NOTES_DIR, note_filename)
    outfilepath = path.join(DATA_DIR, base)
    # print infilepath
    with open(infilepath,"r") as fi, open (outfilepath, "w") as fo:
        bookname = None
        lines_blocks = None

        def write_block(append_sign=True):
            if lines_blocks:
                if bookname:
                    lines_blocks.append(bookname)
                if append_sign:
                    lines_blocks.append("%\n")
                fo.writelines(lines_blocks)

        for line in fi:
            if not line.strip():
                continue
            if line.startswith("#") and line[1] != "#":
                bookname = line.replace("#","",1)
                # print bookname
            elif line.startswith("##") and line[2] != "#":
                write_block()
                line = line.replace("##","",1)
                # print line
                lines_blocks = []
                lines_blocks.append(line)
            else:
                lines_blocks.append(line)
            # print line
        write_block(False)


def allnote2data():
    for filename in os.listdir(NOTES_DIR):
        note2data(filename)

if __name__ == '__main__':
    # note2data("refactor_your_wetwart.md")
    allnote2data()
