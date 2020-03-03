from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

# class SearchForm(forms.Form):
# 	start_date = forms.DateField(required=True,error_messages={
# 		'required':'Must have a start date!'
# 		})
# 	end_date = forms.DateField(required=True,error_messages={
# 		'required':'Must have an end date!'
# 		})
# 	keyword = forms.CharField()
# 	name = forms.CharField()

# 	def clean_start_date(self):
# 		data = self.cleaned_date['start_date']
# 		if data < datetime.date.today():
# 			raise ValidationError(_('Invalid date - start date must be in the past'))
# 		return data



