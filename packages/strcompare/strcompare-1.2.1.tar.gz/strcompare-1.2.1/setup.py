import sys
import os
import sysconfig
from setuptools import setup, Extension, find_packages


def path_to_build_folder():
    f = "{dirname}.{platform}-{version[0]}.{version[1]}"
    dir_name = f.format(
        dirname='lib', platform=sysconfig.get_platform(), version=sys.version_info
    )
    return os.path.join('build', dir_name, 'strcompare')

def main():
    setup(
        name="strcompare",
        version="1.2.1",
        description="Methods to assess string similarity.",
        ext_modules=[Extension(
            name="strcompare",
            sources=['src\\strcompare_module.c'],
            include_dirs=[
                os.path.join(path_to_build_folder(), 'compare_functions'),
                os.path.join(path_to_build_folder(), 'components')
            ]
        )],
        author="Slick Nick",
        author_email="nfeezor@gmail.com",
        url="https://github.com/The-Slick-Nick/string-compare",
        packages=find_packages(where='src'),
        package_dir={"": "src"},
        package_data = {'strcompare': ['compare_functions\\*.h', 'components\\*.h']},
    )


if __name__ == "__main__":
    main()
