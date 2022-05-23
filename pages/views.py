from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
  latest_listings = Listing.objects.order_by('-list_date').all()[:3]

  context = {
    'listings': latest_listings,
    'prices': price_choices,
    'states': state_choices,
    'bedrooms': bedroom_choices
  }
  return render(request, 'pages/index.html', context)

def about(request):
  # get team members
  realtors = Realtor.objects.all()

  # get realtor of the month
  realtor_of_the_month = Realtor.objects.filter(is_mvp=True).all()

  context= {
    'realtors': realtors,
    'mvps': realtor_of_the_month
  }
  return render(request, 'pages/about.html', context)
