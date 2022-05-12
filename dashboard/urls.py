from django.urls import path,include

from . import views

urlpatterns=[
    path('mentor/',views.mentor,name='mentor'),
    path('student/',views.student,name='student'),
    path('collaborator/',views.collaborator,name='collaborator'),
    path('volunteer/',views.volunteer,name='volunteer'),
    path('manager/',views.manager,name='manager'),
    path('student/profile',include('details.urls')),
    path('student/session',include('session.urls')),
    path('student/attendance',include('attendance.urls')),
    path('student/assignments',include('assignments.urls')),
    path('student/logout',include('accounts.urls')),
    path('mentor/logout', include('accounts.urls')),
    path('student/chatbotFAQ/',include('chatbotFAQ.urls')),
    path('mentor/chatbotFAQ/',include('chatbotFAQ.urls')),
    path('mentor/profile',include('details.urls')),
    path('mentor/attendance',include('attendance.urls')),
    path('mentor/session',include('session.urls')),
    path('mentor/forum',views.forum,name="forum"),
    path('mentor/session/visual',views.visual,name="visual"),
    path('manager/profile',include('details.urls')),
    #path('mentor/session',include('sessions.urls'))
   #path('mentor/session',include('sessions.urls'))
]