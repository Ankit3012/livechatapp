from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("regis/", views.registration, name="regis"),
    path("login/chat/<int:uid>", views.chat, name="chat"),
    path("chat/<int:uid>", views.chat, name="chat"),
    path("login/ticket/<int:tid>", views.ticket, name="ticket"),
    path("ticket/<int:tid>", views.ticket_user, name="ticketuser"),
    path('login/chat/messages/<int:sender>/<int:receiver>', views.get, name='message-detail'),
    path('messages/<int:sender>/<int:receiver>', views.get, name='message-detail'),
    path('messages', views.message_list, name='messages'),
    path('openusersave', views.openusersave, name='openusersave'),
    path('openmessages', views.open_message_list, name='openmessages'),
    path('login/chat/update', views.update, name='update'),
    ]