from django.urls import path

from api.views import user_views
from api.views import calon_karyawan_views
from api.views import departement_views

urlpatterns = [
    path('all-users/', user_views.getUsers, name='get-users'),
    path('register/', user_views.register, name='register-users'),
    path('login/', user_views.login, name='login-users'),
    path('user-edit/<int:user_id>/', user_views.updateUser, name='update-users'),
    path('partial-user-edit/<int:user_id>/', user_views.PartialUpdateUser, name='partial_update_user'),
    path('delete-user/<int:user_id>/', user_views.deleteUser, name='delete-users'),

    path('upload-calon-karyawan', calon_karyawan_views.createCalonKaryawan.as_view(), name='upload-keryawan'),

    path('create-departement/', departement_views.createdepartement, name='create-departement'),
]