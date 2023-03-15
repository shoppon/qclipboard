from setuptools import find_packages
from setuptools import setup

setup(
    name="quick_clipboard",
    version="0.1.3",
    license="MIT",
    author="Shoppon",
    author_email="shopppon@gmail.com",
    description="A tool to copy text to clipboard and paste it to the frontmost application.",
    packages=find_packages("."),
    package_dir={"": "."},
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "quick-clipboard = quick_clipboard.main:main",
        ]
    },
)
