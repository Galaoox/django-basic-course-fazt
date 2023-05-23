
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('prefijo/', include('apps.myapp.urls')) de esta forma se agregan prefijos a las urls
    path('', include('apps.myapp.urls'))

]
