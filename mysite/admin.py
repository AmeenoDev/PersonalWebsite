from django.contrib import admin
from .models import Login
from .models import Female_Group, Male_Group, Product, UserName, Video  # Import the Test model if it exists
admin.site.register(Male_Group)
admin.site.register(Female_Group)
admin.site.register(Product)
admin.site.register(UserName)
admin.site.register(Video)

admin.site.register(Login)