"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from django.test import TestCase

class ViewTest(TestCase):
    def test_URL(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "It  was not possible to reach the required URL.")

    def test_content(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Things</title>', html=True)
        self.assertContains(response, '<h1>Things</h1>', html=True)
