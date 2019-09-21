from typing import Dict

import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version


tiny_letters: Dict[int, str] = {
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
    tiny = big.translate(tiny_letters)
    return tiny


# End of file
