# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
import os

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable
tmp_global_obj = tmp_global_obj #pylint: disable=undefined-variable,self-assigning-variable


base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'WhatsappBusiness' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)



# Obtengo el modulo que fue invocado
module = GetParams("module")


if module == "conf_whatsapp":
    print("conf_whatsapp")
