from bizapp.models import Business, Contact
from django.contrib import admin

class InlineContactAdmin(admin.StackedInline):
    model = Business.contacts.through

class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        InlineContactAdmin,
    ]
    exclude = ('contacts',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

admin.site.register(Business, BusinessAdmin)
admin.site.register(Contact, ContactAdmin)


