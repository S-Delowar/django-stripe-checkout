from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.urls import reverse
import stripe

# class HomePageView(TemplateView):
#     template_name = 'home.html'

def home(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        print(f"processing")
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1QYw2MLnOacvvlKlXRlJpm3o",
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "home.html")

    
    
    
class SuccessPageView(TemplateView):
    template_name = 'success.html'
    
class CancelPageView(TemplateView):
    template_name = 'cancel.html'