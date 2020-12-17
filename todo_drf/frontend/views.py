from django.shortcuts import render

from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from api.models import Task



# Create your views here.
def list(request):
	return render(request, 'frontend/list.html')



# def post(request):
     
#     ImageFormSet = modelformset_factory(Images,
#                                         form=ImageForm, extra=3)
#     #'extra' means the number of photos that you can upload   ^
#     if request.method == 'POST':
    
#         postForm = TaskForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES,
#                                queryset=Images.objects.none())
    
    
#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#             #post_form.user = request.user
#             post_form.save()
    
#             for form in formset.cleaned_data:
#                 #this helps to not crash if the user   
#                 #do not upload all the photos
#                 if form:
#                     image = form['image']
#                     photo = Images(task=post_form, image=image)
#                     photo.save()
#             # use django messages framework
#             messages.success(request,
#                              "Yeeew, check it out on the home page!")
#             return HttpResponseRedirect("/")
#         else:
#             print(postForm.errors, formset.errors)
#     else:
#         postForm = TaskForm()
#         formset = ImageFormSet(queryset=Images.objects.none())
#     return render(request,'frontend/index.html',
#                   {'postForm': postForm, 'formset': formset})
