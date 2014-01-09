import unittest


class MainTests(unittest.TestCase):

    def test_stuff(self):
        self.assertEqual(1+1, 2)

    def test_git(self):
        self.assertIn("g", "git")

if __name__ == "__main__":
    unittest.main()