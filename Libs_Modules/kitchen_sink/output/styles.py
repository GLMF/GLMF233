from cleo import Command

class StyleCommand(Command):
    """
    Creation d'une balise de style de mise en forme

    styles
    """

    def handle(self):
        self.add_style('greetings', fg='white', bg='green', options='bold')
        self.line(' Greetings Professor <greetings> Falken </greetings>')
        self.line("instruction: self.add_style('greetings', fg='white', bg='white', options='bold')")
