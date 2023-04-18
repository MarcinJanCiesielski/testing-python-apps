from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel("Test Item", 10.1)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 10.1)

    def test_item_json(self):
        item = ItemModel("Test Item", 10.1)
        expected = {'name': "Test Item", 'price': 10.1}

        self.assertDictEqual(item.json(), expected)