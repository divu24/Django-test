from django.urls import path, include
from . import views
from .views import UserList, UserDetails, GroupList
# from rest_framework_swagger.views import get_swagger_view
#
#
# schema_view = get_swagger_view(title='Swagger API')


urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    # path('o/', schema_view),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('secret/', views.secret_page, name='secret'),
]
