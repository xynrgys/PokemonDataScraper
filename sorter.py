import os
import shutil
import re

#path to folder
folder_path = '/Users/syn/PycharmProjects/pythonProject2'

os.chdir(folder_path)

for f in os.listdir('pokemons_images'):
    sandwich = '_'
    result = f.rsplit(sandwich, 0)[-1].split(sandwich)[1]
    print(f)
    if not os.path.exists(folder_path + '/pokemon/' + result):
        os.mkdir(folder_path + '/pokemon/' + result)
        shutil.copy(os.path.join("pokemons_images", f), folder_path + '/pokemon/' + result)
    else:
        shutil.copy(os.path.join("pokemons_images", f), folder_path + '/pokemon/' + result)