"""Setup script for pylib-template"""

from setuptools import setup

setup(name='pylib-template',
      version='0.0.1',
      description='Template python library.',
      packages=['pylib'],
      license="MIT",
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
      ],
      author='Ayushman Kumar Banerjee',
      author_email='ayushmaan.banerjee@gmail.com',
      zip_safe=False,
      install_requires=["re"],
      )
