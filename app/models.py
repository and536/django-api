from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField('date published')

class Exame(models.Model):
    name_professional = models.CharField(max_length=200)
    date_exam = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date published')