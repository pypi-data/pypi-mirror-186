import sys
import os
import sysconfig
from setuptools import setup, Extension, find_packages

from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

def main():
    setup(
        name="strcompare",
        version="1.2.2",
        description="Methods to assess string similarity.",
        readme="README.md",
        ext_modules=[Extension(
            name="strcompare",
            sources=['src\\strcompare_module.c'],
        )],
        author="Slick Nick",
        author_email="nfeezor@gmail.com",
        url="https://github.com/The-Slick-Nick/string-compare",
        long_description=long_description,
        long_description_content_type='text/markdown'
    )


if __name__ == "__main__":
    main()
