from bizapp.models import Business, Contact, Project
from django import forms
from django.contrib import admin
from django.contrib.localflavor.us.forms import USPhoneNumberField

class InlineContactAdmin(admin.TabularInline):
    model = Contact
    extra = 1

class InlineProjectAdmin(admin.TabularInline):
    model = Project
    extra = 1

class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        InlineContactAdmin,
        InlineProjectAdmin,
    ]

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    #using US Phone because generic PhoneNumberField is missing in 1.4
    phone = USPhoneNumberField()
    email = forms.EmailField()

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('name', 'business', 'phone', 'email')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'business')

admin.site.register(Business, BusinessAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)

