from django.contrib import admin
from .models import polls
# Register your models here.
@admin.register(polls)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")
    prepopulated_fields = {"slug": ("title",)}