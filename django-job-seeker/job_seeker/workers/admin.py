from django.contrib import admin

from workers.models import Developer
from workers.models import Worker


# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name",
        "linkedin_id", "country", "id",
    )


admin.site.register(Worker, WorkerAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name",
        "linkedin_id", "country", "id",
    )


admin.site.register(Developer, DeveloperAdmin)
