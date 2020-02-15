from unittest import TestCase

from pyaa.utils.formatting import (
    extract_aa,
)


class TestExtractAA(TestCase):

    def test_extract_from_left(self):
        test_cases = [
            [
                [
                    ' ____  ____  ___  ____ ',
                    '(_  _)( ___)/ __)(_  _)',
                    '  )(   )__) \__ \  )(  ',
                    ' (__) (____)(___/ (__) '
                ],
                [
                    ' ____ ',
                    '(_  _)',
                    '  )(  ',
                    ' (__) '
                ]
            ],
        ]

        for original, expected in test_cases:
            self.assertListEqual(extract_aa(6, original), expected)
