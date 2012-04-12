from django.shortcuts import redirect

def home(request):
    return redirect('/api/v1/?format=json')
