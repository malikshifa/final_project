import pandas as pd

from django.shortcuts import render, redirect
from psycopg2.extensions import JSON
import re
from project.models import shape
import json
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

user = ''
name = 'shifa',
username = ''
listB = []
type = ''
points = [[37, -109.05], [41, -109.03], [41, -102.05], [37, -102.04]]

def homepage(req):
    return render(req, 'index.html')


def logins(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('map')
        else:
            messages.info(req, 'Username or Password is incorrect')

    context = {}
    return render(req, 'new-login.html', context)


def logoutUser(req):
    logout(req)
    return redirect('logins')


def signup(req):
    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save(),
            name = form.cleaned_data.get('username')
            messages.success(req, 'Account was successfully created for ' + name)
            redirect('login')

    context = {'form': form}
    return render(req, 'new-signup.html', context)


def map(req):
    return render(req, 'map.html')


def mapdata(req):
    if req.method == 'POST':
        pointsin = req.POST.get('stringpoint')
        typein = req.POST.get('type')
        username = req.user
        obj = shape.objects.create(
            point=pointsin,
            shapetype=typein,
            user=username,
        )
        print('success')
    return render(req, 'map.html')


def getmapdata(req):
    df = pd.DataFrame(list(shape.objects.filter(shapetype='rectangle').values()))
    types = df['shapetype'].values

    for item in types:
        type=item

    pointsss = shape.objects.get(user=username).values('point')
    point = str(pointsss)
    result = re.findall(r"[-+]?\d*\.\d+|\d+", point)

    listB = []

    i = 0
    j = 0
    for item in enumerate(result):
        if (i == int(len(result) - 2)):
            listB.append([result[i], result[i + 1]])
            break
        listB.append([result[i], result[i + 1]])
        i += 2
        j += 1

    geo_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": type,
                    "coordinates": [
                        listB
                    ]
                }
            }
        ]
    }
    print(geo_json)
    return render(req, 'map.html', {'geo_json': geo_json})
