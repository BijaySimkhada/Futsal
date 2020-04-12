from django.contrib import admin
from .models import Booking
from django.contrib.auth.admin import UserAdmin


class BookingAdmin(admin.ModelAdmin):
    ordering = ('verified',)
    list_display = ('booked_futsal', 'booked_by', 'booked_date', 'booked_time', 'booked_at', 'verified')


admin.site.register(Booking, BookingAdmin)