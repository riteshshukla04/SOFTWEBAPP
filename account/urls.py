from django.urls import path
from django.contrib.auth import views as auth_views



from. import views 
urlpatterns=[
    path("login/",views.Login),
    path("register/",views.registerPage,name="register"),
    path("logout/",views.logoutUser),
    path("user/",views.userPage),
    path("",views.homepage),
    path('feedback/',views.feedbackhome,name='home'),
    path('feedback/add-complain/',views.add_complain,name='add-complain'),
    path('feedback/add-suggestion/',views.add_suggestion,name='add-suggestion'),
    path('Vendor/',views.vendors),
    path('vendorregister/',views.VendorRegister),
    path('store/<str:pk>/',views.store),
    path('vendorform/',views.VendorForm),
    path('vendorinfo/<str:pk>/',views.vendorinfo),
    path('complete/<str:pk>/',views.complete_order),
    path('delete/<str:pk>/',views.delete_order),
    path('addorder/<str:pk>/',views.add_order),
    path('myorder',views.myorder),
    path('update/<str:pk>',views.updatecustomer),
    path('contacts/',views.contact),
    path('search/',views.search),
    path('book/',views.book),
    path('like/<str:pk>',views.addlike),
    path('deleteBooking/<str:pk>',views.deleteBooking),
    path('updatebooking/<str:pk>',views.updateBooking),
    path('aboutus/',views.aboutus),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('check/',views.check),
    
]
