from django import forms


class categoryForm(forms.Form):

    #breakfastField = forms.BooleanField()
    #lunchField = forms.BooleanField()
    #dinnerField = forms.BooleanField()
    CHOICES = [("breakfast", "Breakfast"),("lunch", "Lunch"), ("dinner", "Dinner")]
    option = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
   

