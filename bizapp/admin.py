from bizapp.models import Business, Contact
from django import forms
from django.contrib import admin
from django.contrib.localflavor.us.forms import USPhoneNumberField

class InlineContactAdmin(admin.TabularInline):
    model = Contact

class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        InlineContactAdmin,
    ]

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    #using US Phone because generic PhoneNumberField is missing in 1.4
    phone = USPhoneNumberField()
    email = forms.EmailField()

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('name', 'business', 'phone', 'email')

admin.site.register(Business, BusinessAdmin)
admin.site.register(Contact, ContactAdmin)


