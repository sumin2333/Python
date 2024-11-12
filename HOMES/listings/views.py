
from django.shortcuts import render, redirect
from .models import PropertyListing
from .forms import PropertyListingForm


def supply_view(request):
    if request.method == 'POST':
        form = PropertyListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listings:index')  # 등록 후 메인 페이지로 이동
    else:
        form = PropertyListingForm()

    return render(request, 'supply.html', {'form': form})


