from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def contabilit√©(request):
    return render(request,'managment/contabilit√©/contabilit√©.html')   
    