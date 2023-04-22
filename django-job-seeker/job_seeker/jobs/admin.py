from django.contrib import admin

from jobs.models.job_description import JobDescription
from jobs.models.message import Message


# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "timestamp")


admin.site.register(Message, MessageAdmin)


class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "minimum_salary", "maximum_salary",
        "schema", "location", "status",
        "software_company",
    )


admin.site.register(JobDescription, JobDescriptionAdmin)
