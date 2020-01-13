from cleo import Command

class LevelCommand(Command):
    """
    Affichage avec les niveaux d'affichage (info, warning, ...)

    levels
    """
    def handle(self):
        levels = []
        levels.append('info')
        levels.append('comment')
        levels.append('question')
        levels.append('error')

        for level in levels:
            self.line('levels: <%(level)s> %(level)s </>' % {'level': level})
