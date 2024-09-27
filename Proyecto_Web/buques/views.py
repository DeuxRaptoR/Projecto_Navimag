from django.shortcuts import render
from buques.models import Usuario, Buque, Departamento, Sistema, Equipo, Registro, Fecha, Equipos, Historial, HistorialCal
import datetime


def mostrarIndex(request):
    return render(request, 'index.html')



def iniciarSesion(request):
    if request.method == "POST":
        nom = request.POST["txtusu"]
        pas = request.POST["txtpas"]

        comprobarLogin = Usuario.objects.filter(nombre_usuario=nom, password_usuario=pas).values()

        registros = Registro.objects.select_related('buque').all()

        fechas = Fecha.objects.select_related('buque').all()

        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo



        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo


        for sig in registros:
                proxi_man = sig.ultimo_horometro + sig.equipo.hora_standar

                pro.siguiente = proxi_man                   


        #------------------------------------------------------------------------------------------------------
        



                  

        if comprobarLogin:
            request.session["estadoSesion"] = True
            request.session["idUsuario"] = comprobarLogin[0]['id']
            request.session["nomUsuario"] = nom.upper()

            datos = {
                'nomUsuario' : nom.upper(), 
                'registros' : registros,
                'fechas' : fechas

            }

        


            if nom.upper() == "ADMIN":
                return render(request, 'menu_principal.html', datos)
            else:
                return render(request, 'menu_usuario.html', datos)
        
        else:
            datos = { 'r2' : 'Error De Usuario y/o Contraseña!!' }
            return render(request, 'index.html', datos)
    
    else:
        datos = { 'r2' : 'No se Puede Procesar La Solicitud!!' }
        return render(request, 'index.html', datos)



def cerrarSesion(request):
    try:
        nom = request.session['nomUsuario']
        del request.session['nomUsuario']
        del request.session['estadoSesion']

        return render(request, 'index.html')
    except:
        return render(request, 'index.html')



def mostrarMenu(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            registros = Registro.objects.select_related('buque').all()
            fechas = Fecha.objects.select_related('buque').all()


            # Calcular el estado para cada registro
            for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


            for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo


            for sig in registros:
                proxi_man = sig.ultimo_horometro + sig.equipo.hora_standar

                pro.siguiente = proxi_man



            
            for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo


            #-------------------------------------------------------------------------------------------------




                
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'registros' : registros,
                'fechas' : fechas
            }



            return render(request, 'menu_principal.html', datos )
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



def mostrarMenuCalendario(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            registros = Registro.objects.select_related('buque').all()
            fechas = Fecha.objects.select_related('buque').all()


           
            for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


            for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo


            
            for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo


            #-------------------------------------------------------------------------------------------------

            for fec in fechas:

                actual = datetime.date.today()
                numero = fec.frecuencia
                formula1 = fec.ult_mantenimiento + datetime.timedelta(days=numero)
                dias_faltantes = (formula1 - actual).days
                status = fec.frecuencia / 5

                fec.resultado = formula1

                fec.dias = dias_faltantes


                if dias_faltantes < 0:
                    fec.categoria = "VENCIDO"
                elif dias_faltantes <= status:
                    fec.categoria = "POR VENCER"
                else: 
                    fec.categoria = "OK" 
                            

                
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'registros' : registros,
                'fechas' : fechas
            }



            return render(request, 'calendario_admin.html', datos )
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



def mostrarMenuCalendarioUsuario(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            registros = Registro.objects.select_related('buque').all()
            fechas = Fecha.objects.select_related('buque').all()


            # Calcular el estado para cada registro
            for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


            for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo


            
            for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo


            #-------------------------------------------------------------------------------------------------

            for fec in fechas:

                actual = datetime.date.today()
                numero = fec.frecuencia
                formula1 = fec.ult_mantenimiento + datetime.timedelta(days=numero)
                dias_faltantes = (formula1 - actual).days
                status = fec.frecuencia / 5

                fec.resultado = formula1

                fec.dias = dias_faltantes


                if dias_faltantes < 0:
                    fec.categoria = "VENCIDO"
                elif dias_faltantes <= status:
                    fec.categoria = "POR VENCER"
                else: 
                    fec.categoria = "OK"



                
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'registros' : registros,
                'fechas' : fechas
            }



            return render(request, 'calendario_usuario.html', datos )
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



def mostrarMenuUsuario(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            registros = Registro.objects.select_related('buque').all()
            fecha = Fecha.objects.select_related('buque').all()


            # Calcular el estado para cada registro
            for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


            for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo


            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'registros' : registros,
                'fecha' : fecha

            }

            return render(request, 'menu_usuario.html', datos)
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)


#--------------------------------------------------------------------------------------------

def mostrarFormRegistrarBuque(request):
    return render(request, 'form_registrar_buque.html')




def registrarBuque(request):
    if request.method == "POST":
        buq = request.POST["txtbuq"].upper()
        hor = request.POST["numhor"]

        comprobarBuque = Buque.objects.filter(nombre_buque=buq, horometro=hor)
        if comprobarBuque:

            est = Buque.objects.all().values().order_by("nombre_buque")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'est' : est,
                'r2' : 'El Buque ('+buq.upper()+') Ya Existe!!'
            }
            return render(request, 'form_registrar_buque.html', datos)

        else:
            
            # se registra el nuevo estilo.
            est = Buque(nombre_buque=buq,horometro=hor)
            est.save()


            # se recuperan todos los estilos para listarlos.
            est = Buque.objects.all().values().order_by("nombre_buque")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'est' : est,
                'r' : 'Buque ('+buq+') Registrado Correctamente!!'
            }

            return render(request, 'form_registrar_buque.html', datos)

    else:

        est = Buque.objects.all().values()

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'est' : est,
            'r2' : 'Debe Presionar El Botón Para Registrar El Buque!!'
        }

        return render(request, 'form_registrar_buque.html', datos)




def mostrarFormActualizarBuque(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Buque.objects.get(id=id)

            est = Buque.objects.all().values().order_by("nombre_buque")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                'est' : est
            }

            return render(request, 'form_actualizar_buque.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        est = Buque.objects.all().values().order_by("nombre_buque")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'est':est,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def actualizarBuque(request, id):
    try:
        buq = request.POST['txtbuq'].upper()
        hor = request.POST['numhor']

        est = Buque.objects.get(id=id)
        est.nombre_buque = buq
        est.horometro = hor
        est.save()



        est = Buque.objects.all().values().order_by("nombre_buque")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'est' : est, 
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)

    except:
        
        est = Buque.objects.all().values().order_by("nombre_buque")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'est' : est,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def eliminarBuque(request, id):
    try:
        
        est = Buque.objects.get(id=id)
        nom = est.nombre_buque
        est.delete()


        est = Buque.objects.all().values().order_by("nombre_buque")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'est':est,
            'r' : "Registro de Buque Eliminado Correctamente!!"
        }

        return render(request, "form_registrar_buque.html", datos)

    except:

        est = Buque.objects.all().values().order_by("nombre_buque")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'est':est,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar Buque!!"
        }

        return render(request, 'form_registrar_buque.html', datos)



# ---------------------------------------------------------------------------------------------------------------


def mostrarFormActualizarDepartamento(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Departamento.objects.get(id=id)

            ast = Departamento.objects.all().values().order_by("nombre_departamento")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                'ast' : ast
            }

            return render(request, 'form_actualizar_departamento.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        ast = Departamento.objects.all().values().order_by("nombre_departamento")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ast':ast,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)


def registrarDepartamento(request):
    if request.method == "POST":
        dep = request.POST["txtdep"].upper()

        comprobarDepartamento = Departamento.objects.filter(nombre_departamento=dep)
        if comprobarDepartamento:

            ast = Departamento.objects.all().values().order_by("nombre_departamento")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ast' : ast,
                'r2' : 'El Departamento ('+dep.upper()+') Ya Existe!!'
            }
            return render(request, 'form_registrar_buque.html', datos)

        else:
            
            # se registra el nuevo estilo.
            ast = Departamento(nombre_departamento=dep)
            ast.save()


            # se recuperan todos los estilos para listarlos.
            ast = Departamento.objects.all().values().order_by("nombre_departamento")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ast' : ast,
                'r' : 'Departamento ('+dep+') Registrado Correctamente!!'
            }

            return render(request, 'form_registrar_buque.html', datos)

    else:

        ast = Departamento.objects.all().values()

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ast' : ast,
            'r2' : 'Debe Presionar El Botón Para Registrar El Departamento!!'
        }

        return render(request, 'form_registrar_buque.html', datos)



def actualizarDepartamento(request, id):
    try:
        dep = request.POST['txtdep'].upper()

        ast = Departamento.objects.get(id=id)
        ast.nombre_departamento = dep
        ast.save()



        ast = Departamento.objects.all().values().order_by("nombre_departamento")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ast' : ast, 
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)

    except:
        
        ast = Departamento.objects.all().values().order_by("nombre_departamento")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ast' : ast,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def eliminarDepartamento(request, id):
    try:
        
        ast = Departamento.objects.get(id=id)
        nom = ast.nombre_departamento
        ast.delete()


        ast = Departamento.objects.all().values().order_by("nombre_departamento")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ast':ast,
            'r' : "Departamento Eliminado Correctamente!!"
        }

        return render(request, "form_registrar_buque.html", datos)

    except:

        ast = Departamento.objects.all().values().order_by("nombre_departamento")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ast':ast,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar el Departamento!!"
        }

        return render(request, 'form_registrar_buque.html', datos)


# ---------------------------------------------------------------------------------------------------------------


def mostrarFormActualizarSistema(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Sistema.objects.get(id=id)

            ost = Sistema.objects.all().values().order_by("nombre_sistema")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                'ost' : ost
            }

            return render(request, 'form_actualizar_sistema.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        ost = Sistema.objects.all().values().order_by("nombre_sistema")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ost':ost,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)


def registrarSistema(request):
    if request.method == "POST":
        sis = request.POST["txtsis"].upper()

        comprobarSistema = Sistema.objects.filter(nombre_sistema=sis)
        if comprobarSistema:

            ost = Sistema.objects.all().values().order_by("nombre_sistema")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ost' : ost,
                'r2' : 'El Sistema ('+sis.upper()+') Ya Existe!!'
            }
            return render(request, 'form_registrar_buque.html', datos)

        else:
            
            # se registra el nuevo estilo.
            ost = Sistema(nombre_sistema=sis)
            ost.save()


            # se recuperan todos los estilos para listarlos.
            ost = Sistema.objects.all().values().order_by("nombre_sistema")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ost' : ost,
                'r' : '('+sis+') Registrado Correctamente!!'
            }

            return render(request, 'form_registrar_buque.html', datos)

    else:

        ost = Sistema.objects.all().values()

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ost' : ost,
            'r2' : 'Debe Presionar El Botón Para Registrar El Sistema!!'
        }

        return render(request, 'form_registrar_buque.html', datos)




def actualizarSistema(request, id):
    try:
        sis = request.POST['txtsis'].upper()

        ost = Sistema.objects.get(id=id)
        ost.nombre_sistema = sis
        ost.save()



        ost = Sistema.objects.all().values().order_by("nombre_sistema")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ost' : ost, 
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)

    except:
        
        ost = Sistema.objects.all().values().order_by("nombre_sistema")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ost' : ost,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def eliminarSistema(request, id):
    try:
        
        ost = Sistema.objects.get(id=id)
        nom = ost.nombre_sistema
        ost.delete()


        ost = Sistema.objects.all().values().order_by("nombre_sistema")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ost':ost,
            'r' : "Sistema Eliminado Correctamente!!"
        }

        return render(request, "form_registrar_buque.html", datos)

    except:

        ost = Sistema.objects.all().values().order_by("nombre_sistema")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ost':ost,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar el Departamento!!"
        }

        return render(request, 'form_registrar_buque.html', datos)



# -------------------------------------------------------------------------------------




def mostrarFormActualizarEquipo(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Equipo.objects.get(id=id)

            ust = Equipo.objects.all().values().order_by("nombre_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                'ust' : ust
            }

            return render(request, 'form_actualizar_equipo.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        ust = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ust':ust,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def registrarEquipo(request):
    if request.method == "POST":
        equ = request.POST["txtequ"].upper()
        sta = request.POST["numsta"]

        comprobarEquipo = Equipo.objects.filter(nombre_equipo=equ,hora_standar=sta)
        if comprobarEquipo:

            ust = Equipo.objects.all().values().order_by("nombre_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ust' : ust,
                'r2' : 'El Equipo ('+equ.upper()+') Ya Existe!!'
            }
            return render(request, 'form_registrar_buque.html', datos)

        else:
            
            # se registra el nuevo estilo.
            ust = Equipo(nombre_equipo=equ,hora_standar=sta)
            ust.save()


            # se recuperan todos los estilos para listarlos.
            ust = Equipo.objects.all().values().order_by("nombre_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ust' : ust,
                'r' : 'Equipo ('+equ+') Registrado Correctamente!!'
            }

            return render(request, 'form_registrar_buque.html', datos)

    else:

        ust = Equipo.objects.all().values()

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ust' : ust,
            'r2' : 'Debe Presionar El Botón Para Registrar El equipo!!'
        }

        return render(request, 'form_registrar_buque.html', datos)




def actualizarEquipo(request, id):
    try:
        equ = request.POST['txtequ'].upper()
        sta = request.POST['numsta']

        ust = Equipo.objects.get(id=id)
        ust.nombre_equipo = equ
        ust.hora_standar = sta
        ust.save()



        ust = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ust' : ust, 
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)

    except:
        
        ust = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ust' : ust,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)



def eliminarEquipo(request, id):
    try:
        
        ust = Equipo.objects.get(id=id)
        nom = ust.nombre_equipo
        ust.delete()


        ust = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ust':ust,
            'r' : "Equipo Eliminado Correctamente!!"
        }

        return render(request, "form_registrar_buque.html", datos)

    except:

        ust = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ust':ust,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar el Equipo!!"
        }

        return render(request, 'form_registrar_buque.html', datos)   




#------------------------------------------------------------------------------------------------------------------

def mostrarFormActualizarEquipos(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Equipos.objects.get(id=id)

            ist = Equipos.objects.all().values().order_by("nom_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                'ist' : ist
            }

            return render(request, 'form_actualizar_equipos.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        ist = Equipos.objects.all().values().order_by("nom_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ist':ist,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)




def registrarEquipos(request):
    if request.method == "POST":
        equi = request.POST["txtequi"].upper()
        

        comprobarEquipos = Equipos.objects.filter(nom_equipo=equi)
        if comprobarEquipos:

            ist = Equipos.objects.all().values().order_by("nom_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ist' : ist,
                'r2' : 'El Equipo ('+equ.upper()+') Ya Existe!!'
            }
            return render(request, 'form_registrar_buque.html', datos)

        else:
            
            # se registra el nuevo estilo.
            ist = Equipos(nom_equipo=equi)
            ist.save()


            # se recuperan todos los estilos para listarlos.
            ist = Equipos.objects.all().values().order_by("nom_equipo")

            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'ist' : ist,
                'r' : 'Equipos ('+equi+') Registrado Correctamente!!'
            }

            return render(request, 'form_registrar_buque.html', datos)

    else:

        ist = Equipos.objects.all().values()

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ist' : ist,
            'r2' : 'Debe Presionar El Botón Para Registrar El equipo!!'
        }

        return render(request, 'form_registrar_buque.html', datos)



def actualizarEquipos(request, id):
    try:
        equi = request.POST['txtequi'].upper()

        ist = Equipos.objects.get(id=id)
        ist.nom_equipo = equi
        ist.save()



        ist = Equipos.objects.all().values().order_by("nom_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ist' : ist, 
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)

    except:
        
        ist = Equipos.objects.all().values().order_by("nom_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'ist' : ist,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'form_registrar_buque.html', datos)


def eliminarEquipos(request, id):
    try:
        
        ist = Equipos.objects.get(id=id)
        ist.delete()


        ist = Equipos.objects.all().values().order_by("nom_equipo")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ist': ist,
            'r' : "Equipo Eliminado Correctamente!!"
        }

        return render(request, "form_registrar_buque.html", datos)

    except:

        ist = Equipos.objects.all().values().order_by("nom_equipo")

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'ist':ist,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar el Equipo!!"
        }

        return render(request, 'form_registrar_buque.html', datos)

#-------------------------------------------------------------------------------------------------------------------


def mostrarFormRegistrarRegistro(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipo = Equipo.objects.all().values().order_by("nombre_equipo")

            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'opcionesBuque' : opcionesBuque,  
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipo' : opcionesEquipo,
            }

            return render(request, 'form_registrar_registro.html', datos)
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



def registrarRegistro(request):
    if request.method == "POST":
        buq = request.POST["cbobuq"]
        dep = request.POST["cbodep"]
        sis = request.POST["cbosis"]
        equ = request.POST["cboequ"]  
        des = request.POST["txtdes"]
        pri = request.POST["cbopri"]
        ult = request.POST["dateult"]
        hor = request.POST["numhor"]
        com = request.POST["txtcom"]
        eje = request.POST["cboeje"]

  
        reg = Registro(buque_id=buq, departamento_id=dep, sistema_id=sis, equipo_id=equ, 
        nombre_texto=des, nombre_prioridad=pri, ultimo_mantenimiento=ult, ultimo_horometro=hor, 
        comentario=com, estado_ejecucion=eje)
        reg.save()
    
        opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
        opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
        opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
        opcionesEquipo = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'opcionesBuque' : opcionesBuque,  
            'opcionesDepartamento' : opcionesDepartamento,
            'opcionesSistema' : opcionesSistema,
            'opcionesEquipo' : opcionesEquipo,              
            'r' : 'Datos Registrados Correctamente!!'
        }

        return render(request, 'form_registrar_registro.html', datos)

    else:

        opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
        opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
        opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
        opcionesEquipo = Equipo.objects.all().values().order_by("nombre_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'opcionesBuque' : opcionesBuque,  
            'opcionesDepartamento' : opcionesDepartamento,
            'opcionesSistema' : opcionesSistema,
            'opcionesEquipo' : opcionesEquipo,               
            'r2' : 'Debe Presionar El Botón Para Agregar El Registro!!'
        }

        return render(request, 'form_registrar_registro.html', datos)



def mostrarFormActualizarRegistro(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Registro.objects.get(id=id)

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipo = Equipo.objects.all().values().order_by("nombre_equipo")


            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado,
                
                'opcionesBuque' : opcionesBuque,
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipo' : opcionesEquipo
            }

            return render(request, 'form_actualizar_registro.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        pan = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'pan ' : pan ,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'menu_principal.html', datos)



def mostrarUsuarioActualizarRegistro(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrado = Registro.objects.get(id=id)

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipo = Equipo.objects.all().values().order_by("nombre_equipo")


            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrado' : encontrado, 
                'opcionesBuque' : opcionesBuque,
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipo' : opcionesEquipo
            }

            return render(request, 'usuario_actualizar_registro.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        pan = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'pan ' : pan ,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'menu_usuario.html', datos)



def actualizarRegistro(request, id):

    try:
        buq = request.POST["cbobuq"]
        dep = request.POST["cbodep"]
        sis = request.POST["cbosis"]
        equ = request.POST["cboequ"] 
        des = request.POST["txtdes"]
        pri = request.POST["cbopri"]
        ult = request.POST["dateult"]
        hor = request.POST["numhor"]
        com = request.POST["txtcom"]
        eje = request.POST["cboeje"]
        
        


        registros = Registro.objects.get(id=id)
        registros.buque_id = buq
        registros.departamento_id = dep
        registros.sistema_id = sis
        registros.equipo_id = equ
        registros.nombre_texto = des
        registros.nombre_prioridad = pri
        registros.ultimo_mantenimiento = ult
        registros.ultimo_horometro = hor
        registros.comentario = com
        registros.estado_ejecucion = eje
        registros.save()


        # se registra en la tabla historial.
        nom_buq = ""+buq.lower()+""
        nom_dep = ""+dep.lower()+""
        nom_sis = ""+sis.lower()+""
        nom_equ = ""+equ.lower()+""
        descripcion = ""+des.lower()+""
        ultimo_horometro = ""+hor.lower()+""
        fechayhora = datetime.datetime.now()
        his = Historial(buque_id=nom_buq, departamento_id=nom_dep, sistema_id=nom_sis, equipo_id=nom_equ,
        descripcion_historial=descripcion, registro_horometro=ultimo_horometro, fecha_hora_historial=fechayhora)
        his.save()



        registros = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        registros = Registro.objects.select_related('buque').all()

            # Calcular el estado para cada registro
        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"

        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo  

        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo                        

        for sig in registros:
                proxi_man = sig.ultimo_horometro + sig.equipo.hora_standar

                pro.siguiente = proxi_man

                
        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'Menu_principal.html', datos)

    except:
        
        registros = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()
        
        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,    
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'Menu_principal', datos)



def actualizarRegistroUsuario(request, id):
    try: 
        pri = request.POST["cbopri"]
        ult = request.POST["dateult"]
        hor = request.POST["numhor"]
        com = request.POST["txtcom"]
        eje = request.POST["cboeje"]

        
        
        registros = Registro.objects.get(id=id)
        registros.nombre_prioridad = pri
        registros.ultimo_mantenimiento = ult
        registros.ultimo_horometro = hor
        registros.comentario = com
        registros.estado_ejecucion = eje
        registros.save()

    
        registros = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        registros = Registro.objects.select_related('buque').all()

            # Calcular el estado para cada registro
        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"

        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo 


        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo                       

        for sig in registros:
                proxi_man = sig.ultimo_horometro + sig.equipo.hora_standar

                pro.siguiente = proxi_man

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'Menu_usuario.html', datos)

    except:
        
        registros = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()
        
        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,    
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'Menu_usuario', datos)



def eliminarRegistro(request, id):
    try:
        
        registros = Registro.objects.get(id=id)
        registros.delete()



        registros  = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"


        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo   


        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo   


        for sig in registros:
                proxi_man = sig.ultimo_horometro + sig.equipo.hora_standar

                pro.siguiente = proxi_man                              

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r' : "Registro Eliminado Correctamente!!"
        }

        return render(request, "menu_principal.html", datos)

    except:

        registros = Registro.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar Pintura!!"
        }

        return render(request, 'menu_principal.html', datos)



#------------------------------------------------------------------------------------------------------------------


def mostrarFormRegistrarFecha(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "":

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipos = Equipos.objects.all().values().order_by("nom_equipo")

            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'opcionesBuque' : opcionesBuque,  
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipos' : opcionesEquipos,
            }

            return render(request, 'form_registrar_fecha.html', datos)
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



def registrarFecha(request):
    if request.method == "POST":
        buq = request.POST["cbobuq"]
        dep = request.POST["cbodep"]
        sis = request.POST["cbosis"]
        equi = request.POST["cboequi"]  
        act = request.POST["txtact"]
        prio = request.POST["cboprio"]
        ulti = request.POST["dateulti"]
        come = request.POST["txtcome"]
        ejec = request.POST["cboejec"]
        fre = request.POST["numfre"]



        
        fec = Fecha(buque_id=buq, departamento_id=dep, sistema_id=sis, equipos_id=equi, 
        actividad=act, prioridad=prio, ult_mantenimiento=ulti, 
        texto_comentario=come, ejecucion=ejec, frecuencia=fre)
        fec.save()

        
        opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
        opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
        opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
        opcionesEquipos = Equipos.objects.all().values().order_by("nom_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'opcionesBuque' : opcionesBuque,  
            'opcionesDepartamento' : opcionesDepartamento,
            'opcionesSistema' : opcionesSistema,
            'opcionesEquipos' : opcionesEquipos,              
            'r' : 'Datos Registrados Correctamente!!'
        }

        return render(request, 'form_registrar_fecha.html', datos)

    else:

        opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
        opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
        opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
        opcionesEquipos = Equipos.objects.all().values().order_by("nom_equipo")

        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'opcionesBuque' : opcionesBuque,  
            'opcionesDepartamento' : opcionesDepartamento,
            'opcionesSistema' : opcionesSistema,
            'opcionesEquipos' : opcionesEquipos,               
            'r2' : 'Debe Presionar El Botón Para Registrar El Dato Nuevo!!'
        }

        return render(request, 'form_registrar_fecha.html', datos)



def mostrarFormActualizarFecha(request, id):

    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontrados = Fecha.objects.get(id=id)

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipos = Equipos.objects.all().values().order_by("nom_equipo")


            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontrados' : encontrados,
                'opcionesBuque' : opcionesBuque,
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipos' : opcionesEquipos
            }

            return render(request, 'form_actualizar_fecha.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        fechas = Fecha.objects.select_related('buque').all()
        pun = Fecha.objects.select_related('departamento').all()
        pin = Fecha.objects.select_related('sistema').all()
        pon = Fecha.objects.select_related('equipo').all()


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas ' : fechas ,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'menu_principal.html', datos)



def mostrarUsuarioActualizarFecha(request, id):

    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:

            encontradoss = Fecha.objects.get(id=id)

            opcionesBuque = Buque.objects.all().values().order_by("nombre_buque")
            opcionesDepartamento = Departamento.objects.all().values().order_by("nombre_departamento")
            opcionesSistema = Sistema.objects.all().values().order_by("nombre_sistema")
            opcionesEquipos = Equipos.objects.all().values().order_by("nom_equipo")


            datos = { 
                'nomUsuario' : request.session["nomUsuario"],
                'encontradoss' : encontradoss,
                'opcionesBuque' : opcionesBuque,
                'opcionesDepartamento' : opcionesDepartamento,
                'opcionesSistema' : opcionesSistema,
                'opcionesEquipos' : opcionesEquipos
            }

            return render(request, 'usuario_actualizar_fecha.html', datos)

        else:

            datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'index.html', datos)

    except:

        fechas = Fecha.objects.select_related('buque').all()
        pun = Fecha.objects.select_related('departamento').all()
        pin = Fecha.objects.select_related('sistema').all()
        pon = Fecha.objects.select_related('equipo').all()


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas ' : fechas ,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2':"El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'menu_usuario.html', datos)



def actualizarFecha(request, id):
    try:
        buq = request.POST["cbobuq"]
        dep = request.POST["cbodep"]
        sis = request.POST["cbosis"]
        equi = request.POST["cboequi"]  
        act = request.POST["txtact"]
        prio = request.POST["cboprio"]
        ulti = request.POST["dateulti"]
        come = request.POST["txtcome"]
        ejec = request.POST["cboejec"]
        fre = request.POST["numfre"]
        
        


        fechas = Fecha.objects.get(id=id)
        fechas.buque_id = buq
        fechas.departamento_id = dep
        fechas.sistema_id = sis
        fechas.equipos_id = equi
        fechas.actividad = act
        fechas.prioridad = prio
        fechas.ult_mantenimiento = ulti
        fechas.texto_comentario = come
        fechas.ejecucion = ejec
        fechas.frecuencia = fre
        fechas.save()


        nom_buq = ""+buq.lower()+""
        nom_dep = ""+dep.lower()+""
        nom_sis = ""+sis.lower()+""
        nom_equi = ""+equi.lower()+""
        descripcion = ""+act.lower()+""
        frecu = ""+fre.lower()+""
        fecha = datetime.datetime.now()
        hist = HistorialCal(buque_id=nom_buq, departamento_id=nom_dep, sistema_id=nom_sis, equipo_id=nom_equi,
        descripcion_actividad=descripcion, descripcion_frecuencia=frecu, fecha_historial=fecha)
        hist.save()
    

        fechas = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        registros = Registro.objects.select_related('buque').all()

            # Calcular el estado para cada registro
        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"

        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo      


        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo        


        for fec in fechas:

                actual = datetime.date.today()
                numero = fec.frecuencia
                formula1 = fec.ult_mantenimiento + datetime.timedelta(days=numero)
                dias_faltantes = (formula1 - actual).days
                status = fec.frecuencia / 5

                fec.resultado = formula1

                fec.dias = dias_faltantes


                if dias_faltantes < 0:
                    fec.categoria = "VENCIDO"
                elif dias_faltantes <= status:
                    fec.categoria = "POR VENCER"
                else: 
                    fec.categoria = "OK"                      


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'registros' : registros,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'calendario_admin.html', datos)

    except:
        
        fechas = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()
        
        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'pun' : pun,
            'pin' : pin,    
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'calendario_admin', datos)



def actualizarFechaUsuario(request, id):
    try:
        prio = request.POST["cboprio"]
        ulti = request.POST["dateulti"]
        come = request.POST["txtcome"]
        ejec = request.POST["cboejec"]
        

        fechas = Fecha.objects.get(id=id)
        fechas.prioridad = prio
        fechas.ult_mantenimiento = ulti
        fechas.texto_comentario = come
        fechas.ejecucion = ejec
        fechas.save()


        fechas = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()


        registros = Registro.objects.select_related('buque').all()

            # Calcular el estado para cada registro
        for reg in registros:
                suma_horas = reg.equipo.hora_standar + reg.ultimo_horometro
                horas_acum = reg.buque.horometro - reg.ultimo_horometro
                resultado = reg.equipo.hora_standar - horas_acum
                stats = reg.equipo.hora_standar / 10

                # Determinar el estado
                if suma_horas < reg.buque.horometro:
                    reg.estado = "VENCIDO"
                elif  resultado <= stats :
                    reg.estado = "POR VENCER"
                else:
                    reg.estado = "OK"

        for pro in registros:
                prox_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horo = pro.buque.horometro

                if prox_man >= horo:
                    pro.proximo = prox_man
                else:
                    pro.proximo = horo      


        for sig in registros:

                pro_man = pro.ultimo_horometro + pro.equipo.hora_standar
                horas = pro_man - sig.buque.horometro 

                proximo = sig.ultimo_mantenimiento + datetime.timedelta(hours=horas)

                ahora = datetime.datetime.now()

                fecha_actual = ahora.strftime("%d/%m/%Y")

                if proximo <= sig.ultimo_mantenimiento:
                    sig.proxima_fecha = fecha_actual

                else:    
                    sig.proxima_fecha = proximo  



        for fec in fechas:

                actual = datetime.date.today()
                numero = fec.frecuencia
                formula1 = fec.ult_mantenimiento + datetime.timedelta(days=numero)
                dias_faltantes = (formula1 - actual).days
                status = fec.frecuencia / 5

                fec.resultado = formula1

                fec.dias = dias_faltantes


                if dias_faltantes < 0:
                    fec.categoria = "VENCIDO"
                elif dias_faltantes <= status:
                    fec.categoria = "POR VENCER"
                else: 
                    fec.categoria = "OK"                          


        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r':"Datos Modificados Correctamente!!"         
        }

        return render(request, 'calendario_usuario.html', datos)

    except:
        
        fechas = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()
        
        datos = { 
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'pun' : pun,
            'pin' : pin,    
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Actualizar!!"         
        }

        return render(request, 'calendario_usuario', datos)



def eliminarFecha(request, id):
    try:
        
        fechas = Fecha.objects.get(id=id)
        fechas.delete()



        fechas  = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()

        for fec in fechas:

                numero = fec.frecuencia
                formula1 = fec.ult_mantenimiento + datetime.timedelta(days=numero)


                fec.resultado = formula1.strftime('%d/%B/%Y')   

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r' : "Registro Eliminado Correctamente!!"
        }

        return render(request, "calendario_admin.html", datos)

    except:

        fechas = Fecha.objects.select_related('buque').all()
        pun = Registro.objects.select_related('departamento').all()
        pin = Registro.objects.select_related('sistema').all()
        pon = Registro.objects.select_related('equipo').all()

        datos = {
            'nomUsuario' : request.session["nomUsuario"],
            'fechas' : fechas,
            'pun' : pun,
            'pin' : pin,
            'pon' : pon,
            'r2' : "El ID ("+str(id)+") No Existe. Imposible Eliminar Pintura!!"
        }

        return render(request, 'calendario_admin.html', datos)



#-------------------------------------------------------------------------------------------------------------------------


def mostrarListarHistorial(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() == "ADMIN":

            his = Historial.objects.select_related('buque').all().order_by("fecha_hora_historial")
            
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'his' : his
            }

            return render(request, 'historial_admin.html', datos)
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)




def mostrarListarHistorialCalendario(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() == "ADMIN":

            hist = HistorialCal.objects.select_related('buque').all().order_by("fecha_historial")
            
            datos = {
                'nomUsuario' : request.session["nomUsuario"],
                'hist' : hist
            }

            return render(request, 'historial_calendario.html', datos)
            
        else:

            datos = { 'r' : 'No Tiene Privilegios Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
            
    else:
        datos = { 'r' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)
#----------------------------------------------------------------------------------------------------------------



# Create your views here.
