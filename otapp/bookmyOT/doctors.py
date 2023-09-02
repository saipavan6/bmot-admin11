

from django.shortcuts import render
import requests

def get_All_Doctors_List():
    Api = 'https://bookmyotservice.pythonanywhere.com/PhysicianList'
    ApiData = requests.get(Api).json()
    if ApiData['Status'] == True:
        return ApiData['ResultData']
    return ApiData

