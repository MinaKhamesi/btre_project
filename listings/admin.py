from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display= ('id', 'title', 'is_published', 'city', 'state', 'price', 'realtor')
  list_display_links= ( 'id', 'title',)
  list_per_page=25
  search_fields=('title', 'zipcode', 'city', 'state', 'price', 'description')
  list_filter=('realtor',)
  list_editable=('is_published',)

admin.site.register(Listing, ListingAdmin)
