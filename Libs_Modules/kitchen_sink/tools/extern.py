from cleo import Command
import subprocess


class ExternCommand(Command):
    """
    Implementation d'une commande qui appelle un programme externe

    extern
    """

    def handle(self):
        self.line('appelle de la commande ls -l avec subprocess')
        subprocess.run(["ls", "-l"])
