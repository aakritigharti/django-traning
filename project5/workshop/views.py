from django.shortcuts import render,get_object_or_404
from .models import *

def workshop_list(request):

    template_name = "workshop/workshop_list.html"
    context = {
     "title" :" Workshop list",
      "workshops" :Workshop.objects.all(),
      "members" :Member.objects.all(),
    

        }
    return render(request, template_name, context)
    
def workshop_detail(request, id):
        template_name = "workshop/workshop_detail.html" 
        workshop = get_object_or_404(Workshop,id=id)
        member = get_object_or_404(Member,workshop=workshop)

        context = {
             "workshop": workshop,
              "member": member
        }
     
        return render(request, template_name, context) 

          
       
    
    
 