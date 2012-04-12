from bizapp.models import Business, Contact
from django import forms
from django.contrib import admin
from django.contrib.localflavor.us.forms import USPhoneNumberField

class InlineContactAdmin(admin.StackedInline):
    model = Business.contacts.through

class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        InlineContactAdmin,
    ]
    exclude = ('contacts',)

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    #using US Phone because generic PhoneNumberField is missing in 1.4
    phone = USPhoneNumberField()
    email = forms.EmailField()

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm

admin.site.register(Business, BusinessAdmin)
admin.site.register(Contact, ContactAdmin)


