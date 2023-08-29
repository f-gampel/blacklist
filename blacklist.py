import tkinter as tk
import csv
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title('Czarna lista')
#root.geometry('800x600')

mainframe = ttk.Frame(root, padding=10)
mainframe.grid(column=0, row=0, sticky='nsew')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Title label
title_label = ttk.Label(mainframe, text='Czarna Lista Bosmana v0.01', font=(None, 25))
title_label.grid(row=0, column=0, columnspan=2)

buttonframe = ttk.Frame(mainframe, padding=5)
buttonframe.grid(column=0, row=1, sticky='ns')
buttonframe['relief'] = 'sunken'

def add_to_list():
    add_dialog = tk.Toplevel(root)
    
    add_dialog_mf = ttk.Frame(add_dialog, padding=10)
    add_dialog_mf.grid(row=0, column=0, sticky='nwes')
    
    entries_frame = ttk.Frame(add_dialog_mf)
    entries_frame.grid(row=0, column=0, sticky='nwe')
    
    button_frame = ttk.Frame(add_dialog_mf)
    button_frame.grid(row=1, column=0, sticky='s')
    
    label1 = ttk.Label(entries_frame, text='Imię')
    label2 = ttk.Label(entries_frame, text='Nazwisko')
    label3 = ttk.Label(entries_frame, text='Rejestracja')
    label4 = ttk.Label(entries_frame, text='Adres')
    label5 = ttk.Label(entries_frame, text='Telefon')
    
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=2, column=0)
    label4.grid(row=3, column=0)
    label5.grid(row=4, column=0)
    
    entry1 = ttk.Entry(entries_frame) 
    entry2 = ttk.Entry(entries_frame) 
    entry3 = ttk.Entry(entries_frame) 
    entry4 = ttk.Entry(entries_frame) 
    entry5 = ttk.Entry(entries_frame) 
    
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    
    def add_function():
        contact = (entry1.get(),
                   entry2.get(),
                   entry3.get(),
                   entry4.get(),
                   entry5.get())
        tree.insert('', tk.END, values=contact)
        contacts.append(contact)
        add_dialog.destroy()
    
    add_button = ttk.Button(button_frame, text='Dodaj', command=add_function)
    cancel_button = ttk.Button(button_frame, text='Anuluj', command=add_dialog.destroy)
    add_button.grid(row=0,column=0)
    cancel_button.grid(row=0,column=1)
    
def read_database(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        contacts = [row for row in reader]
        
    for contact in contacts:
        tree.insert('', tk.END, values=contact)
    return contacts
    
def load_database():
    filetypes = (('Pliki CSV', '*.csv'))
    file_path = filedialog.askopenfilename()
    tree.delete(*tree.get_children())
    read_database(file_path)
    
    
def save_database():
    filetypes = [('Pliki CSV', '*.csv')]
    file_path = filedialog.asksaveasfilename(filetypes = filetypes, defaultextension=".csv")
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for entry in contacts:
            writer.writerow(entry)
    print(file_path)


def del_from_list():
    for selected_item in tree.selection():
        item_values = tree.item(selected_item).get('values')
        item_values = list(map(str, item_values))
        contacts.remove(item_values)
        tree.delete(selected_item)

#Buttons
add_button = ttk.Button(buttonframe, text="Dodaj do listy...", command=add_to_list)
add_button.grid(column=0, row=0, sticky='we')

del_button = ttk.Button(buttonframe, text="Usuń z listy", command=del_from_list)
del_button.grid(column=0, row=1, sticky='we')

save_button = ttk.Button(buttonframe, text="Zapisz jako...", command=save_database)
save_button.grid(column=0, row=2, sticky='we')

load_button = ttk.Button(buttonframe, text="Wczytaj dane", command=load_database)
load_button.grid(column=0, row=3, sticky='we')

# define columns
columns = ('first_name', 'last_name', 'license_plate', 'address', 'phone')

tree = ttk.Treeview(mainframe, columns=columns, show='headings', height=20)

# define headings
tree.heading('first_name', text='Imię')
tree.heading('last_name', text='Nazwisko')
tree.heading('license_plate', text='Rejestracja')
tree.heading('address', text='Adres')
tree.heading('phone', text='Telefon')

# generate sample data
current_filepath = '/home/filip/Documents/Programy/blacklist/baza.csv'
contacts = read_database(current_filepath)

#contacts = []
#for n in range(1, 10):
#    contacts.append((f'imię {n}', f'nazwisko {n}', f'WPI{n}', 'Piaseczno', '1234'))

def item_selected(event):
    pass


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=1, column=1, sticky='ns')

# add a scrollbar
scrollbar = ttk.Scrollbar(mainframe, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky='ns')

# run the app
root.mainloop()