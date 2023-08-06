
import os
from log_manager import logging
log = logging.getLogger('core.GlobalConfigLoader')
from pathlib import Path
import yaml
import argparse
from utils import flat_dict_to_nested_dict_with_array, nested_dict_to_flat_dict_with_array, copy_merge_recursive_dict, valuate_dict_with_context
from config import Config
import json

class GlobalConfigFactory():
    """
    Recherche et charge les differents elements contribuant a la configuration global
    """
    @staticmethod
    def load_global_config(lib_path, client_path):
        """
        Charge et merge les fichiers de configurations
        :param lib_path: chemin global vers les sources du framwork
        :param client_path: chemin global vers le dossier de surcharge spcifique
        :return: un objet Config avec tous les elements
        """
        result_config = Config()
        result_config.config = {}
        log.debut('Chargement des configurations')
        for path in [lib_path, client_path]:
            path = path + '/config'
            for file in os.listdir(path):
                file_path = path + "/" + file
                node_name = Path(file).stem
                if node_name in result_config.config:
                    # La config cote lib sert de valeur par defaut
                    result_config.config[node_name] = copy_merge_recursive_dict(defaut=result_config.config[node_name], source=yaml.load(open(file_path), Loader=yaml.Loader))
                else:
                    result_config.config[node_name] = yaml.load(open(file_path), Loader=yaml.Loader)

        """
           Ajout parametres calcules
        """
        result_config.config['lib_path'] = lib_path
        result_config.config['client_path'] = client_path
        result_config.config['client_name'] = os.path.basename(client_path)

        result_config.flat_config = nested_dict_to_flat_dict_with_array(separator='::', input=result_config.config)
        """
           Surcharge par ligne de commande
        """
        if 'arguments' in result_config.config:
            def bool(value):
                return value == 'True' or value == 'true'

            def str_list(value):
                return value.replace('  ', '').replace(' ,', ',').replace(', ', ',').split(',')

            def str_json(value):
                return json.loads(value)

            arg_type = {
                'str': str,
                'int': int,
                'file': file,
                'bool': bool,
                'str_list': str_list,
                'str_json': str_json
            }

            parser = argparse.ArgumentParser(description=result_config.config.get('arguments').get('title'))
            arguments = list(result_config.config.get('arguments').get('parameters').items())
            for name, arg in arguments:
                argument_key = '-{}'.format(name)
                if len(name) > 1:
                    argument_key = '--{}'.format(name)
                if arg.get('type') == 'store_true' or arg.get('type') == 'store_false':
                    parser.add_argument(argument_key, action=arg.get('type'), help=arg.get('help', ''))
                else:
                    parser.add_argument(argument_key, type=arg_type.get(arg.get('type'), str), help=arg.get('help', ''))
            args = parser.parse_args()
            # Valuation de la config par les arguments
            # La valeur des arguments surcharge la config
            for name, arg in arguments:
                exist = True
                val = None
                val=getattr(args, name)
                if not val is None:
                    log.debug(name + ' detecte en argument', val=val)
                    if isinstance(val, dict):
                        # Gestion des valeurs de type dict
                        # On considere le dict comme un ensemble de sous valeurs
                        # Ceci permet de merger le dict passe en arg avec le dict present dans la config
                        nval = nested_dict_to_flat_dict_with_array(separator='::', input=val)
                        for k,v in list(nval.items()):
                            cle_config = "{}::{}".format(arg['config_name'], k)
                            result_config.flat_config[cle_config] = v
                    else:
                        # Gestion des valeurs de type simple
                        result_config.flat_config[arg['config_name']] = val
            result_config.config = flat_dict_to_nested_dict_with_array(separator='::', flat_dict=result_config.flat_config)

        """
            Surcharge de la config par les emplacements annexe
        """
        for path in result_config.get('core::other_conf_dirs', []):
            for file in os.listdir(path):
                file_path = path + "/" + file
                node_name = Path(file).stem
                if node_name in result_config.config:
                    # La config cote lib sert de valeur par defaut
                    result_config.config[node_name] = copy_merge_recursive_dict(defaut=result_config.config[node_name], source=yaml.load(open(file_path), Loader=yaml.Loader))
                else:
                    result_config.config[node_name] = yaml.load(open(file_path), Loader=yaml.Loader)

        result_config.config = valuate_dict_with_context(
            dict_input=result_config.config,
            context=result_config.config
        )


        """
            Calcul de chemins absolu
        """
        list_paths = list(set(result_config.get_node('testcase').get_node('base_path').config))
        netlist = []
        for lpath in list_paths:
            if not os.path.isabs(lpath):
                lpath = os.path.join(os.getcwd(), lpath)
                if not os.path.exists(lpath):
                    lpath = os.path.join(result_config.config['client_path'], lpath)
                    if not os.path.exists(lpath):
                        lpath = os.path.join(result_config.config['lib_path'], lpath)
                        if not os.path.exists(lpath):
                            log.warn("Chemin testcase {} introuvable".format(lpath))
            netlist.append(os.path.abspath(lpath))

        if len(netlist) == 0:
            raise Exception("Aucun chemin testcase n'existe dans {}".format(','.join(list_paths)))
        result_config.config['testcase']['base_path'] = netlist
        result_config.flat_config = nested_dict_to_flat_dict_with_array(separator='::', input=result_config.config)

        log.fin('Chargement des configurations')

        if result_config.get('core::show_config', False):
            print('--------------- show_config  ---------------')
            print('- Configuration chargee -')
            print('---')
            print(yaml.dump(result_config.config))
            print('--------------- ------------ ---------------')

        return result_config
