from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:post_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:post_id>/vote/<str:updown>', views.vote, name='vote'),

    path('account/<str:name>/<str:word>', views.createAccount, name='createAccount'),
    #ex: /
    path('make/<str:title>/<int:posterID>/<str:sub>/<str:body>/<int:happ>/<int:angr>/<int:stress>/<int:energ>/<int:worr>', views.make, name='make'),
]
