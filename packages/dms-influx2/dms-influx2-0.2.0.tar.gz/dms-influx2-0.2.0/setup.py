import os
import sys
import shutil

from setuptools import find_packages, setup, Command

NAME = 'dms-influx2'
DESCRIPTION = 'Library to connect and retrieve data from DMS influxdb'
URL = 'https://github.com/belingarb/dms-influx2'
EMAIL = 'bozidar.belingar@gmail.com'
AUTHOR = 'Bozidar Belingar'
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '0.2.0'

# Get required packages from requirements.txt file
with open('requirements/base.txt') as f:
    REQUIRED = f.read().splitlines()

dir_path = os.path.abspath(os.path.dirname(__file__))

long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(dir_path, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

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
            if os.path.exists(os.path.join(dir_path, 'dist')):
                shutil.rmtree(os.path.join(dir_path, 'dist'))
            if os.path.exists(os.path.join(dir_path, 'build')):
                shutil.rmtree(os.path.join(dir_path, 'build'))
            if os.path.exists(os.path.join(dir_path, f'{NAME}.egg-info')):
                shutil.rmtree(os.path.join(dir_path, f'{NAME}.egg-info'))
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
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "cli", "venv"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)
