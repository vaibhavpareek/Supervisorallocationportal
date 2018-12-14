from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    Reg_no = forms.CharField(max_length=10)
    specs = forms.CharField(max_length=100)
    mob = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'Reg_no', 'specs', 'mob', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.Reg_no = self.cleaned_data['Reg_no']
        user.specs = self.cleaned_data['specs']
        user.mob = self.cleaned_data['mob']
        if commit:
            user.save()
        return user


class SignSupForm(UserCreationForm):
    Uid = forms.CharField(max_length=10)
    spec = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'Uid', 'spec', 'mobile', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignSupForm, self).save(commit=False)
        user.Uid = self.cleaned_data['Uid']
        user.spec = self.cleaned_data['spec']
        user.mobile = self.cleaned_data['mobile']
        if commit:
            user.save()
        return user


