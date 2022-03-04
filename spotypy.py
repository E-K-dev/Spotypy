import os
from os import *
import spotdl
from spotdl import *
import platform
from platform import (
    python_version,
);
# Vars Global
version = f'1.0';
autor = 'Axel Ezequiel Kampmann';
name = f'''Spotypy Downloader v {version}\n
# By {autor}''';
# End Vars Global Config.

def get__system(): # Obtenemos el sistema operativo.
    if os.name == 'nt' or os.name == 'msdos':
        return 'Windows';

    elif os.name == 'posix':
        return 'Linux';

    else:
        return 'Mac';
        pass

def clean(): # Clean Console Compatible !!.
    if os.name == 'nt' or os.name == 'msdos':
        os.system('cls');
    else:
        os.system('clear');
    pass

def exit__function(): # Funcion para cerrar el script.
    print(f'\n{name}\n\n>> Bye,Bye! . . .\n');
    exit();

def error__if(argument): # Else If with Argument.
    print(f'\n# Opcion ({argument}) invalida , saliendo de la app.\n\n');
    exit__function();

def main(): # Main Function.
    clean();
    menu = f'''{name}

# Requiere python 3.6 o superior.

# Python Version >> ({python_version()}).

# Sistema operativo >> ({get__system()}).

# Selecciona una opcion. #

[a] - Modo compatible con ({get__system()}).

[b] - Ver sistemas compatibles.

[xx] - Salir del script (programa).

'''
    print(menu);
    opciones = str(input('Ingresa una opcion >> ').lower());

    if opciones == 'a':
        wFuncion();

    elif opciones == 'b':
        sistems();
    
    elif opciones == 'xx':
        exit__function();

    else:
        error__if(opciones);

def spotdl__win(extension): # Download Playlist Windows.
    # First part of the function.
    clean();
    menu__3 = f'''{name}
\n# Ingresa tu url de la playlist o cancion a descargar\n'''
    print(menu__3);
    playlist = str(input('Data-or-Url >> '));

    if playlist == '' or playlist == ' ':
        print('\n\nNo ingresaste nada , saliendo . . .\n\n');
        exit__function();
    else:
        pass;
    clean();
    # End First part of the function.

    # Second Part of the function.
    directorio = str('Downloads/'); # Aqui se guardaran las canciones.
    
    if os.path.isdir(directorio): # Creamos el directorio if not exist.
      pass;
    else:
        os.mkdir(directorio); # Crea el directorio.
        pass;

    print(f'Descargando "{playlist}" en "{directorio}" . . .!\n\n');

    os.chdir(directorio); # Change the route ==> (directiory) of work.

    os.system(f'spotdl {playlist} --output-format {extension}');

    print(f'\n\n! Descarga "{playlist}" guardada en "{directorio}" , con exito.\n\n');
    exit__function();
    # End Second Part of function and end Spot__Dl__Windows.

def wFuncion():  # Formato ex .mp3 changer.
    clean(); # Limpiamos la pantalla.

    menu__2 = str(f'''{name}\n
# Selecciona un formato de conversion.

[a] - .MP3.

[b] - .FLAC.

[c] - .WAV.

[d] - .OPUS.

[e] - .M4A.

[xx] - Salir del script (programa).

''');

    print(menu__2);

    ext = str(input('Ingresa una opcion >> ').lower());

    if ext == 'a':
        extension = str('mp3');
        spotdl__win(extension);

    elif ext == 'b':
        extension = str('flac');
        spotdl__win(extension);

    elif ext == 'c':
        extension = str('wav');
        spotdl__win(extension);

    elif ext == 'd':
        extension = str('opus');
        spotdl__win(extension);

    elif ext == 'e':
        extension = str('m4a');
        spotdl__win(extension);

    elif ext == 'xx':
        exit__function();

    else:
        error__if(ext);

def sistems():
    clean();
    print(f'''{name}
# Los sistemas compatibles con este script son #

# Windows.

# Linux.

# Mac.
 
# Userland / Termux.

''');
    exit__function();

main(); # Ejecutamos el main.