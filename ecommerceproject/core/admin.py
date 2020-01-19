from django.contrib import admin
from .models import *
# Register your models here.
class item_admin(admin.ModelAdmin):
    list_display=['title','slug','catageroy','label','sale_type','price','discount_price']
    prepopulated_fields={'slug':('title',)}
admin.site.register(item,item_admin)
admin.site.register(orderitem)
# admin.site.register(order)
# admin.site.register(orderitem)
