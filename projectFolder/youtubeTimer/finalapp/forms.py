from django import forms
from .models import NewDay
from .models import UserAccount
from .models import Person

class NewDayForm(forms.ModelForm):
    class Meta:
        model = NewDay
        fields = ['date', 'hours', 'minutes']


class EditNewDayForm(forms.ModelForm):
    class Meta:
        model = NewDay
        fields = ['date', 'hours', 'minutes']

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nickname', 'bio', 'age']


