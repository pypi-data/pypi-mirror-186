from setuptools import setup
from setuptools.command.install_scripts import install_scripts
import shutil

import setuptools
# from os.path import basename


class InstallScripts(install_scripts):

    def run(self):
        setuptools.command.install_scripts.install_scripts.run(self)

        # Rename some script files
        for script in self.get_outputs():
            if script.endswith(".py") or script.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)


# or
# from distutils.core import setup

setup(
    name='ppbank',
    version='2.2.5',
    description='PPbank Cli Tools',
    author='lhr',
    author_email='airhenry@gmail.com',
    url='https://docs.snquantum.com/ppbank',
    packages=['ppbank','resources'],
    # other arguments here...
    install_requires=[
        'coreapi',
        'typer',
        'requests'
        #        'python-docx'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    cmdclass={
        "install_scripts": InstallScripts
    },
    scripts=['ppbank/ppbank.py']
)
