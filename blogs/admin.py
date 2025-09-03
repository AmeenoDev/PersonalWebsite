from django.contrib import admin
from .models import Product , Test  # Import the Test model if it exists
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'price','active','category']
    list_display_links = ['name','price']
    list_editable =['category','active']
    search_fields=['name']
    list_filter=['category']
    fields = ['name','category']
admin.site.register(Product,ProductAdmin)
admin.site.register(Test)  # Assuming Test is a model you want to register as well
admin.site.site_header = 'Amin panel'
admin.site.site_title = 'Amin'