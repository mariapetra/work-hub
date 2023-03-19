from django.contrib import admin

from .models import Jobs


class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'description', 'location', 'hours',
                    'contract_type', 'manager', 'manager_email', 'salary', 'notes', 'owner')


admin.site.register(Jobs, JobAdmin)
