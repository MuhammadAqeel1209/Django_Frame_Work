from django.urls import path
from. import views
urlpatterns = [
    path("",views.index , name = "ShopHome"),
    path("about/",views.about, name = "AboutUs"),
    path("contact/",views.contact , name = "ContactUs"),
    path("tracker/",views.tracker , name = "TrackingStatus"),
    path("search/",views.search , name = "Search"),
    path("checkout/",views.checkout , name = "CheckOut"),
    path("productviews/<int:id>",views.prodviews , name = "Product View"),
]