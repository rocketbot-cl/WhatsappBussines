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

import json
import sys
import os
import traceback

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

# from whatsapp_business import Whatsapp_auth #pylint: disable=import-error, wrong-import-position, no-name-in-module

global Connection #pylint: disable=invalid-name,global-at-module-level


import os
import requests

class Whatsapp_auth: #pylint: disable=invalid-name
    '''
        Clase Whatsapp
    '''
    def __init__(self, api_key, phone_id):
        self.api_key = "Bearer " + api_key
        self.url = f"https://graph.facebook.com/v15.0/{phone_id}/"
        self.valid = None
        self.get_valid()
        self.headers = {
                "Authorization": self.api_key
            }

    def get_valid(self):
        '''
            Metodo para validar la API Key
        '''
        try:
            url = self.url
            headers = {
                "Authorization": self.api_key
            }
            r = requests.get(url, headers=headers, timeout=30)
            j = r.json()

            if j.get('error'):
                raise Exception(j.get('error').get('message'))
            else:
                self.valid = True


        except Exception as exc:
            raise exc

    def send_message(self, message, phone_number, template=None, code="en_US"):
        '''
            Metodo para enviar mensajes
        '''
        try:
            url = self.url + "messages"
            headers = {
                "Authorization": self.api_key
            }
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                }

            if template:
                data["type"] = "template"
                data["template"] = {
                    "name": template,
                    "language": {
                        "code": code
                    }
                }

            else:
                data["type"] = "text"
                data["text"] = {
                    "body": message
                }

            r = requests.post(url, headers=headers, json=data, timeout=30)
            j = r.json()

            if j.get('error'):
                raise Exception(j.get('error').get('message'))
            else:
                return True

        except Exception as exc:
            raise exc


# Obtengo el modulo que fue invocado
module = GetParams("module")


if module == "conf_whatsapp":
    api_key = GetParams("api_key")
    phone_id = GetParams("phone_id")
    result = GetParams("result")

    try:
        Connection = Whatsapp_auth(api_key, phone_id)

        SetVar(result, Connection.valid)
    except Exception as e:
        SetVar(result, False)
        PrintException()
        raise e

if module == "send_message":
    message = GetParams("message")
    phone_number = GetParams("phone_number")
    full_template = GetParams("template")
    result = GetParams("result")

    try:
        if full_template:
            full_template = full_template.replace(" ", "").split(",")
            template = full_template[0]

            if len(full_template) >= 2:
                code = full_template[1]
        else:
            template = None
            code = None

        send = Connection.send_message(message, phone_number, template, code)

        SetVar(result, send)
    except Exception as e:
        SetVar(result, False)
        traceback.print_exc()
        PrintException()
        raise e
