
from abstract_source_accessor import AbstractSourceAccessor
import subprocess
import os
from log_manager import logging
logger = logging.getLogger('source.GitSourceAccessor')

class GitSourceAccessor(AbstractSourceAccessor):
    """
    Permet de transformer les sources en fichiers recuperables
    La source doit pouvoir etre copie sur une machine
    La source peut contenir des variables dont la valeur est passe dans la source config
    """
    def __init__(self, name, global_config, source_config):
        """
        Recupere la source si besoin pour la rendre accessible en fichier
        """
        super(GitSourceAccessor, self).__init__(
            name=name,
            global_config=global_config,
            source_config=source_config
        )
        self.target_branch = source_config.get('source::branch')
        # Recuperation de la branch du cache
        git_dir=self.local_path + '/.git'


        # Verification du cache existant
        if os.path.exists(self.local_path):
            curr_branch = subprocess.check_output([
                'git --git-dir='+git_dir+' rev-parse --abbrev-ref HEAD'
            ], shell=True).decode()[:-1]
            if curr_branch != self.target_branch:
                # En cas de changement de branch on clean le cache
                subprocess.call('rm -rf '+self.local_path)

        # Mise a jour du cache
        if not os.path.exists(self.local_path):
            # creation du repertoire cache via git clone
            cmd = [
                'git',
                'clone',
                '-b' + self.target_branch,
                '--single-branch',
                '--no-tags',
                source_config.get('source::url'),
                self.local_path
            ]
            logger.info('Creation du dossier temporaire', cmd=cmd)
            subprocess.call(cmd)
        else:
            # Mise du repertoire cache via git pull
            cmd = [
                'git',
                '--git-dir='+git_dir,
                'pull'
            ]
            subprocess.call(cmd)
            logger.info('MAJ du dossier temporaire', cmd=cmd)
