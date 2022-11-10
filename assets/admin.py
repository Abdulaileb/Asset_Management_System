from django.contrib import admin
from .models import (
    Assets,
    Asset_Type,
    Asset_State,
    Location,
    Department,
    Vendor,
    Employees
    )
# Register your models here.

admin.site.register(Assets),
admin.site.register(Asset_Type),
admin.site.register(Asset_State),
admin.site.register(Location),
admin.site.register(Department),
admin.site.register(Vendor),
admin.site.register(Employees)
