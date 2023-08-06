from setuptools import setup, find_packages

setup(
    name="pycooltext",
    description="A function to print cool text.",
    version="0.0.0",
    author="Hart Traveller",
    author_email="hart@cephalon.io",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["rich", "requests", "pathlib"],
)
