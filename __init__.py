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
import traceback
import json

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable
tmp_global_obj = tmp_global_obj #pylint: disable=undefined-variable,self-assigning-variable


# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #pylint: disable=undefined-variable,self-assigning-variable
whatsapp_directory_path = os.path.join(base_path, "modules", "WhatsappBusiness")
whatsapp_libs_path = os.path.join(whatsapp_directory_path, "libs")

if whatsapp_libs_path not in sys.path:
    sys.path.append(whatsapp_libs_path)

from whatsapp_business import Whatsapp_auth #pylint: disable=import-error, wrong-import-position, no-name-in-module

global wsp_Connection #pylint: disable=invalid-name,global-at-module-level





# Obtengo el modulo que fue invocado
module = GetParams("module")


if module == "conf_whatsapp":
    api_key = GetParams("api_key")
    phone_id = GetParams("phone_id")
    result = GetParams("result")

    try:
        wsp_Connection = Whatsapp_auth(api_key, phone_id)

        SetVar(result, wsp_Connection.valid)
    except Exception as e:
        SetVar(result, False)
        PrintException()
        raise e

if module == "send_message":
    message = GetParams("message")
    phone_number = GetParams("phone_number")
    full_template = GetParams("template")
    result = GetParams("result")
    template_params = GetParams("template_params")
    
    try:
        if full_template:
            full_template = full_template.replace(" ", "").split(",")
            template = full_template[0]

            if len(full_template) >= 2:
                code = full_template[1]
        else:
            template = None
            code = None

        if template_params:
            template_params = json.loads(template_params)

        send = wsp_Connection.send_message(message, phone_number, template, code, template_params)

        SetVar(result, send)
    except Exception as e:
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e
