


# ~ import sys
import os
import info
import subprocess
from configparser import ConfigParser



DEFAULT_CONFIG = """[CMD_ARGS]

## --genome option
## Path to genome fasta file or jellyfish index of genome
## if fasta file is given, kmerator will create jellyfish index
## We advise you to create a jellyfish index beforehand
# genome = /index/jellyfish/GRCh38_with_MT.jf

## --transcriptome option
## Path to transcriptome (fasta file)
# transcriptome = /transcriptome/GRCh38.fa

## --jellyfish-transcriptome option
## path to jellyfish transcriptome.
## If a jellyfish transcriptome with the same name (exept extension) exists
## in the directory of the --transcriptome option, this parameter is optional.
## If this option is not set and not jellyfish transcriptome found, it will
## be created.
# jellyfish_transcriptome = /transcriptome/GRCh38.jf

## --specie option
## set a specie (default: human)
# specie = human

## --kmer-length option
## set kmer length (default: 31)
# kmer_length = 31

## --chimera
## Only with --fasta-file option
# chimera = False

## --stringent option
## Only with --selection option
stringent = False

## output directory
# outdir = ./output

## --procs option
## number of procs (default: 1)
# procs = 1

## --keep option
## keep intermediate files (default: False)
# keep = False
"""


class Config:
    """
    attributes:
        - filename: name of configuration file
        - filepath: path of the configuration file
        - content: dict of configuration file
    methods:
        - edit(): edit configuration file
    """
    filename = 'config.ini'

    def __init__(self, appname):
        """ Class initialiser """
        ### define location of config file
        self.filePath = self.get_configPath(appname)
        ### create config file if not exists
        if not os.path.isfile(self.filePath):
            self.__set_default()
        ### create a dict of config file
        self.content = ConfigParser()
        self.content.read(self.filePath)


    def get_configPath(self, appname):
        """
        Find to config
            - app_configfile: params of app
            - user_configfile: params for the user (HOTSPOTS, SNP, etc)
        """
        ### Define config file location
        if os.geteuid():
            configdir = os.path.join(os.path.expanduser('~'), '.config', appname)
        else:
            configdir = os.path.join('/etc', appname)
        configfile = os.path.join(configdir, self.filename)
        return configfile


    def __set_default(self):
        try:
            os.makedirs(os.path.dirname(self.filePath), exist_ok=True)
            with open(self.filePath, 'w') as fs:
                fs.write(DEFAULT_CONFIG)
        except PermissionError as err:
            sys.exit(err.msg)


    def edit(self):
        """ Function doc """
        cmd = 'xdg-open' if os.environ.get('XDG_SESSION_TYPE') == 'x11' else 'editor'
        subprocess.call([cmd, self.filePath])
