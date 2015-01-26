from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
	return HttpResponse('''
		<html>
			<link href='http://fonts.googleapis.com/css?family=Raleway:100,200,300,400,600' rel='stylesheet' type='text/css'>
			<!--<link href='http://fonts.googleapis.com/css?family=Open+Sans:100,200,300,400,600' rel='stylesheet' type='text/css'>-->
			<link href="/static/site_flow/stylesheet_yumstat.css" rel="stylesheet" type="text/css" media="screen" />
			<body>
				<nav>
					<ul>
						<li><small_space></li>
						<li><a href=""><div id="logo_rect"><img src = "/static/site_flow/yumstat_logo.png" height="55" width="auto" alt="Yumstat: An app to track baby's solid foods"></div></a></li>
						<li><med_space></li>
						<li><div id="rect">about</div></li>
						<li><div id="rect">FAQ</div></li>
					</ul>
				</nav>
				<br />
				<med_space>The world is full of <b>flavor</b>
				<br />
				<br />
				<br />
				<br />
				<med_space><med_space><med_space><med_space>Help your baby <b>explore</b> it
				<br />
				<br />
				<br />
				<ul>
					<li><a href="{% url simple %}"><div id="nav_rect">sign in</div></a></li>
					<li><div id="nav_rect">sign up</div></li>
				</ul>
			</body>
		</html>
    	''')
    
    #return HttpResponse('''
    #	Hello! <br />
    #	This is typing on multiple lines.
    #	''')