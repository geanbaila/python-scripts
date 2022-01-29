import os, string

# Obtener el directorio home del usuario
USER_DIR = os.path.expanduser('~')
print(USER_DIR)

# Obtener el directiro presente
BASE_PATH = os.getcwd()
print(BASE_PATH)

# Obtener el directiro presente
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)

# concatenar un árbol de directorios (path)
PATH = os.path.join(BASE_PATH, 'subdir_1','subdir_2', 'file.txt')
print(PATH)

# Obtener el path del archivo y el nombre del archivo a partir del path
(DIRECTORY_NAME, FILE_NAME) = os.path.split(PATH)
print(DIRECTORY_NAME, FILE_NAME)

# Obtener el nombre del archivo y su extensión 
(FILE, FILE_EXTENSION) = os.path.splitext(FILE_NAME)
print(FILE, FILE_EXTENSION)

# crear/modificar una variable de entorno
os.environ['SUBDIR'] = 'subdir_3'

# Obtener el path habiendo consultado una variable de entorno
SUBDIR = os.path.expandvars(BASE_PATH+'/'+os.environ.get('SUBDIR'))
print(SUBDIR)

# Obtener el path habiendo consultado una variable de entorno
SUBDIR = os.path.expandvars(BASE_PATH+'/'+'$SUBDIR')
print(SUBDIR)

# Obtener los caracteres y digitos disponibles 
CODE_CHARS = string.ascii_uppercase + string.digits
print(CODE_CHARS)