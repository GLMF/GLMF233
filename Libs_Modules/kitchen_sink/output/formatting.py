from cleo import Command

class FormattingCommand(Command):
    """
    Affichage avec des options d'affichage

    formatting
    """
    def handle(self):
        options = []
        options.append('bold')
        options.append('underscore')
        options.append('blink')
        options.append('reverse')
        options.append('conceal')

        for a in options:
            tag = "options=%s" % a
            self.line('options: <%(tag)s> %(tag)s </>' % {'tag': tag})
        for a in options:
            tag = "options=%s" % a
            self.line('options: <fg=black;bg=cyan;%(tag)s> %(tag)s </>' % {'tag': tag})
