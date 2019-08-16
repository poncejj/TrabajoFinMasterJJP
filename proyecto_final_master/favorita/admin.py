from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Store)
admin.site.register(models.City)
admin.site.register(models.StoreType)
admin.site.register(models.State)
admin.site.register(models.HolidayType)
admin.site.register(models.HolidayLocale)
admin.site.register(models.HolidayEvent)
admin.site.register(models.FamilyItem)
admin.site.register(models.Item)
admin.site.register(models.Oil)
admin.site.register(models.DriverLicense)
admin.site.register(models.Transaction)
admin.site.register(models.Sale)
admin.site.register(models.VehicleType)
admin.site.register(models.Vehicle)
admin.site.register(models.Driver)
admin.site.register(models.Log)