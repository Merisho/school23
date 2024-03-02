import unittest
import gameoflife


class MyTestCase(unittest.TestCase):
    def test_cell_alive(self):
        game = gameoflife.Game([
            [0, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
        ])

        is_alive = game.is_cell_alive(1, 1)
        self.assertTrue(is_alive, 'cell must live')

        is_alive = game.is_cell_alive(0, 3)
        self.assertTrue(is_alive, 'cell must live')

        is_alive = game.is_cell_alive(2, 2)
        self.assertFalse(is_alive, 'cell must die')

        is_alive = game.is_cell_alive(3, 3)
        self.assertFalse(is_alive, 'cell must die')

        is_alive = game.is_cell_alive(2, 1)
        self.assertFalse(is_alive, 'cell must die')

        is_alive = game.is_cell_alive(1, 0)
        self.assertTrue(is_alive, 'cell must resurrect')



if __name__ == '__main__':
    unittest.main()
