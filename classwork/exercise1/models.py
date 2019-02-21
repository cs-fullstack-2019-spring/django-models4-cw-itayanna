from django.db import models

# Create your models here.


#moms class

class Mom(models.Model):
    mom_first_name = models.CharField(max_length=100)
    mom_last_name = models.CharField(max_length=100)
    mom_phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.mom_first_name} {self.mom_last_name}'

#child class

class Child(models.Model):
    chid_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_mom = models.ForeignKey(Mom,  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.chid_first_name} {self.child_last_name}'