from cleo import Command

class SelectBoxCommand(Command):
    """
    Exemple du choix d'une valeur par l'utlisateur avec une selectbox 

    selectbox
    """

    def handle(self):
        self.single_choice()
        self.multiple_choice()

    def single_choice(self):
        choices = []
        for i in range(10):
            choices.append('choice %02d' % i)
        choices.append('quit')
        choice = self.choice("Choississez une seule valeur", choices, len(choices)-1)
        self.line("Votre choix %s" % choice)

    def multiple_choice(self):
        choices = []
        for i in range(10):
            choices.append('choice %02d' % i)
        choices.append('quit')
        choice = self.choice("Choississez plusieurs valeurs", choices, '9,10', multiple=True)
        self.line("Vos choix %s" % ', '.join(choice))
