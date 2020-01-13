#!/usr/bin/env python3

from cleo import Application

from userinput.autocompletion import AutoCompletionCommand
from userinput.confirmation import ConfirmationCommand
from userinput.secret import SecretCommand
from userinput.selectbox import SelectBoxCommand
from userinput.argument_option import ArgumentOptionCommand

from output.colors import ColorCommand
from output.formatting import FormattingCommand
from output.levels import LevelCommand
from output.styles import StyleCommand
from output.overwrite import OverwriteCommand
from output.progressbar import ProgressBarCommand
from output.table import TableCommand

from tools.skeleton import SkeletonCommand
from tools.command import CommandCommand
from tools.extern import ExternCommand

app = Application()

app.add(ArgumentOptionCommand())
app.add(AutoCompletionCommand())
app.add(ConfirmationCommand())
app.add(SecretCommand())
app.add(SelectBoxCommand())

app.add(ColorCommand())
app.add(FormattingCommand())
app.add(LevelCommand())
app.add(StyleCommand())
app.add(OverwriteCommand())
app.add(ProgressBarCommand())
app.add(TableCommand())

app.add(SkeletonCommand())
app.add(CommandCommand())
app.add(ExternCommand())

if __name__ == '__main__':
    app.run()
