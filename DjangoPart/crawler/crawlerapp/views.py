# The views.py file
from django.http import HttpResponse
from crawlerapp.models import Directory, Adress, Photos
from django.template import Context, loader
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# it returns the resonse to the 1st page or Home page. 
def index(request):
    Directory_list = Directory.objects.all()
    return render(request, 'crawlerapp/index.html', {'Directory_list': Directory_list,})

 # it returns the resonse to the Contact Us page   
def contactus(request):
    Directory_list = Directory.objects.all()
    return render(request, 'crawlerapp/contactus.html', {'Directory_list': Directory_list,})



# when a catagory is searched, it takes the request and
# varifies whether it's a category or a place for which we are searching for.
def search(request):
    if 'what' in request.GET and request.GET['what']:
        what = request.GET['what']
        
        crawlerapp = Directory.objects.filter(Catogory__icontains=what)
        return render(request, 'crawlerapp/search.html',
                      {'crawlerapp': crawlerapp, 'query': what})
    

    elif 'who' in request.GET and request.GET['who']:
        who = request.GET['who']
        crawlerapp = Directory.objects.filter(Bussiness_name__icontains=who)
        return render(request, 'crawlerapp/search.html',
                      {'crawlerapp': crawlerapp, 'query': who})
  # if the form field is left blank and searched, it will give the folowing message.      
    else:
        message = 'You submitted an empty form.'

    
    return HttpResponse(message)


# I tried to include paging here and has set a limit of 10
# That is per page will contain only 10 Business details and not more than 10.
def listing(request):
    directory_list = Directory.objects.all()
    paginator = Paginator(directory_list, 10) # Show 10 business details per page

    page = request.GET.get('page')
    try:
        directory = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        directory = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return directory
