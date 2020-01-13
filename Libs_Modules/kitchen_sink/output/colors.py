from cleo import Command

class ColorCommand(Command):
    """
    Affichage avec des couleurs

    colors
    """
    def handle(self):
        colors = []
        colors.append(None)
        colors.append('black')
        colors.append('red')
        colors.append('green')
        colors.append('yellow')
        colors.append('blue')
        colors.append('magenta')
        colors.append('cyan')
        colors.append('white')

        for fg in colors:
            for bg in colors:
                d = {'fg': '', 'bg': ''}
                if fg == bg: continue
                if fg: d['fg'] = 'fg=%s;' % fg
                if bg: d['bg'] = 'bg=%s' % bg
                self.line('colors: <%(fg)s%(bg)s> %(fg)s%(bg)s</>' % d)
