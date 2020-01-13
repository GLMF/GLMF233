from cleo import Command

class AutoCompletionCommand(Command):
    """

    Exemple de la saisie d'une valeur par l'utilisateur avec et sans completion

    autocompletion
    """

    def handle(self):
        names = ['France', 'USA', 'Russie', 'Japon', 'Allemagne']
        question = self.create_question('Quelle est votre pays pour cette partie de "guerre thermo-nucléaire globale"', default='France')
        question.set_autocomplete_values(names)
        choice = self.ask(question)
        self.line("Vous avez choisi de jouer: %s" % choice)
