from django import forms
from .models import PropertyListing

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['title', 'description', 'price', 'location', 'bedrooms', 'bathrooms','house_type', 'transaction_type',
                  'area','floor_number','parking_spaces' ,'year_built',
                  'images', 'neighborhood_description', 'maintenance_fee' ]
        widgets = {
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
        }