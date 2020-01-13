from cleo import Command

class ConfirmationCommand(Command):
    """
    Exemple d'une demande de confirmation à l'utilisateur

    confirmation
    """

    def handle(self):
        choice = self.confirm('Do you want to play chess? Professor Falken', True, '(?i)^(y|o)')
        self.line('choice %s ' % choice)
        if choice:
            self.line("Yes")
        else:
            self.line("No")
