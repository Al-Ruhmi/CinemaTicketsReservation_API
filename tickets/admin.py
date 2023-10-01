from django.contrib import admin
from .models import Movies,Guest,Reservation,Post
# Register your models here.


admin.site.register(Movies)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Post)