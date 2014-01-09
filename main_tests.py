import unittest

class MainTests(unittest.TestCase):

  def test_stuff(self):
    self.assertEqual(1+1, 2)

if __name__ == "__main__":
  unittest.main()