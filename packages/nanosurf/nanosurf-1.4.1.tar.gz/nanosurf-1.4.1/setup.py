# from setuptools import setup
# setup()
import os
from setuptools import setup, find_packages

def load_doc_file(readme_file_path: str) -> str:
    doc_str = ""
    with open(readme_file_path, "r", encoding="utf-8") as fh:
        doc_str = fh.read()
    return doc_str

def load_version(readme_file_path: str) -> str:
    ver_str = ""
    with open(readme_file_path, "r", encoding="utf-8") as fh:
        ver_str = fh.read()
    _, version = ver_str.split("=")
    version = version.replace('"', "").replace(" ", "")
    return version

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

package_data_files = []
package_data_files += package_files('nanosurf/app')
package_data_files += package_files('nanosurf/doc')
package_data_files += package_files('nanosurf_internal/app')
package_data_files += package_files('nanosurf_internal/doc')

long_description_file = load_doc_file('nanosurf/doc/README.md')

setup(
    name='nanosurf',
    version=load_version('nanosurf/_version.py'),
    author='Nanosurf AG',
    author_email='scripting@nanosurf.com',
    description='Python API for Nanosurf controllers',
    long_description=long_description_file,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(
        include=['*'],
    ),
    package_data={'': package_data_files},
    include_package_data = False,
    zip_safe=False,
    install_requires=['pywin32', 'matplotlib', 'numpy', 'scipy', 'notebook', 'pyside2', 'pyqtgraph', 'psutil', 'debugpy', 'lupa'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    entry_points={
        'console_scripts': [
            'nanosurf_help = nanosurf:help',
        ]
    },
    python_requires='>=3.9,<3.11'
)

