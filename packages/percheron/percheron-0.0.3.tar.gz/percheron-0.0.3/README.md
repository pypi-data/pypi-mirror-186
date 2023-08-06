# percheron

<table height="250px"><tr><td width="30%">
<img alt="percheron logo" src="docs/percheron_logo.png">
</td><td>

[![PyPI](https://img.shields.io/pypi/v/percheron.svg)](https://pypi.org/project/percheron/)

[![Changelog](https://img.shields.io/github/v/release/glasnt/percheron?include_prereleases&label=changelog)](https://github.com/glasnt/percheron/releases)

[![Tests](https://github.com/glasnt/percheron/workflows/Test/badge.svg)](https://github.com/glasnt/percheron/actions?query=workflow%3ATest)

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/glasnt/percheron/blob/master/LICENSE)
</td><tr><table>

Percheron is a data collation tool specifically designed to gather and collate the contributors for a release of the [Django](https://djangoproject.com) project. 

It gathers data from a number of sources, including the commits to the Django project itself, issue tracking, pull requests, and translations. 

For more information, read the [methodology](docs/).

## Installation

Install this tool using `pip`:

    pip install percheron

## Usage

To gather data for a specific release:

    percheron get [RELEASE]

For example: 

    percheron get 4.1

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd percheron
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
