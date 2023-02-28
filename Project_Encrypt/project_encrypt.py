#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import platform
import re
import fnmatch
import glob
from pathlib import Path
from tkinterdnd2 import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk

#################### Start Drop Box ####################


def drop_box():
    root = TkinterDnD.Tk()
    root.withdraw()

    # Header
    root.title('File To Encrypt')

    # Box Size
    root.grid_rowconfigure(1, weight=1, minsize=250)
    root.grid_columnconfigure(0, weight=1, minsize=300)

    ### Print Event Info Console ###
    # def print_event_info(event):
    #     print('\nAction:', event.action)
    #     print('Supported actions:', event.actions)
    #     print('Mouse button:', event.button)
    #     print('Type codes:', event.codes)
    #     print('Current type code:', event.code)
    #     print('Common source types:', event.commonsourcetypes)
    #     print('Common target types:', event.commontargettypes)
    #     print('Data:', event.data)
    #     print('Event name:', event.name)
    #     print('Supported types:', event.types)
    #     print('Modifier keys:', event.modifiers)
    #     print('Supported source types:', event.supportedsourcetypes)
    #     print('Operation type:', event.type)
    #     print('Source types:', event.sourcetypes)
    #     print('Supported target types:', event.supportedtargettypes)
    #     print('Widget:', event.widget, '(type: %s)' % type(event.widget))
    #     print('X:', event.x_root)
    #     print('Y:', event.y_root, '\n')

    # Top Text / Instructions
    Label(root, text='Drag and Drop Encrypted File Here:').grid(
        row=0, column=0, padx=10, pady=5)

    # Destroy Funct. for Lambda
    def destroy():
        root.destroy()

    # Quit Funct. for Lambda
    def quit():
        root.quit()

    # If After File Add
    def file_added():
        Label(root, text='Is this the right file?:').grid(
            row=2, column=0, padx=10, pady=5)

        # Button 1 Config
        buttonbox.configure(buttonbox, text='Yes',
                            command=lambda: (quit(), destroy()))

        # Button 2 Appear
        buttonbox2.pack(side=LEFT, padx=5)

    # Button 1
    buttonbox = Frame(root)
    buttonbox.grid(row=3, column=0, columnspan=2, pady=5)
    buttonbox = Button(buttonbox, text='Close', command=root.destroy)
    buttonbox.pack(side=RIGHT, padx=0)

    # Button 2
    buttonbox2 = Frame(root)
    buttonbox2.grid(row=4, column=0, columnspan=2, pady=5)
    buttonbox2 = Button(buttonbox2, text='No', command=root.destroy)
    buttonbox2.pack_forget()  # (side=LEFT, padx=5)

    #### Listbox to drag & drop files ###

    listbox = Listbox(root, name='drop_listbox',
                      selectmode='extended', width=1, height=1)
    listbox.grid(row=1, column=0, padx=5, pady=5, sticky='news')

    ### Drop callbacks can be shared between the Listbox ###

    def drop_enter(event):
        event.widget.focus_force()
        # print('Entering widget: %s' % event.widget)
        # print_event_info(event)
        return event.action

    def drop_position(event):
        # print('Position: x %d, y %d' %(event.x_root, event.y_root))
        # print_event_info(event)
        return event.action

    def drop_leave(event):
        # print('Leaving %s' % event.widget)
        # print_event_info(event)
        return event.action

    # # Error No File Added
    # def error_no_file():
    #     root = TkinterDnD.Tk()
    #     frame = tk.Frame(root)

    #     mylabel = tk.Label(frame, text = "Please Add File", fg = "red")
    #     mylabel.pack(padx = 5, pady = 10)

    #     mybutton = tk.Button(frame, text = "Ok", command = root.destroy)
    #     mybutton.pack(padx = 5, pady = 10)

    def drop(event):
        if event.data:
            # print('Dropped data:\n', event.data)
            # print_event_info(event)
            if event.widget == listbox:

                # Catch and Use File Name
                global listbox_files

                # Get Filename / Add to List
                listbox_files = listbox.tk.splitlist(event.data)
                for f in listbox_files:
                    if os.path.exists(f):
                        # print('Dropped file: "%s"' % f)
                        listbox.insert('end', f)
                        # Theme Change
                        file_added()
                    else:
                        print('Not dropping file "%s": file does not exist.' % f)
            else:
                print('Error: reported event.widget not known')

        return event.action

    # Make the Listbox Drop Target
    listbox.drop_target_register(DND_FILES)  # , DND_TEXT)

    for widget in (listbox,):  # figure out why this needs space!!!
        widget.dnd_bind('<<DropEnter>>', drop_enter)
        widget.dnd_bind('<<DropPosition>>', drop_position)
        widget.dnd_bind('<<DropLeave>>', drop_leave)
        widget.dnd_bind('<<Drop>>', drop)
        # widget.dnd_bind('<<Drop:DND_Files>>', drop)
        # widget.dnd_bind('<<Drop:DND_Text>>', drop)

    # Define Drag Callbacks
    def drag_init_listbox(event):
        # print_event_info(event)
        # use a tuple as file list, this should hopefully be handled gracefully
        # by tkdnd and the drop targets like file managers or text editors
        data = ()
        if listbox.curselection():
            data = tuple([listbox.get(i) for i in listbox.curselection()])
            print('Dragging :', data)
        # tuples can also be used to specify possible alternatives for
        # action type and DnD type:
        return ((ASK, COPY), (DND_FILES, DND_TEXT), data)

    def drag_end(event):
        # print_event_info(event)

        # this callback doesn't do anything useful
        print('Drag ended for widget:', event.widget)

        # Make the widget a drag source

    listbox.drag_source_register(1, DND_TEXT, DND_FILES)

    listbox.dnd_bind('<<DragInitCmd>>', drag_init_listbox)
    listbox.dnd_bind('<<DragEndCmd>>', drag_end)

    root.update_idletasks()

    root.deiconify()

    root.mainloop()

#################### End Drop Box ####################

### Look For Steghide / Xcode / Macports ###


def find_files(path: str, glob_pat: str, ignore_case: bool = False):
    rule = re.compile(fnmatch.translate(glob_pat), re.IGNORECASE) if ignore_case \
        else re.compile(fnmatch.translate(glob_pat))
    return [n for n in glob.iglob(os.path.join(path, '**'), recursive=True) if rule.match(n)]


# print(find_files('C:/*', '*steghide*', ignore_case=True))


#################### Start Download Required Files OSX ####################

# TODO

#################### End Download Required Files OSX ####################

#################### Start Download Required Files Windows ####################

# TODO

#################### End Download Required Files Windows ####################

#################### Start Install Required Files OSX ####################

# TODO

#################### End Install Required Files OSX ####################

#################### Start Install Required Files Windows ####################

# TODO

#################### End Install Required Files Windows ####################


#################### Start "Start" Window ####################

def start_box():
    root = TkinterDnD.Tk()
    frame = tk.Frame(root)

    # Theme Change on Button Press
    def change_theme():

        # Label 1 Config
        drop_box()
        mylabel.config(text=listbox_files, bg="blue", fg="yellow")
        mylabel.pack(padx=5, pady=10)

        # Label 2 Config
        mylabel2.config(bg="blue", fg="yellow")
        mylabel2.pack(padx=5, pady=10)

        # Button 1 Config
        mybutton.config(text="Yes", command=lambda: (quit(), destroy()))
        mybutton.pack(padx=5, pady=10)

        # Button 2 Config
        mybutton2.config(text="No", command=root.destroy)
        mybutton2.pack(padx=5, pady=10)

    # Count Clicks For Yes Button
    root.counter = 0

    def clicks():
        root.counter += 1
        if root.counter == 3:
            mylabel.config(text="Are You Positive!!!", bg="red")
        elif root.counter == 10:
            mylabel.config(text="You Must Want This Virus!!", bg="red")
        elif root.counter == 20:
            mylabel.config(text="Only a couple more clicks :(", bg="red")
        elif root.counter == 24:
            mylabel.config(text="You made it to 24 clicks!!",
                           bg="blue", fg="yellow")
            change_theme()
        elif root.counter >= 24:
            change_theme()

        # Test Label
        # mylabel.config(text = f"{root.counter}", bg = "blue", fg = "yellow")
        # mylabel.pack(padx = 5, pady = 10)

    # Label 1
    mylabel = tk.Label(frame, text="This is a VIRUS!", bg="red")
    mylabel.pack(padx=5, pady=10)

    # Label 2
    mylabel2 = tk.Label(frame, text="Do You Want to Continue?", bg="red")
    mylabel2.pack(padx=5, pady=10)

    # Button 1
    mybutton = tk.Button(frame, text="Yes", command=clicks)
    mybutton.pack(padx=5, pady=10)

    # Button 2
    mybutton2 = tk.Button(frame, text="No", command=root.destroy)
    mybutton2.pack(padx=5, pady=10)

    frame.pack(padx=5, pady=5)

    root.mainloop()

#################### End "Start" Window ####################


start_box()
