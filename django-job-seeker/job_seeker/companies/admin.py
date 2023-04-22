from django.contrib import admin

from companies.models.company import Company
from companies.models.job_type import JobType


# Register your models here.

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_date", "updated_date", "id")


admin.site.register(JobType, JobTypeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name", "company_url",
        "linkedin_id", "country", "id",
    )


admin.site.register(Company, CompanyAdmin)
