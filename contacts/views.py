from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact

from django.contrib import messages

def add_contact(request):
  if request.method == 'POST':
    # get fields
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    # Chek if user has already made the inquary
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(
        listing_id=listing_id,
        user_id=user_id,
      )
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)
        

    contact = Contact(
      listing_id = listing_id,
      name=name,
      email=email,
      listing=listing,
      phone=phone,
      message=message,
      user_id=user_id,
    )

    contact.save()

    # Send mail
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign in to admin panel for more info',
    #   'minakhamesi@gmail.com',
    #   [realtor_email, 'minakhamesi@gmail.com'],
    #   fail_silently=False
    # )


    messages.success(request, 'your request has been submitted, a realtor will get back to you')
  return redirect('/listings/'+listing_id)
