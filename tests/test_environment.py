"""Environment and tooling validation.

Contains no application or domain logic. These tests exist only to confirm that
the interpreter, the virtual environment, and src-layout packaging are correctly
configured before any project code is written.

Scope note: these tests assume an editable development checkout, which is what
`uv sync` produces at M0. They are not written for non-editable installs.
"""

import sys
from importlib.metadata import version as distribution_version
from pathlib import Path

import pehchaan

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_interpreter_is_python_311() -> None:
    assert sys.version_info[:2] == (3, 11)


def test_running_inside_a_virtual_environment() -> None:
    assert sys.prefix != sys.base_prefix


def test_package_is_imported_from_local_source() -> None:
    # Valid for an editable development checkout only. A non-editable install
    # (wheel installed into a container or CI image) resolves the module inside
    # site-packages and would fail this assertion despite being correct.
    # REVISIT WHEN CI IS INTRODUCED.
    assert pehchaan.__file__ is not None
    assert Path(pehchaan.__file__).resolve() == (
        REPO_ROOT / "src" / "pehchaan" / "__init__.py"
    ).resolve()


def test_package_version_matches_distribution_metadata() -> None:
    # Compares the module attribute against the INSTALLED DISTRIBUTION METADATA.
    # It does not read pyproject.toml. A pyproject.toml edit without a re-sync
    # can leave this passing while the two files disagree.
    assert pehchaan.__version__ == distribution_version("pehchaan-bench")