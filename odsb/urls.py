from django.urls import path
from . import views
urlpatterns = [
    path('',views.all,name='all'),
    path('studhome',views.studhome,name='studhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('registerT',views.registerT,name='registerT'),
    path('accsp',views.accsp,name='accsp'),
    path('requestFRSP',views.requestFRSP,name='requestFRSP'),
    path('login',views.login,name='login'),
    path('confirm',views.confirm,name='confirm'),
    path('logout',views.logout,name='logout'),
    path('forteacher',views.forteacher,name='forteacher'),
    path('forsp',views.forsp,name='forsp'),
    path('signup_form',views.signup_form,name='signup_form'),
    path('teacher_dashboard',views.teacher_dash,name='teacher_dash'),
    path('service_provider_dash',views.service_provider_dash,name='service_provider_dash'),
    path('give_suggestion',views.give_suggestion,name='give_suggestion'),
    path('teacher_post',views.post,name='post'),
    path('service_provider_post',views.service_provider_post,name='service_provider_post'),
    path('suggestions',views.suggestions,name='suggestions'),
    path('posts',views.posts,name='posts'),
    path('id',views.id,name='id'),
    path('signup_student',views.signup_student,name='signup_student'),
    path('see_suggestions',views.see_suggestions,name='see_suggestions')
]