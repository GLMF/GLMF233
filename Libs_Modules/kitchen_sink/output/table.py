from cleo import Command

class TableCommand(Command):
    """
    Exemple saisie libre d'une valeur par l'utilisateur

    table
    """

    def handle(self):
        self.table_default()

    def table_default(self):
        table = self.table()
        self.line("compact default")
        self.line("Global Thermonuclear War simulation - WOPR")
        table.set_header_row(['Country', 'Missile', 'Dead (estimation)'])
        table.set_rows([
            ['France', '00', '0 M'],
            ['USA',    '11', '110 M'],
            ['Japon',  '01', '10 M'],
            ['Russie', '10', '100 M']
        ])
        table.render(self.io)
