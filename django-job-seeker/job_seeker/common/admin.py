from django.contrib import admin

from companies.models.job_type import JobType


# Register your models here.

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date", "updated_date")


admin.site.register(
    JobType, JobTypeAdmin,
)
