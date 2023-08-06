import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="awk_dataframe",
  version="0.2.9",
  description="Wrapper around awk to use as a dataframe implementation in python",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Carlos Molinero",
  author_email="",
  license="MIT",
  packages=["awk_dataframe"],
  include_package_data=True,
  zip_safe=False
)
