from unicodedata import category
import unittest

from models.traveler import Traveler


class TestTraveler(unittest.Traveler):
    def setUp(self):
        self.traveler = Traveler("name", "category", 1)

    def test_traveler_has_name(self):
        self.assertEqual("name", self.name)

    def test_traveler_has_category(self):
        self.assertEqual("category", self.category)

    def test_traveler_has_id(self):
        self.assertEqual(1, self.id)