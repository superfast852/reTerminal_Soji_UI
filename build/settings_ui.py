# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from pathlib import Path
import tk_tools
from sys import exit

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk


ASSETS_PATH = Path(r"./assets/frame0")

box_pos = [(185, 177, 481, 387), (540, 174, 836, 384),
           (895, 174, 1191, 384), (186, 448, 482, 658),
           (541, 445, 837, 655), (896, 445, 1192, 655)]


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


y = []
plot_enable = 0
plot_active = 0
plot_lim = 100
# Building Blocks
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#2E2E2E")


def plot_box_1(sx, sy):
    fig = Figure(figsize=(sx/100, sy/100), dpi=100)
    pl1 = fig.add_subplot(111)
    pl1.plot(y)
    pltwidget = FigureCanvasTkAgg(fig, master=window)
    pltwidget.draw()
    pltwidget.get_tk_widget().place(x=box_pos['r3'][0]+25, y=box_pos["r3"][1]+30)


def button_1():
    exit(0)


def button_2():
    print("b2")


def button_3():
    print("b3")


def button_4():
    print("b4")


def button_5():
    global plot_active
    if plot_active:
        plot_active = 0
    else:
        plot_active = 1
    print("b5")


def button_6():
    print("b6")


# ------------------------------------------BACKBONE------------------------------------------------------------------ #
base = Canvas(
        window,
        bg="#2E2E2E",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

base.place(x=0, y=0)
# Buttons
button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
b1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button_1,
        relief="flat"
    )
b1.place(
        x=0.0,
        y=624.0,
        width=96.0,
        height=96.0
    )

button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
b2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=button_2,
        relief="flat"
    )
b2.place(
        x=0.0,
        y=505.0,
        width=96.0,
        height=96.0
    )

button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
b3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=button_3,
        relief="flat"
    )
b3.place(
        x=0.0,
        y=375.0,
        width=96.0,
        height=96.0
    )

button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
b4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=button_4,
        relief="flat"
    )
b4.place(
        x=0.0,
        y=252.0,
        width=96.0,
        height=96.0
    )

button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
b5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=button_5,
        relief="flat"
    )
b5.place(
        x=0.0,
        y=126.0,
        width=96.0,
        height=96.0
    )

button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
b6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=button_6,
        relief="flat"
    )
b6.place(
        x=0.0,
        y=0.0,
        width=96.0,
        height=96.0
    )

    # Borders
base.create_rectangle(
        0.0,
        0.0,
        96.0,
        720.0,
        fill="#6700CD",
        outline="")

base.create_rectangle(
        0.0,
        0.0,
        1280.0,
        96.0,
        fill="#6700CD",
        outline="")

base.create_text(
        500.0,
        40.0,
        anchor="center",
        text="Soji DNN Command Terminal",
        fill="#FFFFFF",
        font=("PalanquinDark Regular", 40 * -1)
    )

canvas = base


# --------------------------------------TAB CODE---------------------------------------------------------------------- #


asdf = 0


def abstract_plot():
    global asdf
    if asdf == 100:
        asdf = 0
    y.append(asdf)
    if len(y) >= plot_lim:
        y.pop(0)
    asdf += 1
    plot_box_1(250, 180)


def updater():
    if plot_enable:
        abstract_plot()
    window.after(100, updater)


updater()

window.resizable(False, False)
window.mainloop()