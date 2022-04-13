
from tabnanny import check
from django.test import TestCase,Client
from django.urls import reverse, resolve
from bookroom.views import index
from .models import Reservation, Rental
from datetime import timedelta, date

# url test case '


class TestUrls(TestCase):
    

    def test_view_url_resolves(self):
        url = reverse('index_url')
        
        self.assertEquals(resolve(url).func, index)


 



class TestViews(TestCase):

    
    def test_reservation_list_GET(self):
        client = Client()

        response = client.get(reverse('index_url'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'view_booking.html')


class TestModels(TestCase):
    def setUp(self) -> None:
        self.rental = Rental.objects.create(name = 'room4')

        checkout_date = date.today() + timedelta(days=2)
        self.now =  date.today()
        self.reservation = Reservation.objects.create(
            rental_id = self.rental,checkin = self.now, 
            checkout = checkout_date
        )

        return super().setUp()

    def test_previous_reservation(self):
        checkout_date = date.today() + timedelta(days=5)
        checkout2_date = date.today() + timedelta(days=21)
        checkout3_date = date.today() + timedelta(days=20)
        checkin_date = date.today() + timedelta(days=10)
        checkin_date2 = date.today() + timedelta(days=5)

        previous_reservation_id = Reservation.objects.create(rental_id = self.rental,checkin = self.now, checkout = checkout_date)

        Reservation.objects.create(rental_id = self.rental,checkin = checkin_date, checkout = checkout3_date)
        Reservation.objects.create(rental_id = self.rental,checkin = checkin_date2, checkout = checkout2_date)

        self.assertEquals( self.reservation.previous_reservation,previous_reservation_id)


