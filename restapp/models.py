from django.db import models

class Results(models.Model):
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    prediction = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='results',on_delete=models.CASCADE)

    def __str__(self):
        return self.prediction
