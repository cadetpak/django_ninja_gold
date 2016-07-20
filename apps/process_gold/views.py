from django.shortcuts import render, redirect
import random # Need to import 'random' to use function
import string # Need to import 'string' to use function

# Display main page '/' and set initial session factors
def index (request):
	if 'gold' in request.session:
		pass # Pass does not do anything.
	else:
		request.session['gold'] = 0

	if 'activity_log' in request.session:
		pass
	else:
		request.session['activity_log'] = []

	return render (request, 'process_gold/index.html')

# Whenever 'Find Gold!' button is pushed, this action is triggered.
def process_gold(request):
	if request.POST['building'] == 'farm':
		# Will generage random number from 10-20
		coins = random.randrange(10,21)
		message = ''.join(["You have pilfered crops worth ", str(coins), " gold! "])
		request.session['activity_log'].append(message)
		request.session['gold'] += coins

	if request.POST['building'] == 'cave':
		coins = random.randrange(5,11)
		message = ''.join(["You have mined minerals worth ", str(coins), " gold! "])
		request.session['activity_log'].append(message)
		request.session['gold'] += coins

	if request.POST['building'] == 'house':
		coins = random.randrange(2,6)
		message = ''.join(["You have robbed a home of ", str(coins), " gold! "])
		request.session['activity_log'].append(message)
		request.session['gold'] += coins

	if request.POST['building'] == 'casino':
		coins = random.randrange(-50,51)
		if coins > -1: 
			message = ''.join(["You have waged on slots and gained ", str(coins), " gold!"])
		else:
			message = ''.join(["You have waged on slots and lost ", str(coins), " gold!"])
		request.session['activity_log'].append(message)
		request.session['gold'] += coins

	return redirect('/')

# Clear out session data.
def new_game(request):
	del request.session['gold']
	del request.session['activity_log']
	return redirect('/')

