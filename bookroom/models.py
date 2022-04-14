from django.db import models

# Create your models here.



class Rental(models.Model):
    name = models.CharField(("rental name"), max_length=50)
    def __str__(self):
        return self.name
class Reservation(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE, null=True)
    checkin = models.DateField(auto_now=False, auto_now_add=False)
    checkout = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.checkin)

    def previous_reservation(self):
        return Reservation.objects.filter(rental_id = self.rental_id,checkin__lt = self.checkin).values_list('checkin', flat=True).latest('checkin')
