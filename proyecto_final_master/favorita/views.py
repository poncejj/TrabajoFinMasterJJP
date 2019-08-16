import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest
from django.forms import modelformset_factory, formset_factory
from django.db.models import Sum
from datetime import datetime
from .models import *
from .models_forms import *
from django.db.models.functions import ExtractMonth
from .algorithms.genethic_algorithm import *
from .algorithms.meta_algorithm import *
from .common.json_converter import *
from .forms import *
import time
from django.urls import reverse
from django.conf import settings

# Create your views here.
def index(request):
  if settings.CHART is not None:
    values_json = settings.CHART.to_json(orient='values')
  else:
    settings.CHART = pd.read_csv(os.path.join(settings.LOCAL_BDD, "chart2019.csv"))
    values_json = settings.CHART.to_json(orient='values')
  context = {
  'values':values_json,
  }
  return render(request, 'favorita/index.html',context)

def stores(request):
  stores = Store.objects.all()
  context = {
  'title' : 'Stores',
  'generic_objects' : stores
  }
  return render(request, 'store/index.html',context)

def store(request, id):
  StoreFormSet = modelformset_factory(Store, exclude=(), extra=0)
  if request.method == 'POST':
    formset = StoreFormSet(request.POST, request.FILES)
    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect('/favorita/stores')
  else:
    stores_search = Store.objects.filter(id = id)
    if stores_search:
        formset = StoreFormSet(queryset=stores_search)
    else:
        formset = formset_factory(StoreForm)
    return render(request, 'store/details.html', {'formset': formset, 'id':id, 'title':"Store"})

def delete_store(request, id):
  Store.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/stores')

def items(request):
  items = Item.objects.all()
  context = {
  'title' : 'Items',
  'generic_objects' : items
  }
  return render(request, 'item/index.html',context)

def item(request, id):
  ItemFormSet = modelformset_factory(Item, exclude=(), extra=0)
  if request.method == 'POST':
    formset = ItemFormSet(request.POST, request.FILES)
    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect('/favorita/items')
  else:
    items_search = Item.objects.filter(id = id)
    if items_search:
        formset = ItemFormSet(queryset=items_search)
    else:
        formset = formset_factory(ItemForm)
    return render(request, 'item/details.html', {'formset': formset, 'id':id, 'title':"Item"})

def delete_item(request, id):
  Item .objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/items')

def transactions(request):
  transactions = Transaction.objects.all()
  context = {
  'title' : 'Transaction',
  'generic_objects' : transactions
  }
  return render(request, 'transaction/index.html',context)

def transaction(request, id):
  TransactionFormSet = modelformset_factory(Transaction, exclude=(), extra=0)
  if request.method == 'POST':
    formset = TransactionFormSet(request.POST, request.FILES)
    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect('/favorita/transactions')
  else:
    transactions_search = Transaction.objects.filter(id = id)
    if transactions_search:
        formset = TransactionFormSet(queryset=transactions_search)
    else:
        formset = formset_factory(TransactionFormSet)
    return render(request, 'transaction/details.html', {'formset': formset, 'id':id, 'title':"Transaction"})

def delete_transaction(request, id):
  Transaction.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/transactions')

def resources(request):
   resources = Truck.objects.all()
   context = {
   'title' : 'Resources',
   'generic_objects' : resources
   }
   return render(request, 'resource/index.html',context)

def resource(request, id):
  TruckFormSet = modelformset_factory(Truck, exclude=(), extra=0)
  if request.method == 'POST':
    formset = TruckFormSet(request.POST, request.FILES)
    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect('/favorita/resources')
  else:
    trucks_search = Truck.objects.filter(id = id)
    if trucks_search:
        formset = TruckFormSet(queryset=trucks_search)
    else:
        formset = formset_factory(TruckFormSet)
    return render(request, 'resource/details.html', {'formset': formset, 'id':id, 'title':"Resources"})

def delete_resource(request, id):
  Truck.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/resources')


def oils(request):
  oils_prices = Oil.objects.all()
  context = {
  'title' : 'Oil Prices',
  'generic_objects' : oils_prices
  }
  return render(request, 'oil/index.html',context)

def oil(request, id=0):
  OilFormSet = modelformset_factory(Oil, fields='__all__')
  if request.method == 'POST':
    formset = OilFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/oils')
        # do something.
  else:
    if int(id) > 0:
      OilFormSet = modelformset_factory(Oil, fields='__all__', extra=0)
      formset = OilFormSet(queryset = Oil.objects.filter(id = id))
    else:
      formset = OilFormSet(queryset=Oil.objects.none())
  return render(request, 'oil/details.html', {'formset': formset, 'id':id,'title':"Oil"})


def delete_oil(request, id):
  Oil.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/oils')

def cities(request):
  cities_search = City.objects.all()
  context = {
  'title' : 'Cities',
  'generic_objects' : cities_search
  }
  return render(request, 'city/index.html',context)

def city(request, id=0):
  CityFormSet = modelformset_factory(City, fields='__all__')
  if request.method == 'POST':
    formset = CityFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/cities')
        # do something.
  else:
    if int(id) > 0:
      CityFormSet = modelformset_factory(City, fields='__all__', extra=0)
      formset = CityFormSet(queryset = City.objects.filter(id = id))
    else:
      formset = CityFormSet(queryset=City.objects.none())
  return render(request, 'city/details.html', {'formset': formset, 'id':id, 'title':"City"})

def delete_city(request, id):
  City.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/cities')

def states(request):
  states_search = State.objects.all()
  context = {
  'title' : 'States',
  'generic_objects' : states_search
  }
  return render(request, 'state/index.html',context)

def state(request, id=0):
  StateFormSet = modelformset_factory(State, fields='__all__')
  if request.method == 'POST':
    formset = StateFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/states')
        # do something.
  else:
    if int(id) > 0:
      StateFormSet = modelformset_factory(State, fields='__all__', extra=0)
      formset = StateFormSet(queryset = State.objects.filter(id = id))
    else:
      formset = StateFormSet(queryset=State.objects.none())
  return render(request, 'state/details.html', {'formset': formset, 'id':id, 'title':"States"})


def delete_state(request, id):
  State.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/states')

def families(request):
  families_search = FamilyItem.objects.all()
  context = {
  'title' : 'Families',
  'generic_objects' : families_search
  }
  return render(request, 'family/index.html',context)

def family(request, id):
  FamilyFormSet = modelformset_factory(FamilyItem, exclude=(), extra=0)
  if request.method == 'POST':
    formset = FamilyFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/families')
  else:
    family_search = FamilyItem.objects.filter(id = id)
    if family_search:
      formset = FamilyFormSet(queryset=family_search)
    else:
      formset = formset_factory(FamilyItemFormSet)
    return render(request, 'family/details.html', {'formset': formset, 'id':id, 'title':"Family"})

def delete_family(request, id):
  FamilyItem.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/families')

def holidays(request):
  holidays_search = HolidayEvent.objects.all()
  context = {
  'title' : 'Holidays',
  'generic_objects' : holidays_search
  }
  return render(request, 'holiday/index.html',context)

def holiday(request, id):
  HolidateLocaleFormSet = modelformset_factory(HolidayEvent, exclude=(), extra=0)
  if request.method == 'POST':
    formset = HolidateLocaleFormSet(request.POST, request.FILES)
    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect('/favorita/holidays')
  else:
    holiday_search = HolidayEvent.objects.filter(id = id)
    if holiday_search:
      formset = HolidateLocaleFormSet(queryset=holiday_search)
    else:
      formset = formset_factory(HolidayEventFormSet)
    return render(request, 'holiday/details.html', {'formset': formset, 'id':id, 'title':"Holiday"})

def delete_holiday(request, id):
  HolidayEvent.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/holidays')

def holidaysLocales(request):
  holidayLocales_search = HolidayLocale.objects.all()
  context = {
  'title' : 'Holidays Locales',
  'generic_objects' : holidayLocales_search
  }
  return render(request, 'holidayLocale/index.html',context)

def holidayLocale(request, id):
    HolidateLocaleFormSet = modelformset_factory(HolidayLocale, exclude=(), extra=0)
    if request.method == 'POST':
        formset = HolidateLocaleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/favorita/holidaysLocales')
    else:
        holidayLocale_search = HolidayLocale.objects.filter(id = id)
        if holidayLocale_search:
            formset = HolidateLocaleFormSet(queryset=holidayLocale_search)
        else:
            formset = formset_factory(HolidayLocaleFormSet)
        return render(request, 'holidayLocale/details.html', {'formset': formset, 'id':id, 'title':"Holiday Locale"})

def delete_holidayLocale(request, id):
    HolidayLocale.objects.filter(id=id).delete()
    return HttpResponseRedirect('/favorita/holidaysLocales')

def holidaysTypes(request):
   holidayTypes_search = HolidayType.objects.all()
   context = {
   'title' : 'Holidays Types',
   'generic_objects' : holidayTypes_search
   }
   return render(request, 'holidayType/index.html',context)

def holidayType(request, id):
  HolidateTypeFormSet = modelformset_factory(HolidayType, exclude=(), extra=0)
  if request.method == 'POST':
    formset = HolidateTypeFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/holidaysTypes')
  else:
    holidayType_search = HolidayType.objects.filter(id = id)
    if holidayType_search:
      formset = HolidateTypeFormSet(queryset=holidayType_search)
    else:
      formset = formset_factory(HolidayTypeFormSet)
    return render(request, 'holidayType/details.html', {'formset': formset, 'id':id, 'title':"Holiday Locale"})

def delete_holidayType(request, id):
  HolidayType.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/holidaysTypes')

######################## VEHICLE TYPE #########################################
def vehicleTypes(request):
  vehicleTypes = VehicleType.objects.all()
  context = {
  'title' : 'Vehicle Types',
  'generic_objects' : vehicleTypes
  }
  return render(request, 'vehicleType/index.html',context)

def vehicleType(request, id=0):
  VehicleTypeFormSet = modelformset_factory(VehicleType, fields='__all__')
  if request.method == 'POST':
    formset = VehicleTypeFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/vehicleTypes')
        # do something.
  else:
    if int(id) > 0:
      VehicleTypeFormSet = modelformset_factory(VehicleType, fields='__all__', extra=0)
      formset = VehicleTypeFormSet(queryset = VehicleType.objects.filter(id = id))
    else:
      formset = VehicleTypeFormSet(queryset=VehicleType.objects.none())
  return render(request, 'vehicleType/details.html', {'formset': formset, 'id':id, 'title':"Vehicle Type"})

def delete_vehicle(request, id):
  Vehicle.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/vehicles')

def delete_vehicleType(request, id):
  VehicleType.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/vehicleTypes')

############################### VEHICLE #########################################
def vehicles(request):
  vehicles_search = Vehicle.objects.all()
  context = {
  'title' : 'Vehicles',
  'generic_objects' : vehicles_search
  }
  return render(request, 'vehicle/index.html',context)

def vehicle(request, id=0):
  VehicleFormSet = modelformset_factory(Vehicle, fields='__all__')
  if request.method == 'POST':
    formset = VehicleFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/vehicles')
        # do something.
  else:
    if int(id) > 0:
      VehicleFormSet = modelformset_factory(Vehicle, fields='__all__', extra=0)
      formset = VehicleFormSet(queryset = Vehicle.objects.filter(id = id))
    else:
      formset = VehicleFormSet(queryset=Vehicle.objects.none())
  return render(request, 'vehicle/details.html', {'formset': formset, 'id':id, 'title':"Vehicle"})

def delete_vehicle(request, id):
  Vehicle.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/vehicles')

############################### DRIVER #########################################
def drivers(request):
  drivers_search = Driver.objects.all()
  context = {
  'title' : 'Drivers',
  'generic_objects' : drivers_search
  }
  return render(request, 'driver/index.html',context)

def driver(request, id=0):
  DriverFormSet = modelformset_factory(Driver, fields='__all__')
  if request.method == 'POST':
    formset = DriverFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/drivers')
        # do something.
  else:
    if int(id) > 0:
      DriverFormSet = modelformset_factory(Driver, fields='__all__', extra=0)
      formset = DriverFormSet(queryset = Driver.objects.filter(id = id))
    else:
      formset = DriverFormSet(queryset=Driver.objects.none())
  return render(request, 'driver/details.html', {'formset': formset, 'id':id, 'title':"Driver"})

def delete_driver(request, id):
  Driver.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/drivers')


############################### FUEL TYPE #########################################
def fuelTypes(request):
  fuelTypes_search = FuelType.objects.all()
  context = {
  'title' : 'Fuel Types',
  'generic_objects' : fuelTypes_search
  }
  return render(request, 'fuelType/index.html',context)

def fuelType(request, id=0):
  FuelTypeFormSet = modelformset_factory(FuelType, fields='__all__')
  if request.method == 'POST':
    formset = FuelTypeFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/fuelTypes')
        # do something.
  else:
    if int(id) > 0:
      FuelTypeFormSet = modelformset_factory(FuelType, fields='__all__', extra=0)
      formset = FuelTypeFormSet(queryset = FuelType.objects.filter(id = id))
    else:
      formset = FuelTypeFormSet(queryset=FuelType.objects.none())
  return render(request, 'fuelType/details.html', {'formset': formset, 'id':id, 'title':"Fuel Type"})

def delete_fuelType(request, id):
  FuelType.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/fuelTypes')

############################### LICENSE DRIVER ######################################
def driverLicenses(request):
  driverLicenses_search = DriverLicense.objects.all()
  context = {
  'title' : 'Driver Licences',
  'generic_objects' : driverLicenses_search
  }
  return render(request, 'driverLicense/index.html',context)

def driverLicense(request, id=0):
  DriverLicenseFormSet = modelformset_factory(DriverLicense, fields='__all__')
  if request.method == 'POST':
    formset = DriverLicenseFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/driverLicenses')
        # do something.
  else:
    if int(id) > 0:
      DriverLicenseFormSet = modelformset_factory(DriverLicense, fields='__all__', extra=0)
      formset = DriverLicenseFormSet(queryset = DriverLicense.objects.filter(id = id))
    else:
      formset = DriverLicenseFormSet(queryset=DriverLicense.objects.none())
  return render(request, 'driverLicense/details.html', {'formset': formset, 'id':id, 'title':"Driver License"})

def delete_driverLicense(request, id):
  DriverLicense.objects.filter(id=id).delete()
  return HttpResponseRedirect('/favorita/driverLicenses')


############################### CONFIGURATION #########################################
def configuration(request, id=1):
  ConfigurationFormSet = modelformset_factory(Configuration, fields='__all__', extra=0)
  if request.method == 'POST':
    formset = ConfigurationFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect('/favorita/configuration/'+ id + '/')
        # do something.
  else:
    formset = ConfigurationFormSet(queryset = Configuration.objects.filter(id = id))
    return render(request, 'configuration/index.html', {'formset': formset, 'id':id, 'title':"Configuration"})

def showLog(request):
  formset = modelformset_factory(Log, exclude=(), extra=1)
  headers = formset(queryset=Log.objects.none())
  body = modelformset_factory(Log, exclude=(), extra=0)
  
  context = {
  'title' : 'Evaluated Algorithms!',
  'headers': headers,
  'body': body,
  }
  return render(request, 'evaluate/results.html',context)

def showMetaLog(request):
  formset = modelformset_factory(MetaLog, exclude=(), extra=1)
  headers = formset(queryset=MetaLog.objects.none())
  body = modelformset_factory(MetaLog, exclude=(), extra=0)
  
  context = {
  'title' : 'Meta Evaluated Algorithms!',
  'headers': headers,
  'body': body,
  }
  return render(request, 'evaluate/meta_results.html',context)


def configRoute(request, id = 0):
  #Create the basic formset to show in the template only the fields user has to complete
  LogFormSet = modelformset_factory(Log, exclude=('selected', 'population_size', 'number_iterations', 'mutation_rate', 'crossing_rate', 'failed_attempts_stop', 'total_time', 'distance_result', 'num_trucks_result', 'staff_cost_result', 'fuel_cost_result', 'delivery_time_result', 'fitness_result', 'errors', 'created_date'), extra=0)
  if int(id) > 0:
    formset = LogFormSet(queryset = Log.objects.filter(id = id))
  else:
    formset = LogFormSet(queryset = Log.objects.get(selected=True))

  context = {
    'title' : 'Config Route',
    'formset':formset
  }
  return render(request, 'routes/index.html',context)

def showMap(request):
    #When user send a petition we use the POST method
  LogFormSet = modelformset_factory(Log, exclude=('selected', 'population_size', 'number_iterations', 'mutation_rate', 'crossing_rate', 'failed_attempts_stop', 'total_time', 'distance_result', 'num_trucks_result', 'staff_cost_result', 'fuel_cost_result', 'delivery_time_result', 'fitness_result', 'errors', 'created_date'), extra=1)
  #LogFormSet = modelformset_factory(Log, exclude=(), extra=0)
  if request.method == 'POST':
    #Get all the data sended from the template and put them in an object to be evaluated
    #by the selected algorithm with the parameters that the user wants to evaluate
    formset = LogFormSet(request.POST, request.FILES)
    #Recive a complete formset with all the results
    if formset.is_valid():
      selected_log = Log.objects.get(selected=True)
      log_object = Log()
      log_object.population_size = selected_log.population_size
      log_object.number_iterations = selected_log.number_iterations
      log_object.crossing_rate = selected_log.crossing_rate
      log_object.mutation_rate = selected_log.mutation_rate
      log_object.failed_attempts_stop = selected_log.failed_attempts_stop
      log_object.route_date = formset.cleaned_data[0]['route_date']
      log_object.distance_rate = formset.cleaned_data[0]['distance_rate']
      log_object.num_trucks_rate = formset.cleaned_data[0]['num_trucks_rate']
      log_object.staff_cost_rate = formset.cleaned_data[0]['staff_cost_rate']
      log_object.fuel_cost_rate = formset.cleaned_data[0]['fuel_cost_rate']
      log_object.delivery_time_rate = formset.cleaned_data[0]['delivery_time_rate']
      has_solution, planification, log_object = runGenethicMultiobjective(log_object)
      log_object.save(force_insert=True)
      if has_solution:
        #request = HttpRequest()
        form = ShowRouteForm()
        choices = []
        coordinates = {}
        distances = {}
        drivers = {}
        items = {}
        
        for route in planification:
          choices.append((route.name, route))
          coordinates[str(route)] = getJsonCoordinates(route)
          distances[str(route)] = route.distance
          drivers[str(route)] = getJsonDrivers(route)
          items[str(route)] = getJsonItems(route)

        form.fields["routes"].choices = choices
        json_coordinates = json.dumps(coordinates)
        json_distances = json.dumps(distances)
        json_drivers = json.dumps(drivers)
        json_items = json.dumps(items)

        context = {
          'title' : 'Routes',
          'form':form,
          'planification': planification,
          'coordinates': json_coordinates,
          'distances': json_distances,
          'drivers': json_drivers,
          'items': json_items,
        }
        
        return render(request, 'routes/map.html',context)

def configEvaluation(request, id = 0):
  #Create the basic formset to show in the template only the fields user has to complete
  MetaLogFormSet = modelformset_factory(MetaLog, exclude=('total_time', 'best_fitness', 'errors', 'created_date'), extra=1)
  if int(id) > 0:
    formset = MetaLogFormSet(queryset = MetaLog.objects.filter(id = id))
  else:
    formset = MetaLogFormSet(queryset = MetaLog.objects.none())

  #When user send a petition we use the POST method
  if request.method == 'POST':
    #Get all the data sended from the template and put them in an object to be evaluated
    #by the selected algorithm with the parameters that the user wants to evaluate
    formset = MetaLogFormSet(request.POST, request.FILES)
    #Recive a complete formset with all the results
    
    if formset.is_valid():
      meta_log_object = MetaLog()
      meta_log_object.population_size = formset.cleaned_data[0]['population_size']
      meta_log_object.number_iterations = formset.cleaned_data[0]['number_iterations']
      meta_log_object.crossing_rate = formset.cleaned_data[0]['crossing_rate']
      meta_log_object.mutation_rate = formset.cleaned_data[0]['mutation_rate']
      meta_log_object.failed_attempts_stop = formset.cleaned_data[0]['failed_attempts_stop']
      meta_log_object = runMetaAlgorithm(meta_log_object)
      meta_log_object.save(force_insert=True)

  context = {
    'title' : 'Meta Parametrization algorithms',
    'formset':formset
  }
  return render(request, 'evaluate/index.html',context)

def selectEvaluation(request, id = 0):
  Log.objects.all().update(selected=False)
  Log.objects.filter(id=id).update(selected=True)

  return HttpResponseRedirect('/favorita/show_results')
