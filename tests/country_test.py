import unittest

from models.country import Country

class TestCountry(unittest.Country):
    def setUp(self):
        self.country = Country("name", "category", 1)


    def test_country_has_name(self):
        self.assertEqual("name", self.name)

    def test_country_has_category(self):
        self.assertEqual("category", self.category)

    def test_country_has_id(self):
        self.assertEqual(1, self.id)