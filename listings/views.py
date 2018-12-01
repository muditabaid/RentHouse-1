from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from realtors.models import Realtor
# Create your views here.
from .models import Listing
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True) #put condition on object list 
    paginator=Paginator(listings,2)
    page=request.GET.get('page') #request parameter
    paged_listings=paginator.get_page(page)
    context ={
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')

