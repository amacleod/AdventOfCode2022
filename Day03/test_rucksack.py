from unittest import TestCase

import rucksack


class Test(TestCase):
    def test_item_priority(self):
        self.assertEqual(1, rucksack.item_priority('a'))
        self.assertEqual(26, rucksack.item_priority('z'))
        self.assertEqual(27, rucksack.item_priority('A'))
        self.assertEqual(52, rucksack.item_priority('Z'))
