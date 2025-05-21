# Logic-of-Thought (Logot)


<p>
    <a href="https://www.python.org/">
        <img alt="Build" src="https://img.shields.io/badge/Python-3.9+-1f425f.svg?color=purple">
    </a>
    <a href="https://copyright.princeton.edu/policy">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue">
    </a>
</p>

Official implementation of "Logic-of-Thought: Empowering Large Language Models with Logic Programs for Solving Puzzles in Natural Language"

![teaser](pics/teaser.png)

## Requirements

We use Clingo as the ASP solver. The simplest way to install it is via pip:

```bash
pip install clingo
```

If problems occur, please see here for details.

The code is tested with Python 3.9. Install required packages with:

```bash
pip install -r requirements.txt

```

## Quick Start

1. Experiment with a single puzzle
	- Demos of solving individual puzzles are available at ``root/src/demo_{task}.ipynb``.
	- Please provide your API key in the first block of the notebook.

2. Experiments of the paper

## Code Structure and Tips