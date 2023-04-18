from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test Item', 10.1)

            self.assertIsNone(ItemModel.find_by_name('Test Item'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test Item'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Test Item'))
