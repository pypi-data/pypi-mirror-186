from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
VERSION = (HERE / "miniapp" / "version").read_text().strip()

setup(
    name="miniapp",
    version=VERSION,
    description="Microservice Base",
    long_description=README,
    long_description_content_type="text/markdown",
    #url="n/a",
    #author="n/a",
    #author_email="n/a",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3"
    ],
    packages=["miniapp"],
    include_package_data=True,
    install_requires=["jsonschema"],
    extras_require={
        "all": ["pytz", "jinja2"]
    }
    #entry_points={
    #    "console_scripts": [
    #        "miniapp=miniapp.__main__:main",
    #    ]
    #}
)
