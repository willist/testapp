About
=====

Sample app written for the folks at `WillowTree Apps <http://www.willowtreeapps.com/>`_.

Description
===========

Simple database for storing information about business contacts.

- Django application
- Backed by sqlite3
- Using django-tastypie for rest api

API v1
======

/api/v1/
--------

Base API URI. Retrieve information about subresources.

/api/v1/businesses/
-------------------

Retrieve list of businesses.

/api/v1/businesses/{business_id}/
---------------------------------

Retrieve a single business.

/api/v1/contacts/
-----------------

Retrieve a list of contacts.

Methods:

================ ======= =================================================
Parameter        Value   Description
================ ======= =================================================
name             string  Filter contacts by name (exact match required).
name__icontains  string  Filter contacts by substring match of name (case 
                         insensitive).
email            string  Filter contacts by email (exact match required).
email__icontains string  Filter contacts by substring match of email (case    
                         insensitive).
phone            integer Filter contacts by phone (exact match required).
phone__contains  integer Filter contacts by substring match of phone (case 
                         insensitive).
================ ======= =================================================

/api/v1/contacts/{contact_id}/
------------------------------

Retrieve a single contact.
