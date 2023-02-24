from tkinter import *
# from tkinter import ttk  

""" First, create a root window and set its title to 'Menu Demo': """
root = Tk()  
root.title('Menu Demo')
root.geometry('347x216+200+50') 

""" Second, create a menu bar and assign it to the menu option of the root window: 
Note that each top-level window can only have only one menu bar."""
menubar = Menu(root)
root.config(menu=menubar)

""" Third, create a File menu whose container is the menubar: """
file_menu = Menu(menubar, tearoff=0)
""" Fourth, add a menu item to the file_menu: """
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(label="Preferences", menu=sub_menu)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

""" Finally, add the File menu to the menubar: """
menubar.add_cascade(label="File", menu=file_menu, underline=0)

""" Create the Help menu """
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

""" add the Help menu to the menubar """
menubar.add_cascade(label="Help", menu=help_menu)




mainloop()