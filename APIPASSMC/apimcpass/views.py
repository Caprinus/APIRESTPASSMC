from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Seguridad
import json
from django.http import JsonResponse
# Create your views here.


# GPPD para Seguridad
class SeguridadView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def get(self, request, email=''):
        
        if (email !=''):
           usuarios = list(Seguridad.objects.filter(correo_usuario=email).values())
           if len(usuarios) > 0:   
               usuario=usuarios[0]
               datos = {'usuario': usuario}
           else:
               datos = {'message': "Usuarios not found..."}
           return JsonResponse(datos)
        else:
           usuarios = list(Seguridad.objects.values())
           if len(usuarios) > 0:
               datos = {'message': "Success", 'usuarios': usuarios}
           else:
               datos = {'message': "Usuarios not found..."}
           return JsonResponse(datos)
          

    @method_decorator(csrf_exempt)
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Seguridad.objects.create(correo_usuario=jd['correo_usuario'], contrasena=jd['contrasena'], habilitado=jd['habilitado'])                                                                                                                                         
        datos = {'message': "Success"}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def put(self, request, email):
        jd = json.loads(request.body)
        usuarios = list(Seguridad.objects.filter(correo=email).values())
        if len(usuarios) > 0:
            usuario = Seguridad.objects.get(id=id)
            
            usuario.correo_usuario = jd['correo_usuario']
            usuario.contrasena = jd['contrasena']
            usuario.habilitado = jd['habilitado']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def delete(self, request, email):
        usuarios = list(Seguridad.objects.filter(correo_usuario=email).values())
        if len(usuarios) > 0:
            Seguridad.objects.filter(correo_usuario=email).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)

