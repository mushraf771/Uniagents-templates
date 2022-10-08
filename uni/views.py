from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request,'home.html')
class BaseView(View):
    def get(self, request):
        return render(request,'base.html')
class InstituationService(View):
    def get(self, request):
        return render(request,'instituation-service.html')
class StudentPromotional(View):
    def get(self, request):
        return render(request,'student-promotional.html')
class StudentRegister(View):
    def get(self, request):
        return render(request,'student-register.html')
class StudentClientSpeak(View):
    def get(self, request):
        return render(request,'student-clients-speak.html')
    
# for consultent
class AgentCrm(View):
    def get(self, request):
        return render(request,'agent_crm.html')
class AgentWebsite(View):
    def get(self, request):
        return render(request,'agent_website.html')
class AgentResearch(View):
    def get(self, request):
        return render(request,'agent_research.html')
class AgentRegister(View):
    def get(self, request):
        return render(request,'agent_register.html')