from cleo import Command

class SecretCommand(Command):
    """
    Exemple saisie d'une valeur secrète (type mot de passe)

    secret
    """

    def handle(self):
        value = self.secret('Access to WOPR - Enter password')
        self.line("la valeur saisie est %s" % value)
