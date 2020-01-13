from cleo import Command

class CommandCommand(Command):
    """
    Implementation d'une commande qui appelle une autre commande

    command
    """

    def handle(self):
        self.line('appelle de la commande cleo argument_option avec un argument et une option (TheOne -u)')
        self.call("argument_option", "TheOne -u")
        self.line('appelle de la commande cleo argument_option avec un argument et une option (TheOne -u) en mode silent')
        self.call_silent("argument_option", "TheOneSilent -u")
