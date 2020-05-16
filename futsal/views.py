from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from account.models import Account, FutsalInfo, UserInfo


# Create your views here.
def showIndex(request):
    futsals = FutsalInfo.objects.all()[:4]
    return render(request, 'pages/index.html', {'title': 'Homepage | Futsal', 'futsals': futsals})


def showBooking(request, name):
    context = {}
    if request.method == 'POST':

        form = BookingForm(request.POST or None)

        if form.is_valid():
            booked_date = form.cleaned_data.get('book_date')
            booked_time = form.cleaned_data.get('book_time')
            booked_futsal = request.POST['futsal_booked']

            futsals = FutsalInfo.objects.all()

            for futsal in futsals:
                if str(futsal.futsal_name) == booked_futsal:
                    fut = futsal
                    book = Booking(booked_date=booked_date, booked_time=booked_time, contact=request.user.email,
                                   booked_by=request.user, booked_futsal=fut)
                    book.save()
                    break
                else:
                    continue

            return redirect('/')
        else:
            context['form'] = form
            return render(request, 'pages/bookform.html', context)

    else:
        form = BookingForm(request.POST or None)
        context['form'] = form
        context['name'] = name
        return render(request, 'pages/bookform.html', context)
