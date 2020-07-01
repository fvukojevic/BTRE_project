from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from listings.choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.POST.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings': page_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.POST:
        keywords = request.POST['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'city' in request.POST:
        city = request.POST['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    if 'state' in request.POST:
        state = request.POST['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    if 'bedrooms' in request.POST:
        bedrooms = request.POST['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.POST:
        price = request.POST['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.POST
    }
    return render(request, 'listings/search.html', context)
