from setuptools import setup, find_packages

setup(
  name="aegis-engine",
  version="1.0.0",
  license="MIT",
  author="Bailey de Villiers",
  author_email="bailey.devilliers@gmail.com",
  packages=find_packages("scripts"),
  package_dir={'': "scripts"},
  url='https://github.com/itchysnake/aegis',
  keywords="digital marketing",
  install_requires=[
    "numpy>=1.2",
    "pandas>=1.5",
    "python-dateutil>=2.8",
    "pytz>=2022.7",
    "six>=1.16",
    "webencodings>=0.5"
  ],
)