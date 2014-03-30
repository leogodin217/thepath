from django_webtest import WebTest

import sure


class TestHomePageView(WebTest):
    """Tests view functionality of the home page
    """

    def test_home_page_returns_OK(self):
        response = self.app.get('/')
        response.status.should.equal('200 OK')
