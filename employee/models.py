from django.db import models

class Location(models.Model) : 
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Department(models.Model) : 
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Employee(models.Model) : 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=100)
    salary = models.FloatField()
    expn = models.PositiveSmallIntegerField()
    d_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    # photo = models.TextField(max_length=255, blank=True, null=True)

class Contact(models.Model) : 
    number = models.PositiveBigIntegerField()
    address = models.CharField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)