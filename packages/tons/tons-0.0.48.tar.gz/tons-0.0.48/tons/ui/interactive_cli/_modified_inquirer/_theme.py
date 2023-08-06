from blessed import Terminal
from inquirer.themes import Default

term = Terminal()


class ModifiedTheme(Default):
    def __init__(self):
        super(ModifiedTheme, self).__init__()
        self.List.selection_color = term.bold
        self.List.selection_cursor = ">"
        self.List.unselected_color = term.normal
