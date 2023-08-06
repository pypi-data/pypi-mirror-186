# -*- coding = utf-8 -*-
# @TIME : 2023/01/19 20:01
# @File : setup.py
# @Software : PyCharm

from setuptools import setup, Command
import sys
import os
from shutil import rmtree

VERSION = '0.1.0'
DESCRIPTION = 'EEMs_toolkit是一个可以在Python上对三维荧光（EEM）进行平行因子分析（PARAFAC）的工具包，' \
              '功能大致类似于MATLAB的drEEM toolbox。'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
REQUIRED = [
    'numpy', 'scipy', 'pandas', 'matplotlib', 'tensorly', 'tlviz', 'joblib', 'openpyxl'
]
here = os.path.abspath(os.path.dirname(__file__))
about = {'__version__': VERSION}


class UploadCommand(Command):
    """上传功能支持"""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name='EEMs-toolkit',
    version=VERSION,
    description=DESCRIPTION,
    author='HHhyJJ',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/HHhyJJ/EEMs-toolkit',
    python_requires='>=3.9.0',
    # packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    py_modules=['EEMs_toolkit'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)
