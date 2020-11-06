from django.urls import path
from .import views

urlpatterns = [
    path('', views.landing_page),
    path("home/<str:type>", views.display_product),
    path('show_category/<int:cat_id>', views.show_category),
    path('show_category/<str:all>', views.show_all),
    path('home/<str:type>/<int:id>', views.show_item),
    path('cart', views.display_cart),
    path('add_cart/<int:prod_id>', views.add_to_cart),
]


