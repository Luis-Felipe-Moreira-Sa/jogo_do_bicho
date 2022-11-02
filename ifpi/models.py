from django.db import models

# Create your models here.
class Result(models.Model):
    last_result = models.CharField(max_length=80, null=True)
    last_date_update = models.CharField(max_length=80, null=True)

    def last_date(self):
        return self.last_date_update

    def __str__(self):
        return self.last_result
        #, self.last_date_update


class Bets(models.Model):
    bet = models.CharField(max_length=40, null=True)
    name_user = models.CharField(max_length=40, null=True)
    concurso_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.bet
