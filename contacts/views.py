from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method =='POST':
        return 
    return render(request,'lisings/listing.html')
