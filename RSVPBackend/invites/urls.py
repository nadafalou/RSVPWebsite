from django.urls import path

from invites import views

app_name = 'invites'

urlpatterns = [
    path('createinvite/', views.CreateInviteView.as_view(), name='create-invite'),
    path('<pk>', views.InviteView.as_view(), name='invite'),
    path('update/<pk>', views.UpdateInviteView.as_view(), name='update-invite'),
    path('allInvites/', views.ListInvitesView.as_view(), name='all-invites'),
    path('createevent/', views.CreateEventView.as_view(), name='create-event'),
    path('allevents/', views.ListEventsView.as_view(), name='all-events'),
    path('event/<pk>', views.EventView.as_view(), name='event')
]