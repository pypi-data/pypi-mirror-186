from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="helloworld-rrodorr",
    version="0.0.1",
    description="Say hello!",
    py_modules=["helloworld"],
    package_dir={"": "src"},
    url="https://github.com/rrodorr/helloworld-rrodorr",
    author="rrodorr",
    author_email="rrodorr@posteo.net",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "pandas < 2.0",
    ],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "twine",
            "check-manifest",
            ],
        },
)

