from django.shortcuts import render, HttpResponse
from team.models import Profile
# from django.contrib import messages
from team.models import Profile
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context={
    #     'variable':"THIS IS SENT"
    # }
    return render(request,'index.html')
def team(request):
    return render(request,'team.html')

# def profile_submit(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         profile = Profile(
#             first_name=form_data['first_name'],
#             middle_name=form_data['middle_name'],
#             last_name=form_data['last_name'],
#             linkedin=form_data['linkedin'],
#             instagram=form_data['instagram'],
#             github=form_data['github'],
#             profile_pic=request.FILES.get('profile_pic')
#         )
#         profile.save()
#         return redirect('profile_success')  # Redirect to a success page

#     return render(request, 'profile_form.html')
def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        linkedin = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # contact = Contact(name=name, email=email,phone=phone,desc=desc,image=image, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
   
    return render(request, 'contact.html')

