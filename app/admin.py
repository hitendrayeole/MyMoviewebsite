from django.contrib import admin
from app.models import Detail
from app.models import Crausallink
from app.models import Movie
from app.models import Code
from app.models import TCode
admin.site.register(Detail);
admin.site.register(Movie);
admin.site.register(Crausallink);
admin.site.register(Code);
admin.site.register(TCode);
