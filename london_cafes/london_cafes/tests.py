from django.test import TestCase
from .models import Ratings, Cafe

class CafeManagerTestCase(TestCase):
	
	def setUp(self):
		rating3 = Ratings.objects.create(id=1, rating=3)
		rating5 = Ratings.objects.create(id=2, rating=5)
		Cafe.objects.create(id=1, name="cafe1", description="desc1", address1="a1", address2="a2", address3="a3", city="city1", post_code="A1 ABC", atmosphere_rating=rating5, coffee_rating=rating3, wifi_rating=rating3)
		Cafe.objects.create(id=2, name="cafe2", description="desc2", address1="a1", address2="a2", address3="a3", city="city1", post_code="A1 ABC", atmosphere_rating=rating5, coffee_rating=rating5, wifi_rating=rating5)

	def test_exact_ratings_filters(self):
		cafe1 = Cafe.objects.filter(id__in=[1,2])
		#print(cafe1.atmosphere_rating.rating)
		cafes = Cafe.objects.atmosphere_exact_rating(5)
		#print(cafes)
		self.assertItemsEqual(cafes, cafe1)    
		