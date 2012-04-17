from tastypie import fields
from tastypie.api import Api
from tastypie.resources import ModelResource
from bizapp.models import Business, Contact, Project

class BusinessResource(ModelResource):
    contacts = fields.ToManyField('bizapp.api.ContactResource', 'contact_set')
    projects = fields.ToManyField('bizapp.api.ProjectResource', 'project_set')

    class Meta:
        queryset = Business.objects.all()
        resource_name = 'businesses'

class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contacts'
        filtering = {
            "email": ("icontains", "exact", ),
            "phone": ("icontains", "exact", ),
            "name": ("icontains", "exact", ),
        }

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'

v1_api = Api(api_name='v1')
v1_api.register(BusinessResource())
v1_api.register(ContactResource())
v1_api.register(ProjectResource())
