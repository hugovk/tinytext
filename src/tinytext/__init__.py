from __future__ import annotations

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python 3.7 and lower
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__)


__all__ = ["__version__"]


class Color:
    colors = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
    }


ENDLINE = "\x1b[0m\x1b[37m"


class TextColor:
    def __init__(self, text: str, new_color=Color.colors["white"]) -> None:
        self._text_color = f"\x1b[{new_color}m" + text + ENDLINE

    def __str__(self) -> str:
        return f"{self._text_color}"

    @property
    def change_color(self) -> str:
        return self._text_color

    @change_color.setter
    def change_color(self, new_color=Color.colors["white"]) -> None:
        self._text_color = f"\x1b[{new_color}m" + self._text_color[5:-9] + ENDLINE


tiny_letters: dict[int, str] = {
    ord("a"): "ᵃ",
    ord("b"): "ᵇ",
    ord("c"): "ᶜ",
    ord("d"): "ᵈ",
    ord("e"): "ᵉ",
    ord("f"): "ᶠ",
    ord("g"): "ᵍ",
    ord("h"): "ʰ",
    ord("i"): "ᶦ",
    ord("j"): "ʲ",
    ord("k"): "ᵏ",
    ord("l"): "ᶫ",
    ord("m"): "ᵐ",
    ord("n"): "ᶰ",
    ord("o"): "ᵒ",
    ord("p"): "ᵖ",
    ord("q"): "ᑫ",
    ord("r"): "ʳ",
    ord("s"): "ˢ",
    ord("t"): "ᵗ",
    ord("u"): "ᵘ",
    ord("v"): "ᵛ",
    ord("w"): "ʷ",
    ord("x"): "ˣ",
    ord("y"): "ʸ",
    ord("z"): "ᶻ",
    ord("A"): "ᴬ",
    ord("B"): "ᴮ",
    ord("C"): "ᶜ",
    ord("D"): "ᴰ",
    ord("E"): "ᴱ",
    ord("F"): "ᶠ",
    ord("G"): "ᴳ",
    ord("H"): "ᴴ",
    ord("I"): "ᴵ",
    ord("J"): "ᴶ",
    ord("K"): "ᴷ",
    ord("L"): "ᴸ",
    ord("M"): "ᴹ",
    ord("N"): "ᴺ",
    ord("O"): "ᴼ",
    ord("P"): "ᴾ",
    ord("Q"): "ᑫ",
    ord("R"): "ᴿ",
    ord("S"): "ˢ",
    ord("T"): "ᵀ",
    ord("U"): "ᵁ",
    ord("V"): "ⱽ",
    ord("W"): "ᵂ",
    ord("X"): "ˣ",
    ord("Y"): "ʸ",
    ord("Z"): "ᶻ",
    ord("`"): "`",
    ord("~"): "~",
    ord("!"): "﹗",
    ord("@"): "@",
    ord("#"): "#",
    ord("$"): "﹩",
    ord("%"): "﹪",
    ord("^"): "^",
    ord("&"): "﹠",
    ord("*"): "﹡",
    ord("("): "⁽",
    ord(")"): "⁾",
    ord("_"): "⁻",
    ord("-"): "⁻",
    ord("="): "⁼",
    ord("+"): "+",
    ord("{"): "{",
    ord("["): "[",
    ord("}"): "}",
    ord("]"): "]",
    ord(":"): "﹕",
    ord(";"): "﹔",
    ord("?"): "﹖",
}


def tinytext(big: str) -> str:
    """convert your text ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ"""
    tiny: str = big.translate(tiny_letters)
    return tiny


def colored_tinytext(big: str, new_color: str = "") -> str:
    """convert your text ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ with color"""
    tiny: str = big.translate(tiny_letters)
    try:
        color_tiny: str = TextColor(tiny, Color.colors[new_color])
    except KeyError:
        print("Color not changed")
        color_tiny: str = TextColor(tiny)
    return color_tiny


# End of file
# print(colored_tinytext('HI','red'))
