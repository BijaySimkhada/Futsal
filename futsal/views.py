from django.shortcuts import render
from .forms import BookingForm
from .models import Booking


# Create your views here.
def showIndex(request):
    return render(request, 'pages/index.html', {'title': 'Homepage | Futsal'})


def showBooking(request):
    context = {}
    if request.method == 'POST':

        form = BookingForm(request.POST or None)

        if form.is_valid():
            booked_date = form.cleaned_data.get('book_date')
            booked_time = form.cleaned_data.get('book_time')
            contact = form.cleaned_data.get('contact')
            booked_futsal = request.POST['futsal_booked']

            book = Booking(booked_date=booked_date, booked_time=booked_time, contact=contact, booked_by=request.user,
                           booked_futsal=booked_futsal)

            book.save()
            return render(request, 'pages/index.html')
        else:
            context['fomr'] = form
            return render(request, 'pages/bookform.html', context)

    else:
        form = BookingForm(request.POST or None)
        context['form'] = form
        return render(request, 'pages/bookform.html', context)
