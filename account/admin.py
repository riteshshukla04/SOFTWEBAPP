from django.contrib import admin
from .models import Complain,Suggestion,Order,Vendor,Tag,Customer,Booking
admin.site.register(Complain)

class SuggestionAdmin(admin.ModelAdmin):
    list_display=('name','add_time')

admin.site.register(Suggestion,SuggestionAdmin)



admin.site.register(Customer)

class TagAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Tag,TagAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','vendor','status',)
admin.site.register(Order,OrderAdmin)

class VendorAdmin(admin.ModelAdmin):
     list_display=('name','phone','price','type',)
admin.site.register(Vendor,VendorAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=('customer','startdate','Type')

admin.site.register(Booking,BookingAdmin)

admin.site.site_header="SOFT Admin"
admin.site.site_title = "SOFT Admin"
admin.site.index_title = "SOFT Admin"