from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import * 

#ModelsForms
class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class TransactionFormSet(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class OilForm(ModelForm):
    class Meta:
        model = Oil
        fields = '__all__'
            

class CityFormSet(ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class StateFormSet(ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class FamilyItemFormSet(ModelForm):
    class Meta:
        model = FamilyItem
        fields = ['name']

class HolidayEventFormSet(ModelForm):
    class Meta:
        model = HolidayEvent
        fields = '__all__'

class HolidayLocaleFormSet(ModelForm):
    class Meta:
        model = HolidayLocale
        fields = '__all__'

class HolidayTypeFormSet(ModelForm):
    class Meta:
        model = HolidayType
        fields = '__all__'

class VehicleTypeForm(ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'
        
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

class MetaLog(object):
    class Meta:
        model = MetaLog
        fields = '__all__'

class FuelTypeForm(ModelForm):
    class Meta:
        model = FuelType
        fields = '__all__'

class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        fields = '__all__'

class DriverLicenseForm(ModelForm):
    class Meta:
        model = DriverLicense
        fields = '__all__'
        