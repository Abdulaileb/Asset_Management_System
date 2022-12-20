from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Departments(models.Model):
    Dept = (
    ('Academic','Academic'),
    ('Administration','Administration'),
    )
    Name = models.CharField(max_length=100, choices=Dept, null=True,)

    def __str__(self):
        return self.Name

#class DepreciationRate(models.Model):
    #Depre_Rate = models.PositiveBigIntegerField(null=True, default='2%')

   # def __repr__(self):
    #    return self.Depre_Rate

#class DepreciationType(models.Model):
 #   Depre_Type = models.CharField(max_length=100, null=True, default='Straight-Line Method')

  #  def __str__(self):
   #     return self.Depre_Type

class Assign(models.Model):
    Assign_group = (
    ('Faculty','Faculty'),
    ('Department','Department'),
    ('Employee','Employee'),
    )
    Name = models.CharField(max_length=100, choices=Assign_group,)

    def __str__(self):
        return self.Name

class Vendor(models.Model):
    VENDOR_CHOICES = (
    ('Manufacturer','Manufacturer'),
    ('wholesaler','Wholesaler'),
    ('retailers','Retailer'),
    ('service and maintenance providers','Service and maintenance providers'),
    ('independent vendors','Independent vendors')
    )
    Company_Name = models.CharField(max_length=50, blank=False, default='CYPA')
    Name = models.CharField(max_length=100)
    Business = models.CharField(max_length=40, choices=VENDOR_CHOICES, default='Manufacturer')
    Address = models.TextField(max_length=250)
    City = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Website = models.URLField(max_length=250, blank=True, null=True)
    Country = CountryField(blank_label='(select country)')

    def __str__(self):
        return self.Company_Name


class Employee(models.Model):
    Full_Name = models.CharField(max_length=50)
    Title = models.TextField()
    Departments = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL) 
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.Full_Name


class Assets(models.Model):
    A_CHOICES = (
    ('New','New'),
    ('Good','Good'),
    ('Used','Used'),
    ('Defective','Defective')
    )
    Name = models.CharField(max_length= 50)
    Type = models.ForeignKey("Asset_Type", on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Model = models.TextField(max_length=200, null=True,)
    Serian_Num = models.CharField(max_length= 100, null=True, blank=True)
    Asset_State = models.CharField(max_length=15, choices=A_CHOICES, default='New')
    LifeSpan = models.CharField(max_length=50, null=True, default='10Yrs')
    Date_Acquired = models.DateField()
    Warantee_Start_Date = models.DateField()
    Warantee_Start_Date = models.DateField()
    Assign_to = models.ForeignKey("Assign", on_delete=models.CASCADE)
    Date_Assigned = models.DateField()
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Asset_Type(models.Model):
    type = models.CharField(max_length= 50)

    def __str__(self):
        return self.type






