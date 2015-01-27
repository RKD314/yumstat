from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

authomatic = Authomatic(CONFIG, 'asjdf897akfj!asdjf?ajfowi')


#def index(request):
#    return render(request, 'simple/index.html')


def login(request, provider_name):
    response = HttpResponse()
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
    
    if result:	#we have a result, so the login procedure has finished, and we should render a result

    	if result.user:	#we have the user logged in, we should verify the id and name
    		result.user.update()	
	        response=render_to_response('simple/user.html', {'username':result.user.name, 'profile_pic':result.user.picture, 'user_id':result.user.id})
	        
    	elif result.error:	#there was an error logging in
	    	response=render_to_response('simple/login_error.html')	    
        
    return response
