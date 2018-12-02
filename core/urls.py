from django.urls import path, include

from core.views import users, network

scanner_patterns = [
    path('netstat/', network.Netstat.as_view()),
    path('ifstat/', network.Ifstat.as_view()),
    path('network-common-info/', network.NetworkCommonInfo.as_view()),
    path('packets-info/', network.PacketsInfo.as_view())
]

urlpatterns = [
    path('login/', users.SigninView.as_view()),
    path('signup/', users.SignupView.as_view()),
    path('scanners/', include(scanner_patterns))
]
