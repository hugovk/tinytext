from __future__ import annotations

import tinytext


def test_something() -> None:
    # Arrange

    # Act
    tiny: str = tinytext.tinytext("into tinier text")

    # Assert
    assert tiny == "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"
