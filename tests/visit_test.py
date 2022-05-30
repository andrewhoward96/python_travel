import unittest
from models.visit import Visit


class TestVisit(unittest.Visit):
    def setUp(self):
        self.visit = Visit("name", "category", 1)

    def test_visit_has_name(self):
        self.assertEqual("name", self.name)

    def test_visit_has_category(self):
        self.assertEqual("category", self.category)

    def test_visit_has_id(self):
        self.assertEqual(1, self.id)