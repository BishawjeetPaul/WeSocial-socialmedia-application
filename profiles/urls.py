from django.urls import path
from .views import (
	profile_view,
	invites_received_view,
	ProfileListVIew,
	invite_profiles_list_view,
	send_invitation,
	remove_from_friends,
	accept_inviatation,
	reject_inviatation,
	accept_inviatation,
	reject_inviatation,
	ProfileDetailView,
)


app_name = 'profiles'

urlpatterns = [
	
	path('', ProfileListVIew.as_view(), name='all-profiles-view'),
	path('my-profile/', profile_view, name='profile-view'),
	path('my-invites/', invites_received_view, name='my-invites-view'),
	path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
	path('send-invite/', send_invitation, name='send-invite'),
	path('remove-friend/', remove_from_friends, name='remove-friend'),
	path('my-invites/accept/', accept_inviatation, name='accept-invite'),
	path('my-invites/reject/', reject_inviatation, name='reject-invite'),
	path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
]