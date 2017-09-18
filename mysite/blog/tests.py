from django.test import TestCase

from .models import Post


class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Post(title="My entry title")
        self.assertEqual(str(entry), entry.title)
