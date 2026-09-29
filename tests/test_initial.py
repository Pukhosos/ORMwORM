from pytest import mark


def test_discovery() -> None:
    """Test if pytest discovers `/tests` folder."""

    assert 0 == 0  # noqa: PLR0133


@mark.doctest_only
def test_doctest() -> None:
    """
    Test if doctest discovery works.

    >>> 0 == 0
    True
    """

    pass
