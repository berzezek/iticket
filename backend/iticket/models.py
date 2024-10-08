from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    place = models.CharField(max_length=255)
    tickets_amount = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="events")

    def __str__(self):
        return self.title


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number = models.IntegerField()
    ticket_type = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.event.title} - {self.number}"


class Order(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    date = models.DateTimeField()
    status = models.CharField(max_length=255)
    total = models.FloatField()

    def __str__(self):
        return f"{self.number} - {self.user}"
