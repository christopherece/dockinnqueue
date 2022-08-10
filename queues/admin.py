from .models import Queue
from django.contrib import admin

# Register your models here.
class QueueAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'name',
    )
admin.site.register(Queue, QueueAdmin)


