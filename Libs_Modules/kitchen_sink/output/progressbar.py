from cleo import Command
import time

class ProgressBarCommand(Command):
    """
    Cleo permet de d'afficher une barre de progression

    progressbar
    """

    def handle(self):
        self.progress_bar_50_units()

    def progress_bar_50_units(self):
        progress = self.progress_bar(50)
        for sec in range(50):
            time.sleep(1)
            progress.advance()
        progress.finish()
        self.line('')
        self.line('impact')
