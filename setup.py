from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name="genix",
    version="0.1.2",
    description="GUI library for Pygame",
    long_description="Genix is a new pygame GUI library.  It aims to be very "
                     "readable, and straightforward when creating UI elements"
                     "like inventories or main menus for games.",
    url='https://github.com/thealec1/genix',
    author="Alec Reilly",
    author_email="areilly14@icloud.com",
    license='MIT',
    classifiers=classifiers,
    keywords=['pygame', 'interface', 'gui', 'ui'],
    packages=['genix', 'genix.components','genix.constraints','genix.containers'],
    install_requires=['pygame>=1.9.6']
)
