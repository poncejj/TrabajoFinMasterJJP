from django.db import models
from datetime import date
from .choices import *
from .forms import *
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "States"

class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "Cities"

class Configuration(models.Model):
    extra_hour_rate = models.FloatField(default = 0)
    weekend_hour_rate = models.FloatField(default = 0)
    duration_driving_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 2, 00, 00))
    duration_break_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 00, 15, 00))
    duration_load_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 00, 15, 00))
    max_population = models.IntegerField(default = 0)
    max_iterations = models.IntegerField(default = 0)
    
    class Meta:
        verbose_name_plural = "Configurations"

class FuelType(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default = 0)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "FuelTypes"

class VehicleType(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default = 1000)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, default = None)
    max_work_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 18, 00, 00))
    max_speed_limit = models.IntegerField(default = 0)
    km_per_galon = models.FloatField(default = 0)
    perishable = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "VehicleTypes"

class DriverLicense(models.Model):
    name = models.CharField(max_length=2)
    vehicle_type = models.ManyToManyField(VehicleType)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "DriverLicenses"

class Driver(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,)
    driver_license = models.ForeignKey(DriverLicense, null=True, on_delete = models.CASCADE)
    driver_hour_cost = models.FloatField(default = 15)
    max_work_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 8, 00, 00))
    max_work_extra_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 4, 00, 00))

    def __str__(self):
        return str(self.name) + " " + str(self.last_name)
    class Meta:
        verbose_name_plural = "Drivers"

class FamilyItem(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "FamiliyItems"

class HolidayType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "HolidayTypes"

class HolidayLocale(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "HolidaysLocals"

class HolidayEvent(models.Model):
    date = MyDateField(default=now)
    holiday_type = models.ForeignKey(HolidayType, on_delete=models.CASCADE)
    locale = models.ForeignKey(HolidayLocale, on_delete=models.CASCADE) 
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    transferred = models.BooleanField()

    def __str__(self):
        return str(self.description) + ' (' + str(self.date) + ')'
    class Meta:
        verbose_name_plural = "HolidaysEvents"


class Item(models.Model):
    item_nbr = models.IntegerField(default = 0, unique=True)
    family = models.ForeignKey(FamilyItem, on_delete=models.CASCADE)
    class_item = models.IntegerField(default = 0)   
    perishable = models.BooleanField()
    available_quantity = models.IntegerField(default = 0)
    
    def __str__(self):
        return str(self.item_nbr) + ' - ' + str(self.family.name)
    class Meta:
        verbose_name_plural = "Items"
class Log(models.Model):
    route_date = MyDateField(default=now)
    population_size = models.IntegerField(default=10, null=True, blank=True, validators=[MinValueValidator(2),MaxValueValidator(100)])
    number_iterations = models.IntegerField(default=10, null=True, blank=True, validators=[MinValueValidator(2),MaxValueValidator(100)])
    mutation_rate = MinMaxDecimal(default = 0.5, max_digits=18, decimal_places=2, min_value=0, max_value=1)
    crossing_rate = MinMaxDecimal(default = 0.5, max_digits=18, decimal_places=2, min_value=0, max_value=1)
    failed_attempts_stop = models.IntegerField(default=5, null=True, blank=True, validators=[MinValueValidator(1),MaxValueValidator(10)])
    distance_weight = MinMaxDecimal(default = 0.2, max_digits=18, decimal_places=2, min_value=0, max_value=1)
    num_trucks_weight = MinMaxDecimal(default = 0.2, max_digits=18, decimal_places=2, min_value = 0, max_value=1)
    staff_cost_weight = MinMaxDecimal(default = 0.2, max_digits=18, decimal_places=2, min_value = 0, max_value=1)
    fuel_cost_weight = MinMaxDecimal(default = 0.2, max_digits=18, decimal_places=2, min_value = 0, max_value=1)
    delivery_time_weight = MinMaxDecimal(default = 0.2, max_digits=18, decimal_places=2, min_value = 0, max_value=1)
    #Results
    distance_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    num_trucks_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    staff_cost_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    fuel_cost_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    delivery_time_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    fitness_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    min_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    max_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    mean_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    median_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    variance_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    std_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    errors = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)
    total_time = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.route_date)+ " " + str(self.population_size)+ " " + str(self.number_iterations)+ " " + str(self.mutation_rate)+ " " + str(self.crossing_rate)+ " " + str(self.failed_attempts_stop)+ " " + str(self.distance_weight)+ " " + str(self.num_trucks_weight)+ " " + str(self.staff_cost_weight)+ " " + str(self.fuel_cost_weight)+ " " + str(self.delivery_time_weight)
        
class MetaLog(models.Model):
    route_date = MyDateField(default=now)
    population_size = models.IntegerField(default=10, null=True, blank=True, validators=[MinValueValidator(2),MaxValueValidator(100)])
    number_iterations = models.IntegerField(default=10, null=True, blank=True, validators=[MinValueValidator(2),MaxValueValidator(100)])
    mutation_rate = MinMaxDecimal(default = 0.5, max_digits=18, decimal_places=2, min_value=0, max_value=1)
    crossing_rate = MinMaxDecimal(default = 0.5, max_digits=18, decimal_places=2, min_value=0, max_value=1)
    failed_attempts_stop = models.IntegerField(default=5, null=True, blank=True, validators=[MinValueValidator(1),MaxValueValidator(10)])
    #Results
    best_fitness = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    min_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    max_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    mean_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    median_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    variance_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    std_result = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    errors = models.TextField(null=True, blank=True)
    total_time = models.DecimalField(default = 0, max_digits = 18, decimal_places = 2)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Oil(models.Model):
    date = MyDateField(default=now)
    dcoilwtico = models.FloatField(default = 0)

    def __str__(self):
        return str(self.date) + ' - ' + str(self.dcoilwtico)
    class Meta:
        verbose_name_plural = "Oils"

class StoreType(models.Model):
    letter = models.CharField(max_length=1)

    def __str__(self):
        return str(self.letter)
    class Meta:
        verbose_name_plural = "StoreTypes"

class Store(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    store_type = models.ForeignKey(StoreType, on_delete=models.CASCADE)
    cluster = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    open_hour = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 6, 00, 00))
    close_hour = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime(1994, 1, 31, 22, 00, 00))

    def __str__(self):
        return str(self.city.name) + ' ' + str(self.location)
    class Meta:
        verbose_name_plural = "Stores"

class Transaction(models.Model):
    date = MyDateField(default=now)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    transactions = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = "Transactions"
    @property
    def date_year(self):
        return self.date.strftime('%Y')

class Sale(models.Model):
    date = MyDateField(default=now)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, to_field = 'item_nbr', on_delete=models.CASCADE)
    unit_sales = models.IntegerField(default = 0)
    onpromotion = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "Sales"

class Vehicle(models.Model):
    registration = models.CharField(max_length=200)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.registration)
    class Meta:
        verbose_name_plural = "Vehicles"