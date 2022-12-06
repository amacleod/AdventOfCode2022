from unittest import TestCase

import crates


class Test(TestCase):
    def test_columns(self):
        cols = crates.columns('[A] [B]    ', 4)
        self.assertEqual('[A] ', cols[0])
        self.assertEqual('[B] ', cols[1])
        self.assertEqual('   ', cols[2])
        cols = crates.columns('    [Z]     [X]', 4)
        self.assertEqual('    ', cols[0])
        self.assertEqual('[Z] ', cols[1])
        self.assertEqual('    ', cols[2])
        self.assertEqual('[X]', cols[3])

    def test_crate_row(self):
        self.assertListEqual([None, 'Z', None, 'X'], crates.crate_row('    [Z]     [X]\n'))

    def test_parse_move(self):
        move = crates.parse_move("move 3 from 2 to 1")
        # Source and target should be 0-indexed after parsing
        self.assertEqual(1, move.source)
        self.assertEqual(0, move.target)
        self.assertEqual(3, move.quantity)
