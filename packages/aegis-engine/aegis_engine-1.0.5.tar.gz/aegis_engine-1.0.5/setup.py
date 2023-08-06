from setuptools import setup, find_packages

setup(
  name="aegis_engine",
  version="1.0.5",
  license="MIT",
  author="Bailey de Villiers",
  author_email="bailey.devilliers@gmail.com",
  description = "Capital market asset valuation engine.",
  long_description=open("README.md", 'r').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/itchysnake/aegis',
  keywords="",

  # Finds all sub-packages except those in "exclude"
  packages = find_packages(
  ),
  exclude_package_data={
        '': ['config.py'],
  },
  package_dir={"":"."},
  install_requires=[
    "numpy>=1.2",
    "pandas>=1.5",
    "python-dateutil>=2.8",
    "pytz>=2022.7",
    "six>=1.16",
    "webencodings>=0.5"
  ],
)