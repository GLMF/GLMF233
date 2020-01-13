from cleo import Command

class ArgumentOptionCommand(Command):
    """
    Exemple de l'utilisation d’arguments et options

    argument_option
        { name : who do you want to greet ? }
        { surname? : who do you want to greet (surname) ? }
        { --u|uppercase : met le nom en majuscule }
    """

    def handle(self):
        fullname = self.argument('name')
        surname = self.argument('surname')
        if surname:
            fullname = '%s (%s)' % (surname, fullname)
        is_uppercase = self.option('uppercase')
        if is_uppercase:
            fullname = fullname.upper()
        self.line("Greetings Professor %(name)s" % {'name':fullname})
