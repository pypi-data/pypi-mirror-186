SRC_README_MD = """
# Loci Notes `_src` README
This directory is used by [Loci Notes](https://loci-notes.gitlab.io/) to store and process source code used in secure code reviews. Since code can be spread out across multiple people looking at the same codebases, it's important that the locations of code are normalized across all these different machines. This folder structure is the current [Loci Notes Standard for Source Code](https://loci-notes.gitlab.io/advanced/standards).

## Usage
You should store top level repositories to be reviewed in this folder. To do this correctly, clone them directly under `_src`.

```bash
$ cd _src && git clone https://github.com/user/repository repository
```
"""  # noqa: E501
