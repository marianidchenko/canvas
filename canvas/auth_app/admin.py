from django.contrib import admin

# Register your models here.
from canvas.auth_app.models import CanvasUser


@admin.register(CanvasUser)
class CanvasUser(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', 'is_staff',)
