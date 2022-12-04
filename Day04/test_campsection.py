from unittest import TestCase

from campsection import CampSectionRange, parse_pair


def does_overlap(pair_def: str) -> bool:
    left, right = parse_pair(pair_def)
    return left.overlaps(right)


class TestCampSectionRange(TestCase):
    def test_overlaps(self):
        cases = [
            ('1-3,3-6', True),
            ('1-2,3-5', False),
            ('4-9,4-5', True),
            ('4-5,4-9', True),
            ('3-9,4-5', True),
            ('4-5,3-9', True),
            ('67-84,66-87', True)
        ]
        for case in cases:
            self.assertEqual(case[1], does_overlap(case[0]), msg=f'Overlap check for "{case[0]} should have been {case[1]}')
