from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError

# Create your tests here.
class ThingsModelTestCase(TestCase):
    def setUp(self):
        self.thing = Thing(
            name="Valid Name", 
            description="Valid Description", 
            quantity=50
        )

    def test_valid_thing(self):
        self._assert_thing_is_valid()

    def test_name_must_be_unique(self):
        thing2 = Thing(
            name="new thing", 
            description="Valid Description", 
            quantity=50
        )
        thing2.save() 
        self.thing.name = thing2.name
        self._assert_thing_is_invalid()

    def test_name_cannot_be_blank(self):
        self.thing.name = ''
        self._assert_thing_is_invalid()

    def test_name_can_contain_30_characters(self):
        self.thing.name = 'x' * 30
        self._assert_thing_is_valid()

    def test_name_cannot_contain_more_than_30_characters(self):
        self.thing.name = 'x' * 31
        self._assert_thing_is_invalid()

    def test_description_need_not_be_unique(self):
        thing2 = Thing(
            name="new thing", 
            description="Valid Description", 
            quantity=50
        )
        self.thing.description = thing2.description
        self._assert_thing_is_valid()

    def test_description_can_be_blank(self):
        self.thing.description = ''
        self._assert_thing_is_valid()

    def test_description_can_contain_120_characters(self):
        self.thing.description = 'x' * 120
        self._assert_thing_is_valid()

    def test_description_cannot_contain_more_than_210_characters(self):
        self.thing.description = 'x' * 121
        self._assert_thing_is_invalid()

    def test_quantity_need_not_be_unique(self):
        thing2 = Thing(
            name="new thing", 
            description="Valid Description", 
            quantity=50
        )
        self.thing.quantity = thing2.quantity
        self._assert_thing_is_valid()

    def test_quantity_can_be_between_0_and_100(self):
        self.thing.quantity = 0
        self._assert_thing_is_valid()

    def test_quantity_cannot_be_less_than_0(self):
        self.thing.quantity = -1
        self._assert_thing_is_invalid()

    def test_quantity_cannot_be_more_than_100(self):
        self.thing.quantity = 101
        self._assert_thing_is_invalid()
        
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should be valid')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

