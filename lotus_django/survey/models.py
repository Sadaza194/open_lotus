from django.db import models
from django.contrib.auth.models import User  # Import the User model from Django



from django.db import models

class Frage(models.Model):
    text = models.TextField()
    typ = models.CharField(max_length=20, choices=[('likert', 'Likert-Skala'), ('kurztext', 'Kurztext')])
    frequenz = models.CharField(max_length=20, choices=[('taegllich', 'Täglich'), ('woechentlich', 'Wöchentlich'), ('monatlich', 'Monatlich')])

class Antwort(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference the correct User model
    zeitpunkt = models.DateTimeField(auto_now_add=True)
    wert = models.IntegerField(null=True, blank=True) # Für Likert-Skala
    text = models.TextField(null=True, blank=True) # Für Kurztext
