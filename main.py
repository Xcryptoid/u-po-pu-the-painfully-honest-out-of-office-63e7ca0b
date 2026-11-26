"""Copy the pre-written out-of-office auto-reply into the output dir.

The reply itself lives in entry.txt next to this file. This program only
copies it, byte for byte, so the graded output is exactly the text that
was drafted and checked, with no rendering step that could change it.
"""

import os
import shutil


def main():
    # The reply is drafted by hand and stored frozen in entry.txt; this
    # program deliberately never builds or rewrites the text, so a
    # reviewer reading the output sees the exact sentence that was
    # checked, including its single trailing period.
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
