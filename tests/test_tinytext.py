from __future__ import print_function, unicode_literals

import unittest

import tinytext


class TestTinyText(unittest.TestCase):
    def test_something(self):
        # Arrange

        # Act
        tiny = tinytext.tinytext("into tinier text")

        # Assert
        self.assertEqual(tiny, "ᶦᶰᵗᵒ ᵗᶦᶰᶦᵉʳ ᵗᵉˣᵗ")


if __name__ == "__main__":
    unittest.main()

# End of  file
