from django.contrib import admin
from django.contrib import admin
from .models import Foo

@admin.register(Foo)
class FooAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')  # Replace 'some_other_field' with actual field names
    list_filter = ('status',)
