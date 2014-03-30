from django.test import TestCase
from journeys.models import Journey

import sure


class TestModels(TestCase):
    """Tests model functionality
    """

    def test_journeys_have_multiple_trails(self):
        journey = Journey.objects.create(name="journey1", description = "a description")
        journey.trail_set.create(name="trail1", description="trail description1")
        journey.trail_set.create(name="trail2", description="trail description2")
        journey.trail_set.create(name="trail3", description="trail description3")

        journey.trail_set.all()[0].name.should.equal("trail1")
        journey.trail_set.all()[1].name.should.equal("trail2")
        journey.trail_set.all()[2].name.should.equal("trail3")
