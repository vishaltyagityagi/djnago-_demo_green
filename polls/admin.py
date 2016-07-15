from django.contrib import admin
from .models import Question,Blog,RegistrationForm,Product,Service,Content,Email,Cms


admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(RegistrationForm)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Content)
admin.site.register(Email)
admin.site.register(Cms)
