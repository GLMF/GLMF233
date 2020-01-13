#!/usr/bin/env python3

from cleo import Application
from cleo import CommandTester
import pytest

from tools.skeleton import SkeletonCommand

app = Application()
app.add(SkeletonCommand())

if __name__ == '__main__':
    command = app.find('skeleton')
    command_tester = CommandTester(command)
    command_tester.execute()

    if "Falken" in command_tester.io.fetch_output():
        print('Falken: OK')
    else:
        print('Falken: Failed')
    if "Uchiha" in command_tester.io.fetch_output():
        print('Uchiha: OK')
    else:
        print('Uchiha: Failed')
