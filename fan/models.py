from django.db import models
from django.contrib.auth.models import User
from usuario.models import UsuarioRegistrado

class Fan(UsuarioRegistrado):
    class Meta:
        db_table="FAN"
