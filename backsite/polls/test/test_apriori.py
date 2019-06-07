from unittest import TestCase

from django.test import TestCase
from ..views import Apriori


class TestApriori(TestCase):

    def response_check(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_apriori_data(self):
        print(self.response_check('http://localhost:8000/polls/apriori/getdata'))

    def test_apriori_run(self):
        print(self.response_check(''))

    def test_origin_data(self):
        print(Apriori.origin_data())

