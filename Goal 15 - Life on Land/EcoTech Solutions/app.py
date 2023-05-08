from rich import text
from rich import box
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

from rich.live import Live
from rich.traceback import install
install(show_locals=True)
from rich.console import Console

from datetime import datetime
import numpy as np
import asciichartpy
import csv
import keyboard
from time import sleep
import psutil
import platform

layout = Layout()
layout.split_column(
        Layout(name = "Header"),
        Layout(name = "Body"),
        Layout(name = "Footer")
        )

layout["Body"].split_column(
        Layout(name = "Upper_Body"),
        Layout(name = "Lower_Body")
        )
layout["Upper_Body"].split_row(Layout(name = "UB1"), Layout(name = "UB2"))
layout["Lower_Body"].split_row(Layout(name = "LB1"), Layout(name = "LB2"))
layout["UB1"].split_column(Layout(name = "UB1_1"), Layout(name = "UB1_2"))
layout["Header"].size = 3
layout["Footer"].size = 3

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand = True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")

        grid.add_row("♻", "[b]EcoTech Solutions[/]", datetime.now().ctime().replace(":", "[blink]:[/]"))

        return Panel(grid, style = "Bold white on Black")

class Footer:
    def __rich__(self) -> Panel:
        f_grid = Table.grid(expand=True)
        f_grid.add_column(justify="left")
        f_grid.add_column(justify="center")
        f_grid.add_column(justify="right")

        f_grid.add_row("☀", "[b]SDG Goal 15 - Life on Land[/]", "🌿")

        return Panel(f_grid, style = "Bold white on black")


layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)