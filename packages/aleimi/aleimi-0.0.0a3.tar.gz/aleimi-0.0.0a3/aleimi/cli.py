#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aleimi import confgen, boltzmann, extractor, tools, __version__
import argparse
import os

"""
Tengo que adicionar la parte de los comandos extras para pasarselos a exrtractor
para la creacion de los templates, probar con los argumentos que se pasan
si alguno esta mal entonces dlanzar un warning o algo por el estilo
Tengo que ver esto bien, me falta por implemnetar lo fde .gjf
Y lo de el analisis para al menos psi4 y orca
    """

def _aleimi():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        help = "The path were the molecule(s) is(are)",
        dest='suppl',
        type=str)
    parser.add_argument(
        '-p', '--params',
        help = "Parameters to run ALEIMI",
        dest='params',
        type=str)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f"aleimi: {__version__}")

    args = parser.parse_args()

    suppl = args.suppl
    params = args.params
    if not os.path.exists(suppl):
        raise FileNotFoundError(f"{suppl} does not exist or is not accessible.")
    if not os.path.exists(params):
        raise FileNotFoundError(f"{params} does not exist or is not accessible.")



    with open(params,'r') as f:
        lines = f.readlines()

    user_keywords = {}
    for line in lines:
        if not line.startswith('#') and len(line.strip()):
            line = line.split('#')[0]
            index = line.index('=') # Only get the first equal
            key, value = line[:index].replace('-', '_').strip(), line[index+1:].strip()
            user_keywords[key] = value
    user_keys = user_keywords.keys()

    confgen_keywords = tools.get_default_args(confgen.main)
    for key in confgen_keywords.keys():
        if key in user_keys:
            try:
                confgen_keywords[key] = type(confgen_keywords[key])(user_keywords[key]) # Here I  am taking the type of the variable
            except:
                raise ValueError(f"{user_keywords[key]} must be a {type(confgen_keywords[key])}-like")

    mopac_keywords = tools.get_default_args(tools.mopac)
    for key in mopac_keywords.keys():
        if key in user_keys:
            try:
                mopac_keywords[key] = type(mopac_keywords[key])(user_keywords[key]) # Here I  am taking the type of the variable
            except:
                raise ValueError(f"{user_keywords[key]} must be a {type(mopac_keywords[key])}-like")

    boltzmann_keywords = tools.get_default_args(boltzmann.main)
    for key in boltzmann_keywords.keys():
        if key in user_keys:
            try:
                boltzmann_keywords[key] = type(boltzmann_keywords[key])(user_keywords[key]) # Here I  am taking the type of the variable
            except:
                raise ValueError(f"{user_keywords[key]} must be a {type(boltzmann_keywords[key])}-like")

    extractor_keywords = tools.get_default_args(extractor.main)
    for key in extractor_keywords.keys():
        if key in user_keys:
            try:
                extractor_keywords[key] = type(extractor_keywords[key])(user_keywords[key]) # Here I  am taking the type of the variable
            except:
                raise ValueError(f"{user_keywords[key]} must be a {type(extractor_keywords[key])}-like")

    with open('outparams.params', 'w') as f:
        used_keywords = {**confgen_keywords, **mopac_keywords, **boltzmann_keywords, **boltzmann_keywords}
        for key in used_keywords:
            f.write(f"{key:<35} = {used_keywords[key]:<20}\n")

    mol_names = confgen.main(suppl,**confgen_keywords)
    for mol_name in mol_names:
        tools.mopac(f"{mol_name}.mop",**mopac_keywords)
        boltzmann.main(f"{mol_name}.arc",**boltzmann_keywords)
        extractor.main(f"{mol_name}.arc",f"{mol_name}.boltzmann", **boltzmann_keywords)