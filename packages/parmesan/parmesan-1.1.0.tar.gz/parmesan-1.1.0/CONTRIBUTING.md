# Contributing


### 👉 TL;DR: Just run `make` before `git push` to perform all checks 👈


Development follows the [GitLab Flow](https://about.gitlab.com/2014/09/29/gitlab-flow/). Read [:eyes: this Wiki page :book:](https://gitlab.com/tue-umphy/software/parmesan/-/wikis/GitLab-Workflow) for a detailed walkthrough. In short:

- If you want to improve something, create an issue and describe what you want to improve
- Get the repository onto your machine with `git clone ...`
- Install `PARMESAN` from the repository alongside the development requirements:

   ```bash
   pip install '.[dev]' # the . means this directory, the [dev] means ”install development requirements”
   ```

- (optionally) install `PARMESAN` in *editable* mode, so you don't have to reinstall it with `pip install .` every time you change something by running:

   ```bash
   pip install -e .
   # if the above didn't work, try
   pip install --user -e .
   # if the above didn't work, try
   pip install --prefix="$HOME/.local" -e .
   # if that doesn't work either, then let's hope for a fix in pip
   # Then you might need to reinstall PARMESAN after every change you make via
   # pip install .    🙄
   ```

- Create a branch for the issue either via the button at the issue or manually with `git switch -c ISSUENUMBER-title-of-the-issue && git push -u origin ISSUENUMBER-title-of-the-issue`
- Work on the branch as usual
- Before you commit, run `make` to be sure that everything is fine. This will build the documentation, run the tests and assert that the code is properly formatted.
- Commit and upload your changes with `git commit -a -m "Add feature bla blubb" && git push`
- If your branch is ready, create a Merge Request (GitLab will suggest a button to do that)
- In the Merge Request describe how your changes fix/improve the issue
- Somebody with merging rights will then comment and merge the request

## Code Style

Code should be formatted with [`black`](https://github.com/ambv/black) and follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

Be sure to have run the following commands before pushing commits. Otherwise, the CI pipeline will only pass with warnings.

```bash
python3 -m pip install install --user black pycodestyle
# format all Python files in black style
black .
# check PEP8 compatibility
pycodestyle .
```

Or in short:

```bash
make check-codestyle
# this will check whether the code is properly formatted
```

## Build Documentation

The documentation can be built by running

```bash
# Install sphinx plugins
python3 -m pip install sphinx_rtd_theme sphinxcontrib-mermaid nbsphinx
# Create the documentation
make -C docs html
# Open the documentation
xdg-open docs/_build/html/index.html
```

Or in short:

```bash
make docs
# this will build the documentation and show it in your browser
```

>>>
### Notebooks

If you work on the notebooks in the documentation, make sure to run the following in the repository:

```bash
pip install nbstripout
python -m nbstripout --install
```

This strips the output cells from the notebooks (i.e. plots, etc...) whenever you `git commit` so they don't get anchored in the history. The notebooks will be executed automatically during the generation of the documentation.

### 🎥 Asciinema Screencasts

You can add [Asciinema](https://asciinema.org/) screencasts to the sphinx documentation.

Record a screencast to a file `docs/source/asciinema/myscreencast.cast` in the PARMESAN repository with:

```bash
# 'pip install asciinema' if it is not installed
asciinema rec docs/source/asciinema/myscreencast.cast
# then the terminal is reset and everything from then on is recorded
# exit via 'exit' or CTRL-D to stop the recording
```

Include this screencast in the sphinx documentation with

```rst
.. asciinema:: asciinema/myscreencast.cast
```
>>>

## Versioning

We use [semantic versioning](https://semver.org/).

Versions are added manually as git tags.

You can see a changelog based on the annotated version tags by running this command:

```bash
git tag -l 'v*' -n99 --sort=-version:refname --format='%(color:green)%(refname:strip=2)%(color:yellow) (%(color:cyan)%(creatordate:format:%a %b %d %Y)%(color:yellow))%0a%(color:magenta)==========================%0a%0a%(color:yellow)%(contents:subject)%(color:normal)%0a%0a%(contents:body)'
```

To mark the current commit as a version, run

```bash
# start the tag with a lowercase v
# and u
git tag -a v1.2.3
```

You editor will then open. Write the version summary and **please** read [How
to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/). At
least write a short first line, **then leave a blank line**, then write
whatever you think should be in the release notes.

Then publish the version tag:

```bash
git push --tags
```

## Tests

To run the tests, run

```bash
python3 -m unittest -v
```

To get a test coverage, run

```bash
# Install coverage
python3 -m pip install --user coverage
# Run the tests
python3 -m coverage run --source parmesan -m tests -v
# Show the coverage
python3 -m coverage report
# Create a HTML report
python3 -m coverage html
# View the HTML page
xdg-open html/index.html
```

Or in short:

```bash
make coverage
# this will run the tests and open the coverage report in your browser
```

## Writing tests

For now just look at the existing tests for an example how to test something. Basically, you create a file `test_myfeature.py` in the `tests` folder which looks like this:

```python
import unittest

class MyFeatureTest(unittest.TestCase):
    """
    This class groups together tests for my feature
    """

    def test_myfeature(self):
        # here you calculate something and then you can use
        # one of the many self.assert* functions to make sure
        # that some result is equal to something else, etc...
        # Look it up in the Python unittest documentation.
        # for example:
        self.assertEqual(1,2) # this will fail obviously

    def test_my_other_feature(self):
        # you can and should write multiple tests
```
