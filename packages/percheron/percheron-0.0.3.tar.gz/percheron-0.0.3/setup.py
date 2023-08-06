from setuptools import setup
from textwrap import dedent

VERSION = "0.0.3"


def get_long_description():
    return dedent("""
        # percheron

        Percheron is a data collation tool specifically designed to gather and collate the contributors for a release of the [Django](https://djangoproject.com) project. 

        It gathers data from a number of sources, including the commits to the Django project itself, issue tracking, pull requests, and translations. 

        For more information, read the [methodology](https://github.com/glasnt/percheron/tree/main/docs).

        For usage information, see the [GitHub README](https://github.com/glasnt/percheron)
    """)


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
