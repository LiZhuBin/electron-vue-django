from django.test import TestCase
from ..views import index

class TestIndex(TestCase):
    def test_index(self):
        print(index())

