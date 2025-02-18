from django.contrib import admin
from .models import User  # Apne custom User model ko import karein

# Custom admin class to manage User model
class UserAdmin(admin.ModelAdmin):
    # Jo fields admin panel mein dikhana chahte hain
    list_display = ['email', 'is_active', 'is_staff']  # Aap aur fields add kar sakte hain
    search_fields = ['email']  # Search karne ke liye email field ko add kiya
    ordering = ['email']  # Records ko order karne ke liye email field

# Register the User model with custom admin class
admin.site.register(User, UserAdmin)
