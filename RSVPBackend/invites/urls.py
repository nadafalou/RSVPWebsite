from django.urls import path

from invites import views

app_name = 'invites'

urlpatterns = [
    path('createinvite/', views.CreateGuestInvite.as_view(), name='create-invite'),
    path('<pk>', views.GuestInvite.as_view(), name='invite'),
    path('update/<pk>', views.UpdateGuestInvite.as_view(), name='update-invite'),
    path('allInvites/', views.GuestInvites.as_view(), name='all-invites'),
    # path('')
]