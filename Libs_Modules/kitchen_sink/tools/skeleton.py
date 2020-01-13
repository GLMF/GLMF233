from cleo import Command

#
# cet exemple a pour but de vous montrer comment on crée une commande à ajouter à la console
# Pour ce faire il faut créer un classe qui hérite de Command, une classe importer du package cleo
#
# Cette classe doit avoir une docstring dont le contenu sera utiliser dans cleo
#
# la première ligne de la docstring est une description suscinte de l'utilite de cette commande
#
# la deuxième ligne de la docstring est le nom de la commande dans la console
#

class SkeletonCommand(Command):
    """
    Implementation d'une commande très basique

    skeleton
    """

    def handle(self):
        self.line("Greetings Professor Falken")
