from django_webtest import WebTest

import sure

from journeys.models import Journey


class TestHomePageBehaviors(WebTest):
    """Tests behaviors of the home home page
    """

    def test_home_page_shows_title(self):
        "Given the site is functioning"

        "When I visit the home page"
        response = self.app.get('/')

        "I should see the page title"
        response.mustcontain('<title>The Path</title>')
        response.mustcontain('<h1>The Path</h1>')

    def test_home_page_shows_journeys(self):
        "Given two journeys exist"
        journey1 = Journey.objects.create(name="Learn Django", description="Become the bomb when it comes to Django")
        journey2 = Journey.objects.create(name="Fix your brain", description="Become the bomb when it comes to brain hacking")

        "When I visit the home page"
        response = self.app.get('/')

        "I should the name and description of both journeys"
        response.mustcontain(journey1.name)
        response.mustcontain(journey1.description)
        response.mustcontain(journey2.name)
        response.mustcontain(journey2.description)
