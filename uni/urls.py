
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from uni import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home'),
    path('base/',views.BaseView.as_view(),name='base'),
    path('instituation-service/',views.InstituationService.as_view(),name='instituation-service'),
    path('student-promotional/',views.StudentPromotional.as_view(),name='student-promotional'),
    path('student-register/',views.StudentRegister.as_view(),name='student-register'),
    path('clients-speak-student/',views.StudentClientSpeak.as_view(),name='clients-speak-student'),
# for consultents
    path('agent_crm/',views.AgentCrm.as_view(),name='agent_crm'),
    path('agent_website/',views.AgentWebsite.as_view(),name='agent_website'),
    path('agent_research/',views.AgentResearch.as_view(),name='agent_research'),
    path('agent_register/',views.AgentRegister.as_view(),name='agent_register'),

]
