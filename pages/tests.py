from django.test import TestCase

from pages.models import Page


class PagesTestCase(TestCase):
    def setUp(self):
        Page.create(title="about", description="about page description")

    def page_have_title(self):
        Page.objects.get(title="about")
