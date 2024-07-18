from django.db.models import Count
from django.shortcuts import render, render_to_response
from oscar.core.loading import get_class, get_model
from django.views import generic


# Create your views here.
from my_checkout.views import Order

Product = get_model('catalogue', 'product')
ConditionalOffer = get_model('offer', 'ConditionalOffer')

SLIDER_MAX_PRODUCTS = 10


def home(request):
    context = dict()

    products_featured = Product.objects.filter(featured=True)[:SLIDER_MAX_PRODUCTS]
    products_popular = Product.objects.filter(popular=True)[:SLIDER_MAX_PRODUCTS]
    top_seller = Product.objects.filter(top_seller=True)[:SLIDER_MAX_PRODUCTS]
    offer = ConditionalOffer.objects.all()
    offer_count = offer.count()

    context['products_featured'] = products_featured
    context['products_popular'] = products_popular
    context['offer'] = offer
    context['offer_count'] = offer_count
    context['top_seller'] = top_seller

    return render(request, 'home/index.html', context)


# =================
# How To Pay 
# =================

class HowToPay(generic.ListView):
    model = Order
    template_name = 'oscar/checkout/how_to_pay.html'


def send_email(request):
    return render_to_response('oscar/customer/emails/commtype_registration_body.html')


def print_page(request):
    return render_to_response('oscar/partials/print_page_pdf.html')