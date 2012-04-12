from tastypie import fields
from tastypie.api import Api
from tastypie.resources import ModelResource
from bizapp.models import Business, Contact

class BusinessResource(ModelResource):
    contacts = fields.ToManyField('bizapp.api.ContactResource', 'contacts')

    class Meta:
        queryset = Business.objects.all()
        resource_name = 'businesses'

    #def dehydrate(self, bundle):
        #bundle.data['contacts'] = Business.contacts.throughout
        #return bundle


class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contacts'

v1_api = Api(api_name='v1')
v1_api.register(BusinessResource())
v1_api.register(ContactResource())
