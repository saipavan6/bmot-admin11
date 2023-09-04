from django.shortcuts import render

from .bookmyOT.dashboard import dashboard
from otapp.bookmyOT.doctors import get_All_Doctors_List
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = dashboard()
    return render(request, 'bookmy _ot.html', data)


def data():
    pass


def physician_list(request):

    physicians_data = get_All_Doctors_List()
    print(physicians_data)
    context = {
        'physicians_data': physicians_data,
    }
    return render(request, 'getphysician.html', context)



def view_physician(request,id):
    # Your plain text content
    print(id)
    text_content = "This is a plain text response."
    # Create an HttpResponse object with the text content and set the content type
    response = HttpResponse(text_content, content_type='text/plain')
    return response