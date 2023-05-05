from django.test import TestCase, Client
from django.urls import reverse

class TestGamesGraph(TestCase):
    def setUp(self):
        self.client = Client()

    def test_games_page_chart(self):
        response = self.client.get(reverse('compare'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<canvas id="comparegraph"></canvas>')
        self.assertContains(response, 'Sales Data Comparision')
        # self.assertContains(response, 'var sources_list')
        # self.assertContains(response, 'var sources_list_pc')
        # self.assertContains(response, 'var country')