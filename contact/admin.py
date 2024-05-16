from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name' , 'phone'
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id','first_name',
    list_per_page = 50
    list_max_show_all = 1000
    list_editable = 'first_name',
    list_display_links = 'phone',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display='name',