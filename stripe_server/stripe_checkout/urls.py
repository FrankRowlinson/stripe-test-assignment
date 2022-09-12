from django.urls import path


from .views import *


urlpatterns = [
    path('buy/<int:pk>/', checkout_session, name='create-checkout-session'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel')
]