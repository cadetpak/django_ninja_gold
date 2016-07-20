from django.conf.urls import patterns, url 
from . import views

# ANY URLs that you expect, and what view functions they direct to.

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^process_gold$', views.process_gold),
	url(r'^new_game$', views.new_game),
]