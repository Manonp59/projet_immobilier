from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

class User(AbstractUser):
    pass

class Estimation(models.Model):
    
    zip_choices = (   (98178, '98178'),
        (98125, '98125'),
        (98028, '98028'),
        (98136, '98136'),
        (98074, '98074'),
        (98053, '98053'),
        (98003, '98003'),
        (98198, '98198'),
        (98146, '98146'),
        (98038, '98038'),
        (98007, '98007'),
        (98115, '98115'),
        (98107, '98107'),
        (98126, '98126'),
        (98019, '98019'),
        (98103, '98103'),
        (98002, '98002'),
        (98133, '98133'),
        (98040, '98040'),
        (98092, '98092'),
        (98030, '98030'),
        (98119, '98119'),
        (98112, '98112'),
        (98052, '98052'),
        (98027, '98027'),
        (98117, '98117'),
        (98058, '98058'),
        (98001, '98001'),
        (98056, '98056'),
        (98166, '98166'),
        (98023, '98023'),
        (98070, '98070'),
        (98148, '98148'),
        (98105, '98105'),
        (98042, '98042'),
        (98008, '98008'),
        (98059, '98059'),
        (98122, '98122'),
        (98144, '98144'),
        (98004, '98004'),
        (98005, '98005'),
        (98034, '98034'),
        (98075, '98075'),
        (98116, '98116'),
        (98010, '98010'),
        (98118, '98118'),
        (98199, '98199'),
        (98032, '98032'),
        (98045, '98045'),
        (98102, '98102'),
        (98077, '98077'),
        (98108, '98108'),
        (98168, '98168'),
        (98177, '98177'),
        (98065, '98065'),
        (98029, '98029'),
        (98006, '98006'),
        (98109, '98109'),
        (98022, '98022'),
        (98033, '98033'),
        (98155, '98155'),
        (98024, '98024'),
        (98011, '98011'),
        (98031, '98031'),
        (98106, '98106'),
        (98072, '98072'),
        (98188, '98188'),
        (98014, '98014'),
        (98055, '98055'),
        (98039, '98039'),)
    
    waterfront_choices = ( (1,'oui'), (0,'non'))
    
    titre = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now())
    m2_living = models.FloatField()
    m2_lot = models.FloatField()
    m2_above = models.FloatField()
    m2_basement = models.FloatField()
    bedrooms = models.FloatField()
    bathrooms = models.FloatField()
    floors = models.FloatField()
    zipcode = models.IntegerField(choices=zip_choices)
    grade = models.IntegerField()
    view = models.IntegerField()
    waterfront = models.IntegerField(choices=waterfront_choices)
    condition = models.IntegerField()
    yr_renovated = models.IntegerField()
    yr_built = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    predicted_price = models.FloatField(null=True)
    

