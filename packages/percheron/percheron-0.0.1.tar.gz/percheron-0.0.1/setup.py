from setuptools import setup
import os

VERSION = "0.0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="percheron",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Katie McLaughlin",
    url="https://github.com/glasnt/percheron",
    project_urls={
        "Issues": "https://github.com/glasnt/percheron/issues",
        "CI": "https://github.com/glasnt/percheron/actions",
        "Changelog": "https://github.com/glasnt/percheron/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["percheron"],
    entry_points="""
        [console_scripts]
        percheron=percheron.cli:cli
    """,
    install_requires=[
        "click",
        "GitPython",
        "requests",
        "requests-cache[all]",
        "rich-click",
        "tqdm",
        "nltk",
        "python-dotenv",
        "datasette",
        "sqlite-utils",
    ],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
