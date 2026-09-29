from pytest import Config, DoctestItem, Item, Parser


def pytest_addoption(parser: Parser) -> None:
    """Add `--doctest-only` option."""

    parser.addoption(
        '--doctest-only',
        action='store_true',
        default=False,
        help='Run only doctests',
    )


def pytest_collection_modifyitems(config: Config, items: list[Item]) -> None:
    """Mark all tests in `/tests` as excluded from doctest runs."""

    doctest_only: bool = config.getoption('--doctest-only')
    items[:] = [
        item
        for item in items
        if (
            isinstance(item, DoctestItem)
            if doctest_only
            else (
                not isinstance(item, DoctestItem)
                and item.get_closest_marker('doctest_only') is None
            )
        )
    ]
