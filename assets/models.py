from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Assets(models.Model):
    Name = models.CharField(max_length= 50)
    Type = models.ForeignKey(
        "Asset_Type", 
        on_delete=models.CASCADE
    )
    Quantity = models.IntegerField()
    Model = models.TextField()
    Serian_Num = models.CharField(max_length= 100, null=True, blank=True)
    Department = models.ForeignKey(
        "Department", 
        on_delete=models.CASCADE)
    State = models.ForeignKey(
        "Asset_State", 
        on_delete=models.CASCADE)
    Date_Acquired = models.DateField()
    Location = models.ForeignKey(
        "Location", 
        on_delete=models.CASCADE)
    Vendor = models.ForeignKey(
        "Vendor", 
        on_delete=models.CASCADE)
    Employee = models.ForeignKey(
        "Employees", 
        on_delete=models.CASCADE)
    Description = models.TextField()

    class meta:
        verbose_name_plural = "Assets Information"
        ordering = ['Name', 'Type', 'Date_Acquired', 'Vendor']
        get_latest_by = "Date_Acquired"
    def __str__(self):
        return self.Name

class Asset_Type(models.Model):
    type = models.CharField(max_length= 50)

    def __str__(self):
        return self.type

ASSETS_CHOICES = (
    ('New','New'),
    ('Like New','Used_Like New'),
    ('Good','Used_Good'),
    ('Fair','Used_Fair'),
    ('Damaged','Damaged')
)

class Asset_State(models.Model):
    State = models.CharField(max_length=15, choices=ASSETS_CHOICES, default='N')

    def __str__(self):
        return self.State

class Location(models.Model):
    Location = models.TextField()

    def __str__(self):
        return self.Location

class Department(models.Model):
    Dept_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Dept_Name

VENDOR_CHOICES = (
    ('Manufacturer','Manufacturer'),
    ('wholesaler','Wholesaler'),
    ('retailers','Retailer'),
    ('service and maintenance providers','Service and maintenance providers'),
    ('independent vendors','Independent vendors')
)

class Vendor(models.Model):
    Company_Name = models.CharField(max_length=50, blank=False, null=False, default='CYPA')
    Name = models.CharField(max_length=100)
    Business = models.CharField(max_length=40, choices=VENDOR_CHOICES, default='Manufacturer')
    Address = models.TextField()
    City = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Website = models.URLField(max_length=250, blank=True, null=True)
    Country = CountryField(blank_label='(select country)')

    def __str__(self):
        return f"{self.Company_Name}, {self.Name}"

EMPLOYEE_CHOICES = (
    ('Active','Active'),
    ('Inactive','Inactive')
)

class Employees(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=40)
    Title = models.TextField()
    Department = models.ForeignKey(
        "Department", 
        on_delete=models.CASCADE) 
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Status = models.CharField(max_length=10, default='Active')

    def __str__(self):
        return f"{self.First_Name}, {self.Last_Name}"
