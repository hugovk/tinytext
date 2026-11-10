from __future__ import annotations

import io
import sys

import tinytext
from tinytext import cli


def test_something() -> None:
    # Arrange

    # Act
    tiny: str = tinytext.tinytext("into tinier text")

    # Assert
    assert tiny == "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"


def test_for_digits() -> None:
    # Arrange
    numbers = "9876543210"

    # Act
    tiny: str = tinytext.tinytext(numbers)

    # Assert
    assert tiny == "⁹⁸⁷⁶⁵⁴³²¹⁰"


def test_cli_cp1252_stdout(monkeypatch) -> None:
    # Arrange
    monkeypatch.setattr(sys, "argv", ["tinytext", "hello"])
    buffer = io.BytesIO()
    monkeypatch.setattr(sys, "stdout", io.TextIOWrapper(buffer, encoding="cp1252"))

    # Act
    cli.main()
    sys.stdout.flush()

    # Assert
    assert buffer.getvalue().decode("utf-8").strip() == "ʰᵉᶫᶫᵒ"
