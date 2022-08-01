class TestsPage:

    def test_open_url(self, setup):

        assert 'shiningpanda' in setup.current_url, 'Web Page is not opened'
