
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


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\super\Desktop\reTerminal\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


asdf = 0
tab = 0
loop_id = None
y = []
plot_lim = 100
# Building Blocks
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#2E2E2E")


def plot_box_1(sx, sy, px, py):
    fig = Figure(figsize=(sx/100, sy/100), dpi=100)
    pl1 = fig.add_subplot(111)
    pl1.plot(y)
    pltwidget = FigureCanvasTkAgg(fig, master=window)
    pltwidget.draw()
    tkplt = pltwidget.get_tk_widget()
    tkplt.place(x=px, y=py)
    return tkplt, fig


def button_1():
    global tab
    tab = 0
    exit(0)


def button_2():
    global tab
    tab = 2
    switch_frames(base)
    print("b2")


def b2_updater():
    global tab, loop_id
    if tab != 2:
        window.after_cancel(loop_id)
        # Remember to destroy widgets
    else:
        loop_id = window.after(25, b2_updater)

def button_3():
    global tab
    tab = 3
    switch_frames(base)
    print("b3")


def b3_updater():
    global tab, loop_id
    if tab != 3:
        window.after_cancel(loop_id)
        # Remember to destroy widgets
    else:
        loop_id = window.after(25, b3_updater)


def button_4():
    global tab
    tab = 4
    switch_frames(base)
    print("b4")


def b4_updater():
    global tab, loop_id
    if tab != 4:
        window.after_cancel(loop_id)
        # Remember to destroy widgets
    else:
        loop_id = window.after(25, b4_updater)


def button_5():
    global tab
    tab = 5
    switch_frames(base)
    print("b5")


def b5_updater():
    global tab, loop_id
    if tab != 5:
        window.after_cancel(loop_id)
        # Remember to destroy widgets
    else:
        loop_id = window.after(25, b5_updater)


def button_6():
    global tab
    if tab != 6:
        # Home
        tab = 6
        switch_frames(base)
        box_pos = [(185, 177, 481, 387), (540, 174, 836, 384), (895, 174, 1191, 384),
                   (186, 448, 482, 658), (541, 445, 837, 655), (896, 445, 1192, 655)]

        # Bars
        progress1 = ttk.Progressbar(window, maximum=100, length=200, value=0, orient='horizontal', mode='determinate')
        progress2 = ttk.Progressbar(window, maximum=100, length=200, value=0, orient='horizontal', mode='determinate')
        progress1.place(x=(box_pos[1][0] + 148) - 100, y=(box_pos[1][1] + 105))
        progress2.place(x=(box_pos[1][0] + 148) - 100, y=(box_pos[1][1] + 175))

        # Widget Rectangles
        canvas.create_rectangle(
            185.0,
            177.0,
            481.0,
            387.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            245.0,
            223.0,
            anchor="nw",
            text="Pi stats:\nIP, cpu usage, whatever",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )

        canvas.create_rectangle(
            540.0,
            174.0,
            836.0,
            384.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            600.0,
            220.0,
            anchor="nw",
            text="Battery Monitor",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )
        canvas.create_text(
            600.0,
            250.0,
            anchor="nw",
            text="Analytical Engine Bat",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )
        canvas.create_text(
            600.0,
            320.0,
            anchor="nw",
            text="Battery Monitor",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )
        canvas.create_rectangle(
            895.0,
            174.0,
            1191.0,
            384.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            948.0,
            180.0,
            anchor="nw",
            text="Sensor monitor",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )

        canvas.create_rectangle(
            186.0,
            448.0,
            482.0,
            658.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            246.0,
            494.0,
            anchor="nw",
            text="Arm angles",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )

        canvas.create_rectangle(
            541.0,
            445.0,
            837.0,
            655.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            601.0,
            491.0,
            anchor="nw",
            text="idk some other stats",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )

        canvas.create_rectangle(
            896.0,
            445.0,
            1192.0,
            655.0,
            fill="#6700CD",
            outline="")

        canvas.create_text(
            949.0,
            485.0,
            anchor="nw",
            text="Allen add important stats",
            fill="#000000",
            font=("PalanquinDark Regular", 20 * -1)
        )

        # Updating Function
        asdf = 0
        b6_updater(progress1, progress2, box_pos)


def b6_updater(p1, p2, box_pos):
    global loop_id, asdf
    if asdf == 100:
        asdf = 0
    p1['value'] = asdf
    p2['value'] = 100-asdf
    y.append(asdf)
    if len(y) >= plot_lim:
        y.pop(0)
    asdf += 1
    plt_wid, fig = plot_box_1(250, 180, box_pos[2][0]+25, box_pos[2][1]+30)
    if tab != 6:
        window.after_cancel(loop_id)
        p1.destroy()
        p2.destroy()
        fig.clf()
        plt_wid.place_forget()
        plt_wid.destroy()
        del(plt_wid)
    else:
        loop_id = window.after(25, b6_updater, p1, p2, box_pos)


def switch_frames(root):
    root.delete('all')
    # Borders
    root.create_rectangle(
        0.0,
        0.0,
        96.0,
        720.0,
        fill="#6700CD",
        outline="")

    root.create_rectangle(
        0.0,
        0.0,
        1280.0,
        96.0,
        fill="#6700CD",
        outline="")

    root.create_text(
        500.0,
        40.0,
        anchor="center",
        text="Soji DNN Command Terminal",
        fill="#FFFFFF",
        font=("PalanquinDark Regular", 40 * -1)
    )


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
# ---------------------------------------TAB CODE--------------------------------------------------------------------- #


button_6()

window.resizable(False, False)
window.mainloop()
