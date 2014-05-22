from django.test import TestCase
from news.views import kalimati_url
import unirest
from django.test.client import Client
# Create your tests here.
class TestHomePage(TestCase):
	def setUp(self):
		print "Begin"

	def tearDown(self):
		print "Exit"

	def test_homepage(self):
		c=Client()
		response = c.get('/')
		self.assertContains(response,"PyInformer")        
		
	def test_weather_present_location(self):
		c= Client
		response = c.get('/')
		self.assertContains(response,"Present Weather")

	def test_kalimati_url(self):
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code,200)


	def test_kalimati_bajar_info(self):
		c = Client()
		response = c.get('/')
		self.assertContains(response,'Daily Wholesale Price Bulletin')