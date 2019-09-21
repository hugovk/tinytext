import tinytext
from hypothesis_auto import auto_pytest_magic


def test_something():
    # Arrange

    # Act
    tiny = tinytext.tinytext("into tinier text")

    # Assert
    assert tiny == "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"


auto_pytest_magic(tinytext.tinytext)
