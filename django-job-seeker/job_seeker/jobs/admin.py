from django.contrib import admin

from jobs.models.message import Message


# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "timestamp")


admin.site.register(Message, MessageAdmin)
