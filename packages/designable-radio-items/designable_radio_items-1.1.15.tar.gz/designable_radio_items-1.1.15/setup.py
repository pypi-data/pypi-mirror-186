import json

from setuptools import setup

with open("package.json", encoding="utf-8") as f:
    package = json.load(f)


def load_readme() -> str:
    with open("README.md", encoding="utf-8") as fin:
        return fin.read()


package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    packages=[package_name],
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers=[
        "Framework :: Dash",
    ],
)
