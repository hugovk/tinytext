from __future__ import annotations

import tinytext


def test_something() -> None:
    # Arrange

    # Act
    tiny: str = tinytext.tinytext("into tinier text")

    # Assert
    assert tiny == "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"


def test_for_digits() -> None:
    # Arrange
    numbers = "".join(
        str(character) for character in range(9, -1, -1)
    )  # numbers = 9876543210

    # Act
    tiny: str = tinytext.tinytext(numbers)

    # Assert
    assert tiny == "⁹⁸⁷⁶⁵⁴³²¹⁰"
