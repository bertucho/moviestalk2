from django.contrib import admin
from quotes.models import Movie
from quotes.models import Quote
from django import forms

class QuoteForm(forms.ModelForm):
	text = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Quote

class MovieAdmin(admin.ModelAdmin):

	class Media:
		js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js',
			'/static/js/jquery-ui.min.js',
			'/static/js/autocomplete.js',
			)
		css = {'all': ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css',)}

class QuoteAdmin(admin.ModelAdmin):
	form = QuoteForm

admin.site.register(Movie, MovieAdmin)
admin.site.register(Quote, QuoteAdmin)