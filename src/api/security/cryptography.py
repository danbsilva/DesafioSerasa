# Para fins de conhecimento essas funcoes foram criadas pelo ChatGPT ###

from flask import request, current_app
import os
import base64


def key():

    return current_app.config['SECRET_KEY']


def encrypt(data):

    KEY = key()

    chave_bytes = KEY.encode('utf-8')
    texto_bytes = data.encode('utf-8')
    texto_cifrado = bytearray()

    for i in range(len(texto_bytes)):
        char = texto_bytes[i] ^ chave_bytes[i % len(chave_bytes)]
        texto_cifrado.append(char)

    texto_cifrado_base64 = base64.b64encode(texto_cifrado)
    return texto_cifrado_base64.decode('utf-8')


def decrypt(data):
    KEY = key()
    chave_bytes = KEY.encode('utf-8')

    texto_cifrado_bytes = base64.b64decode(data)
    texto_decifrado = bytearray()

    for i in range(len(texto_cifrado_bytes)):
        char = texto_cifrado_bytes[i] ^ chave_bytes[i % len(chave_bytes)]
        texto_decifrado.append(char)

    return texto_decifrado.decode('utf-8')