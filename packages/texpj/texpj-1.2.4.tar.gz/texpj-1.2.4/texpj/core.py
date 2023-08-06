#!/usr/bin/env python3
import click
import os
import platform
import json
import shutil
from os.path import abspath, expanduser, normpath, exists

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
config = dict()


def choose(win, unix):
    return win if platform.system() == 'Windows' else unix


def texpath():
    return abspath(expanduser(f"{config['path']}/texpj-template"))


def destroyTemplate(dir):
    if not os.path.isdir(dir):
        os.remove(dir)
        return

    if dir[-1] == os.sep:
        dir = dir[:-1]
    files = os.listdir(dir)
    for file in files:
        if file == '.' or file == '..':
            continue
        path = dir + os.sep + file
        if os.path.isdir(path):
            destroyTemplate(path)
        else:
            os.unlink(path)
    os.rmdir(dir)


def copytree(src, dst, symlinks=False, ignore=None, exclude=['.git']):
    for item in os.listdir(src):
        if item in exclude:
            continue
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


LN = choose('mklink /D', 'ln -s')


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Utilidad para manejo de plantillas de latex por consola.

    Utilice:

    \b\033[32m
    $ texpj comando -h
    \033[0m

    Para obtener una mayor información sobre el comando.
    """
    global config

    config['path'] = choose('c:\\data\\documents', '~/Documents')

    pconf = f"{click.get_app_dir('texpj')}/config.json"

    if not exists(pconf):
        print('Como primer paso complete la configuración')
        print(
            '\n\tPuede consultar las configuraciones',
            f'en {click.get_app_dir("texpj")}/config.json')
        print()
        print(
            'En el directorio ingresado se',
            'creará el directorio "texpj-template"')
        response = config['path']
        while True:
            response = input(f'Directorio (default {config["path"]}): ')
            if not response.strip() and exists(expanduser(config['path'])):
                break
            if exists(abspath(expanduser(response))):
                config['path'] = normpath(response)
                if not exists(texpath()):
                    os.mkdir(f"{texpath()}")
                break
            print(f'El directorio {response} no existe!')

        if not exists(click.get_app_dir('texpj')):
            os.mkdir(click.get_app_dir('texpj'))

        with open(pconf, 'w') as fconf:
            json.dump(config, fconf, indent=2)

    with open(pconf, 'r') as fconf:
        config = json.load(fconf)


@main.command()
@click.argument('alias')
def update(alias):
    """
    Actualiza el template identificado con el ALIAS.
    """
    print(f"cd {texpath()}/{alias}")
    print("git pull")
    os.system(f"cd {texpath()}/{alias}; git pull")


def wdescription(path, description):
    with open(f"{path}/.description.texpj", 'w') as f:
        f.write(description)


def rdescription(path):
    content = ''

    if exists(f"{path}/.description.texpj"):
        with open(f"{path}/.description.texpj", 'r') as f:
            content = f.read()

    if len(content.strip()) == 0:
        content = 'sin descripción'
    return content


@main.command()
@click.argument('directory')
@click.argument('alias')
@click.argument('description', required=False)
def add(directory, alias, description):
    """
    Registra DIRECTORY como una plantilla de latex y lo identifica con ALIAS.

    \b
    \033[32m
    $ texpj add . elec_doc 'Reporte para electro'
    $ texpj add reporte report 'Reporte para electro'
    \033[0m
    """

    if exists(f"{texpath()}/{alias}"):
        print("ERROR: los alias deben únicos")
        return

    print(f"{LN} {abspath(expanduser(directory))} {texpath()}/{alias}")
    os.system(f"{LN} {abspath(expanduser(directory))} {texpath()}/{alias}")
    wdescription(
        f"{texpath()}/{alias}", '' if description is None else description)


@main.command()
@click.argument('template')
@click.argument('alias')
@click.argument('description', required=False)
@click.option('--url/--no-url', default=False, help="indica si es un url")
def install(template, alias, description, url):
    """
    Instala el TEMPLATE de forma local y lo regitra como ALIAS.

    Descarga un repositorio con el comando git.
    'user/repo-name' bastará si es un repositorio de Github sino
    puede utilizar un url activando la opción --url.

    \b
    Ejemplo:
    \033[32m
    $ texpj install BenyaminGaleano/report 'Reporte ...'
    $ texpj install https://github.com/BenyaminGaleano/report.git 'desc' --url
    \033[0m
    """

    if exists(f"{texpath()}/{alias}"):
        print("ERROR: los alias deben únicos")
        return

    if url:
        print(f"git clone {template} {texpath()}/{alias}")
        os.system(f"git clone {template} {texpath()}/{alias}")
    else:
        print(
            f"git clone https://github.com/{template}.git {texpath()}/{alias}")
        os.system(
            f"git clone https://github.com/{template}.git {texpath()}/{alias}")

    wdescription(
        f"{texpath()}/{alias}", '' if description is None else description)


@main.command()
@click.argument('alias')
def remove(alias):
    """
    Elimina la plantilla identificada como ALIAS,
    si es un enlace simbólico, no elimina
    el contenido (si fue agregado con texpj add ...).
    """
    if alias is None:
        return

    destroyTemplate(f"{texpath()}/{alias}")


@main.command()
def list():
    """
    Lista todas las posibles plantillas guardadas.
    """
    print("Plantillas en el directorio:")
    for template in os.listdir(texpath()):
        if not os.path.isdir(f"{texpath()}/{template}"):
            continue
        print(f' {template:20}', rdescription(f"{texpath()}/{template}"))


@main.command()
@click.argument('alias')
@click.argument('description')
def describe(alias, description):
    """
    Cambia la descripción de ALIAS por DESCRIPTION.
    """
    wdescription(f"{texpath()}/{alias}", description)


@main.command()
@click.argument('alias')
@click.argument('name')
@click.option('--directory', '-d', help="directorio base", default="")
def create(alias, name, directory):
    """
    Crea una copia del template registrado como ALIAS en la posición actual
    o en el directorio indicado con -d con el nombre NAME.

    \b\033[32m
    $ texpj create report lab1
    $ texpj create report lab1 -d ~/documentos/latex
    \033[0m
    """
    target = abspath(expanduser(os.path.join(directory, name)))
    print(
        f"copiando {texpath()}/{alias} a {target}")
    if not exists(f"{target}"):
        os.mkdir(f"{target}")
    copytree(f"{texpath()}/{alias}", f"{target}")


@main.command()
@click.argument('files', nargs=-1)
def launch(files):
    """
    Se encarga de abrir los archivos.
    """
    for f in files:
        print(f'Abriendo {f}')
        os.popen(f"open {abspath(expanduser(f))}")


if __name__ == "__main__":
    main()
