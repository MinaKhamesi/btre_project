from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context)

def search(request):
  query_list = Listing.objects.order_by('-list_date')
  # Search Keyword
  if 'keywords' in request.GET:
    keyword = request.GET['keywords']
    if keyword:
      query_list = query_list.filter(description__icontains = keyword)

  # Search City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      query_list = query_list.filter(city__iexact = city)

  # Search state
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      query_list = query_list.filter(state__iexact = state)
  # Search Price
  if 'price' in request.GET:
    price = request.GET['price']
    query_list = query_list.filter(price__lte = price)

  # Search bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    query_list = query_list.filter(bedrooms__lte = bedrooms)

  context = {
    'states': state_choices,
    'prices': price_choices,
    'bedrooms': bedroom_choices,
    'listings': query_list,
    'values': request.GET
  }
  return render(request, 'listings/search.html', context)