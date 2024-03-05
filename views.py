from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template import loader
from .models import Data
import csv
import pyrebase
import os

# Create your views here.


# Initialize Firebase
config = {
    "apiKey": "AIzaSyCqdtAJ_GwhmN8DoVCX7NqmkWIAhFO0C2w",
    "authDomain": "django-2b488.firebaseapp.com",
    "projectId": "django-2b488",
    "storageBucket": "django-2b488.appspot.com",
    "messagingSenderId": "933177512383",
    "appId": "1:933177512383:web:01363dce4da094b9e3110a",
    "measurementId": "G-BWTYJ3Q6Z2",
    "databaseURL": "https://django-2b488-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# Function to upload a file to Firebase Cloud Storage
def upload_file_to_firebase(file_path, destination_path):
    storage.child(destination_path).put(file_path)

# def insertdata(request):
#     if request.method == 'POST':
#         data = Data(
#             year_of_investment = request.POST['year_of_investment'],
#             name_of_doctor = request.POST['name_of_doctor'],
#             tm_name = request.POST['tm_name'],
#             hq_name = request.POST['hq_name'],
#             month_of_investment = request.POST['month_of_investment'],
#             amount_invested = request.POST['amount_invested'],
#             new_renew = request.POST['new_renew'],
#             roi_of_last_year = request.POST['roi_of_last_year'],
#             january_roi = request.POST['january_roi'],
#             february_roi = request.POST['february_roi'],
#             march_roi = request.POST['march_roi'],
#             april_roi = request.POST['april_roi'],
#             may_roi = request.POST['may_roi'],
#             june_roi = request.POST['june_roi'],
#             july_roi = request.POST['july_roi'],
#             august_roi = request.POST['august_roi'],
#             september_roi = request.POST['september_roi'],
#             october_roi = request.POST['october_roi'],
#             november_roi = request.POST['november_roi'],
#             december_roi = request.POST['december_roi'],
#             total = request.POST['total'],
#             times_of_roi = request.POST['times_of_roi'],
#             category = request.POST['category'],
#         )
#         data.save()
#         return redirect('displaydata')
#     return render(request, 'add.html')

# def displaydata(request):
#     data = Data.objects.all().values()
#     return render(request, 'display.html', {'data': data})

import firebase_admin
from firebase_admin import credentials

# Replace this with your Firebase project's credential file path
cred = credentials.Certificate('./credentials.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred)

def insertdata(request):
    if request.method == 'POST':
        db = firebase_admin.firestore.client()

        data_ref = db.collection(u'data')
        data_doc = data_ref.document()

        data = {
            u'year_of_investment': request.POST['year_of_investment'],
            u'name_of_doctor': request.POST['name_of_doctor'],
            u'tm_name': request.POST['tm_name'],
            u'hq_name': request.POST['hq_name'],
            u'month_of_investment': request.POST['month_of_investment'],
            u'amount_invested': request.POST['amount_invested'],
            u'new_renew': request.POST['new_renew'],
            u'roi_of_last_year': request.POST['roi_of_last_year'],
            u'january_roi': request.POST['january_roi'],
            u'february_roi': request.POST['february_roi'],
            u'march_roi': request.POST['march_roi'],
            u'april_roi': request.POST['april_roi'],
            u'may_roi': request.POST['may_roi'],
            u'june_roi': request.POST['june_roi'],
            u'july_roi': request.POST['july_roi'],
            u'august_roi': request.POST['august_roi'],
            u'september_roi': request.POST['september_roi'],
            u'october_roi': request.POST['october_roi'],
            u'november_roi': request.POST['november_roi'],
            u'december_roi': request.POST['december_roi'],
            u'total': request.POST['total'],
            u'times_of_roi': request.POST['times_of_roi'],
            u'category': request.POST['category'],
        }

        data_doc.set(data)
        return redirect('displaydata')
    return render(request, 'add.html')

def displaydata(request):
    db = firebase_admin.firestore.client()
    data_ref = db.collection(u'data')
    data = data_ref.stream()

    return render(request, 'display.html', {'data': data})

# ... (keep the other functions unchanged)

def deletedata(request, id):
    data = get_object_or_404(Data, id=id)
    data.delete()
    return HttpResponseRedirect(reverse('displaydata'))

def updatedata(request, id):
    x = Data.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'x': x,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    year_of_investment = request.POST['year_of_investment']
    name_of_doctor = request.POST['name_of_doctor']
    tm_name = request.POST['tm_name']
    hq_name = request.POST['hq_name']
    month_of_investment = request.POST['month_of_investment']
    amount_invested = request.POST['amount_invested']
    new_renew = request.POST['new_renew']
    roi_of_last_year = request.POST['roi_of_last_year']
    january_roi = request.POST['january_roi']
    february_roi = request.POST['february_roi']
    march_roi = request.POST['march_roi']
    april_roi = request.POST['april_roi']
    may_roi = request.POST['may_roi']
    june_roi = request.POST['june_roi']
    july_roi = request.POST['july_roi']
    august_roi = request.POST['august_roi']
    september_roi = request.POST['september_roi']
    october_roi = request.POST['october_roi']
    november_roi = request.POST['november_roi']
    december_roi = request.POST['december_roi']
    total = request.POST['total']
    times_of_roi = request.POST['times_of_roi']
    category = request.POST['category']
    member = Data.objects.get(id=id)
    member.year_of_investment = year_of_investment
    member.name_of_doctor = name_of_doctor
    member.tm_name = tm_name
    member.hq_name = hq_name
    member.month_of_investment = month_of_investment
    member.amount_invested = amount_invested
    member.new_renew = new_renew
    member.roi_of_last_year = roi_of_last_year
    member.january_roi = january_roi
    member.february_roi = february_roi
    member.march_roi = march_roi
    member.april_roi = april_roi
    member.may_roi = may_roi
    member.june_roi = june_roi
    member.july_roi = july_roi
    member.august_roi = august_roi
    member.september_roi = september_roi
    member.october_roi = october_roi
    member.november_roi = november_roi
    member.december_roi = december_roi
    member.total = total
    member.times_of_roi = times_of_roi
    member.category = category
    member.save()
    return HttpResponseRedirect(reverse('displaydata'))

def export(request):
    profiles = Data.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=exported_file.csv'
    writer = csv.writer(response)
    writer.writerow(['YEAR OF INVESTMENT', 'NAME OF DOCTOR', 'TM NAME', 'HQ', 'MONTH OF INVESTMENT', 'INVESTED AMT', 'NEW/RENEW 2023', 'LAST YEAR ROI FROM INVESTED MONTH', 'JAN', 'FEB', 'MARCH', 'APRIL', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'TOTAL', 'TIMES OF ROI V/S INVESTMENT', 'CATEGORY- SATISFACTORY/POOR'])
    profile_fields = profiles.values_list('year_of_investment', 'name_of_doctor', 'tm_name', 'hq_name', 'month_of_investment', 'amount_invested', 'new_renew', 'roi_of_last_year', 'january_roi', 'february_roi', 'march_roi', 'april_roi', 'may_roi', 'june_roi', 'july_roi', 'august_roi', 'september_roi', 'october_roi', 'november_roi', 'december_roi', 'total', 'times_of_roi', 'category')
    for profile in profile_fields:
        writer.writerow(profile)
    return response