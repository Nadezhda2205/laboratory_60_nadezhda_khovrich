from django.contrib import admin
from booking.models import Booking, BookingProduct


class BookingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'phone', 'address', 'created_at']
    ordering = ['-created_at']


class BookingProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'booking', 'product', 'quantity']


admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingProduct, BookingProductAdmin)


