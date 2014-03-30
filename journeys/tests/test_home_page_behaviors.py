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
        journey1.trail_set.create(name="trail 1", description="Trail 1 description")
        journey1.trail_set.create(name="trail 2", description="Trail 2 description")
        journey2 = Journey.objects.create(name="Fix your brain", description="Become the bomb when it comes to brain hacking")

        "When I visit the home page"
        response = self.app.get('/')

        "I should the name and description of both journeys"
        response.mustcontain(journey1.name)
        response.mustcontain(journey1.description)
        response.mustcontain(journey1.trail_set.all()[0].name)
        response.mustcontain(journey1.trail_set.all()[1].name)
        response.mustcontain(journey2.name)
        response.mustcontain(journey2.description)

    def test_trails_can_have_links(self):
        "Given a journey exists with a linked trail"
        journey1 = Journey.objects.create(name="Learn Django", description="Become the bomb at Django")
        journey1.trail_set.create(name="Complete Django tutorial", description="Do it all", url="https://docs.djangoproject.com/en/dev/intro/tutorial01/")

        "When I visit the home page"
        response = self.app.get('/')

        "Then the trail should have a link"
        response.mustcontain('<a href="%s">Complete Django tutorial</a>' %  "https://docs.djangoproject.com/en/dev/intro/tutorial01/")

    def test_trails_do_not_need_links(self):
        "Given a journey exists with a non-linked trail"
        journey1 = Journey.objects.create(name="Do Django", description="Write a simple Django app")
        journey1.trail_set.create(name="Complete Django tutorial", description="Do it all")

        "When I visit the home page"
        response = self.app.get('/')

        "Then the trail should not have a link"
        response.text.should_not.contain('Do Django</a>')
