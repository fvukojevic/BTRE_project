from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {'listing': listing, 'mvp_realtors': mvp_realtors}
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
