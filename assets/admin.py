from django.contrib import admin
from assets.models import (
    Assets,
    Asset_Type,
    Departments,
    Vendor,
    Employee,
    )


admin.site.register(Assets),
admin.site.register(Asset_Type),
admin.site.register(Departments),
admin.site.register(Vendor),
admin.site.register(Employee),
