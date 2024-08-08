from django.contrib import admin

from record.models import Records


# Register your models here.
@admin.register(Records)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sign_of_publication',)
