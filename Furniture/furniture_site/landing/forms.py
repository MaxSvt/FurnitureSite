from django import forms


class FeedBackForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Фамилия', 'class': 'form-control'}
        )
    )
    phone_number = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Телефон', 'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'your_email@example.ru', 'class': 'form-control'}
        )
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'class': 'form-control'}
        )
    )
