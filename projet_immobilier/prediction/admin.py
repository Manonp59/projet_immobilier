from django.contrib import admin
from prediction.models import User, Estimation
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    
class EstimationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'predicted_price')
    
admin.site.register(Estimation, EstimationAdmin)
admin.site.register(User,UserAdmin)