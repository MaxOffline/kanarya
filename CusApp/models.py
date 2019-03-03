from django.db import models
from django.contrib.auth.models import User



class newcustomer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, unique = True, null = True)
    Customer_Name = models.CharField(max_length = 20)
    Clothes_Price = models.IntegerField()
    Clothes_Kilos = models.IntegerField()
    added = models.BooleanField(default=False)



    def total(self):
        return(self.Clothes_Price*self.Clothes_Kilos)

    def __str__(self):
        return(str(self.user))

    class Meta:
        permissions=(("can_view", "can view views "),)




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return(str(self.id))





class Item(models.Model):
    cart = models.CharField(max_length = 1000)
    itemuser = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    url = models.CharField(max_length = 12)
    color = models.CharField(max_length = 12)
    weight = models.CharField(max_length = 12)
    submitted = models.BooleanField(default=False)
    def __str__(self):
        return(str(self.cart))
