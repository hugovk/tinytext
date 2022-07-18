from __future__ import annotations

from hypothesis_auto import auto_pytest_magic  # type: ignore[import]

import tinytext


def test_something() -> None:
    # Arrange

    # Act
    tiny: str = tinytext.tinytext("into tinier text")

    # Assert
    assert tiny == "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"


auto_pytest_magic(tinytext.tinytext)
