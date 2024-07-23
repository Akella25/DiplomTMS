from django.shortcuts import render
from hotel.models import Hotel, Citi
from hotel.forms import HotelSearchForm


def hotel_info(request, pk):
    hotel = Hotel.objects.prefetch_related("city").get(pk=pk)

    return render(request, 'info_hotel.html', {'hotel': hotel})





def search_hotel(request):

    form = HotelSearchForm()
    if request.method == 'POST':
        form = HotelSearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = {}
            if form.cleaned_data['citi']:
                citi = Citi.objects.filter(name=form.cleaned_data['citi']).first()
                data['city'] = citi.id
            #citi = form.cleaned_data['citi']
            if form.cleaned_data['star'] is not None:
                data['stars'] = form.cleaned_data['star']
            #star = form.cleaned_data['star']
            pool = ''
            if form.cleaned_data['pool']:

                if form.cleaned_data['pool'] == 'True':
                    data['swimming_pool'] = True

                else:
                    data['swimming_pool'] = False
            print(data)
            #citi = Citi.objects.filter(name=citi).first().id
            hotels = Hotel.objects.filter(**data).all()
            print(hotels)
            return render(request, 'search.html', {'hotels': hotels, 'form': form})

    return render(request, 'search.html', {'form': form})