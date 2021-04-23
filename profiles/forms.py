from django import forms

from .models import Profile
# from django.contrib.auth.models import UserProfile

from datetimewidget.widgets import DateTimeWidget

from datetime import datetime, date, time, timedelta


class UserProfileAddForm(forms.ModelForm):
	date_range1 = datetime.now().year - 18
	date_range2 = datetime.now().year - 80
	#birth_date=forms.DateField(widget = forms.SelectDateWidget(
		#years=range(date_range1, date_range2, -1)))

	class Meta:
		model = Profile
		fields = ('phone_number', 'birth_date', 'country', 'city', 'zip_code',
				  'timezone', 'organization', 'address', 'website', 'avatar')

		dateTimeOptions = {
			'format': 'dd/mm/yyyy HH:ii P',
			'autoclose': True,
			'showMeridian': True
		}
		widgets = {
			# Use localization and bootstrap 3
			'datetime': DateTimeWidget(attrs={'id': "birth_date"},
									   options = dateTimeOptions,
									   usel10n=True, bootstrap_version=4)
		}



class UserProfileEditForm(forms.ModelForm):
	birth_date = forms.DateField(widget=forms.SelectDateWidget())

	class Meta:
		model = Profile
		fields = ('phone_number', 'birth_date', 'country', 'city', 'zip_code',
				  'timezone', 'organization', 'address', 'website', 'avatar')


class PrimaryProfileAddForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user', 'activation_token', 'key_expires')






