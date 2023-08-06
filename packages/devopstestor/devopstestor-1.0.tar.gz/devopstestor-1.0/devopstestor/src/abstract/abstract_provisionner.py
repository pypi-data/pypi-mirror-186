class AbstractProvisionner(object):
    """
    Classe abstraite des provisionners
    Un provisonner permet de controller une machine a travers un outils de deploiement (ex saltstack, ansible)
    """
    def initialise(self, machine_controller, machine_name):
        """
        Initialise le provisioner
        A surcharger si necessaire
        """
        pass


    def get_machine_controller(self):
        """
        A ne pas surcharger
        Retourne le chemin conduisant aux fichiers sur la machine
        """
        return self.machine_controller

    def __init__(self, global_config, machine_controller, machine_name):
        """
        A ne pas surcharger
        Ordonnance l'Initialisation du provisionner
        """
        self.machine_controller = machine_controller
        self.global_config = global_config

        # Initialisation du provisioner
        self.initialise(
            machine_controller=machine_controller,
            machine_name=machine_name
        )

    ## Parametrage utils ###
    def set_max_map_count(self, max_map_count, name="testauto"):
        # Set vm_max_map_count
        ret, out = self.machine_controller.run_cmd("sysctl -w vm.max_map_count={}".format(max_map_count))
        if ret != 0:
            return False, out
        ret, out = self.machine_controller.append_in_file(content="vm.max_map_count={}".format(max_map_count), file_path="/etc/sysctl.d/{}.conf".format(name))
        return True, out
