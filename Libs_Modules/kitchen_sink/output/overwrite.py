from cleo import Command
import time

class OverwriteCommand(Command):
    """
    commande qui permet de réécrire sur la dernière ligne du terminal

    overwrite
    """


    def handle(self):
        self.line('DEFCON 1 COUNTDOWN')
        for i in range(10):
            time.sleep(1)
            self.overwrite('<info>%d seconds</> before impact' % (10-i))
        self.line('')
        self.line('<error>IMPACT</>')
