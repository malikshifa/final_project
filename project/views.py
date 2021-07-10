import pandas as pd

from django.shortcuts import render, redirect
import re
from project.models import shape
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

user = ''
name = 'shifa',
username = ''
listB = []
type = ''
points = [[37, -109.05], [41, -109.03], [41, -102.05], [37, -102.04]]

def homepage(req):
    return render(req, 'index.html')


# def tempt(req):
#     return render(req, 'temp.html')


def logins(req):
    #if req.user.is_authenticated:
     #   return redirect('map')
    #else:
    if req.method == 'POST':
        username = req.POST.get('username')
        userid = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('map')
        else:
            messages.info(req, 'Username or Password is incorrect')

    context = {}
    return render(req, 'new-login.html', context)

@login_required(login_url='logins')
def logoutUser(req):
    logout(req)
    return redirect('logins')


def signup(req):
    #if req.user.is_authenticated:
    #    return redirect('map')
    #else:
    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save(),
            name = form.cleaned_data.get('username')
            messages.success(req, 'Account was successfully created for ' + name)
            redirect('logins')

    context = {'form': form}
    return render(req, 'new-signup.html', context)

@login_required(login_url='logins')
def map(req):
    return render(req, 'temp.html')


@login_required(login_url='logins')
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
    return redirect('getmapdata')


@login_required(login_url='logins')
def getmapdata(req):
    current_user = req.user
    listB = []
    listC = []
    df = pd.DataFrame(list(shape.objects.filter(user=current_user.id).values()))
    if len(df) == 0:
        print("0 array")
        return redirect('map')
    types = df['shapetype'].values
    shapes = df['point'].values

    counter = 1

    for item in shapes:
        pointsss = re.findall(r"[-+]?\d*\.\d+|\d+", str(item))
        i = 0

        for item in enumerate(pointsss):
            if i == int(len(pointsss) - 2):
                listB.append([float(pointsss[i]), float(pointsss[i + 1])])
                break

            listB.append([float(pointsss[i]), float(pointsss[i + 1])])
            i += 2
        listC.append(listB)
        listB = []

    for item in listC:
        print(item)
        print('/n')
    # return render(req, 'map.html')
    return render(req, 'map.html', {'listB': listB})

def get_coord_len(req):
    current_user = req.user
    df = pd.DataFrame(list(shape.objects.filter(user=current_user.id).values()))
    print('print length:')
    print(len(df))
    return render(req, 'map.html')


def single_shape(req):
    print('dummy')
    current_user = req.user
    #print(current_user)

    df = pd.DataFrame(list(shape.objects.filter(user=current_user.id).values()))
    #print(df)
    types = df['shapetype'].values
    pointsss = df['point'].values
    #print(types)
    #print(point)


    for item in types:
        type = item


    #pointsss = shape.objects.get(user=username).values('point')
    point = str(pointsss)
    result = re.findall(r"[-+]?\d*\.\d+|\d+", point)
    
    listB = []

    i = 0
    j = 1
    listC = []
    #print(int(len(result) - 2))
    #print("/n")
    for item in enumerate(result):
        if (i == int(len(result) - 2)):
            listB.append([result[i], result[i + 1]])
            break
        listB.append([result[i], result[i + 1]])
        if j == 4:
            listC.append([listB[j],listB[j-1],listB[j-2],listB[j-3]])
            print(j)
            print('/n')
            print(listC)
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
    #print(geo_json)
    return render(req, 'map.html', {'lisB': listB})

    #return render(req, 'map.html')