from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="null-assessor", # the name that you will install via pip
    version="1.1",
    author="Keino Baird",
    author_email="keinobaird@gmail.com",
    description="Assess nulls in a dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/kbee181756/lambdata-keinobaird-p1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)