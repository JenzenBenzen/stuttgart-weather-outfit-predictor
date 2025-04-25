import unittest
from logic import outfit_recommendation

class TestOutfitRecommendation(unittest.TestCase):
    def test_tshirt(self):
        self.assertEqual(outfit_recommendation(25), "T-Shirt")

    def test_pullover(self):
        self.assertEqual(outfit_recommendation(18), "T-Shirt + Pullover")

    def test_jacket(self):
        self.assertEqual(outfit_recommendation(5), "T-Shirt + Jacket")

if __name__ == "__main__":
    unittest.main()
