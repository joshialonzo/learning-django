from django.contrib import admin

from jobs.models.job_description import JobDescription
from jobs.models.message import Message
from jobs.models.question import Question
from jobs.models.selection_process import SelectionProcess
from jobs.models.stage import Stage


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


class SelectionProcessAdmin(admin.ModelAdmin):
    list_display = (
        "job_description",
        "headhunting_firm",
        "software_company",
        "status",
    )


admin.site.register(SelectionProcess, SelectionProcessAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text",)


admin.site.register(Question, QuestionAdmin)


class StageAdmin(admin.ModelAdmin):
    list_display = (
        "selection_process", "channel",
        "platform", "event_date", "interviewer",
    )


admin.site.register(Stage, StageAdmin)
