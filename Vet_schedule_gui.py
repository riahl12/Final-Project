from distutils import command
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv


main_list = []
header = ["Title ", " First name ", " Last name " , " Phone # " , " Email " , " Email Opt-In Service " ,
                             " Pet Name " , " Species " , " Pet Age " , " Gender " , " Dog Breed " , " Cat Breed " , " Priority"]
FILENAME = "vet_schedule.csv"

#Create new file or overwrite when gui restarts
with open(FILENAME, "w", newline='') as file:
    Writer = csv.writer(file, delimiter=',')
    Writer.writerow(header)


def add():  #checks that the correct input is allowed for the different required fields, then grabs all the entries and appends them into the main list
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-") #this is setting that only string characters can be entered to validate input
                                                                                        #for the schedule
    phone_characters = set("123456789-")
    if not (name_characters.issuperset(first_name_entry.get()) and name_characters.issuperset(last_name_entry.get()) 
        and name_characters.issuperset(petname_entry.get())):
        messagebox.showerror("Error","The first name, last name and pet name must be letters. Try again.")

    
    elif not (phone_characters.issuperset(phone_label_entry.get())):
        messagebox.showerror("Error","That is not a phone number. Try again.")

    else:
        messagebox.showinfo("Check-In", "You are checked in.")
        with open(FILENAME, "r") as csv_file:
            priority = len(list(csv_file))
            
        lst = [title_combobox.get() + ' ', first_name_entry.get() + ' ', last_name_entry.get() +' ', phone_label_entry.get() + ' ' ,
            email_label_entry.get() +' ', email_opt_combobox.get() +' ', petname_entry.get() +' ', pet_species_combobox.get() +' ' ,
             petage_spinbox.get() +' ', pet_gender_combobox.get() +' ', dogbreed_combobox.get() +' ', catbreed_combobox.get()+ ' ', priority]
        main_list.append(lst)
    

def save():#This function is what appends to the csv file and combines the header that was created at the top along with writing the main list that
            #holds all the entries, then when the button is clicked it will tell the user the information was saved successfully
    with open(FILENAME, "a", newline='') as file:
        Writer = csv.writer(file, delimiter=',')
        for item in main_list:
            print(f'Item: {item}')
            Writer.writerow(item)
            main_list.remove(item)
        messagebox.showinfo("Check-In", "Your information was saved successfully.")

def clear():#This function is used if you need to add multiple entries at the same time and will clear all the
            #fields for you to be able to continue to use the program
    title_combobox.delete(0,END)
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    phone_label_entry.delete(0,END)
    email_label_entry.delete(0,END)
    email_opt_combobox.delete(0,END)
    petname_entry.delete(0,END)
    pet_species_combobox.delete(0,END)
    petage_spinbox.delete(0,END)
    pet_gender_combobox.delete(0,END)
    dogbreed_combobox.delete(0,END)
    catbreed_combobox.delete(0,END)



window = Tk()   #The start of the GUI creation
window.title("Vet Schedule")

frame = Frame(window)
frame.pack()

#User Info
user_info_frame = LabelFrame(frame, text="Owner Information")
user_info_frame.grid(row= 0, column=0, padx=25, pady=10)

first_name_label = Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Dr.","Mr.","Ms.","Mrs."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

phone_label = Label(user_info_frame, text="Phone Number")
phone_label.grid(row=2, column=0)
phone_label_entry = Entry(user_info_frame)
phone_label_entry.grid(row=3, column=0)

email_label = Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)
email_label_entry = Entry(user_info_frame)
email_label_entry.grid(row=3, column=1)

email_opt_label = Label(user_info_frame, text="Email Opt-In Service")
email_opt_combobox = ttk.Combobox(user_info_frame, values=["Yes", "No", "Not now"])
email_opt_label.grid(row=2, column=2)
email_opt_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Pet info
pet_info_frame = LabelFrame(frame, text="Pet Information")
pet_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

petname_label = Label(pet_info_frame, text="Pet Name")
petname_entry = Entry(pet_info_frame)
petname_label.grid(row=0, column=0)
petname_entry.grid(row=1, column=0)

pet_species_label = Label(pet_info_frame, text="Species")
pet_species_combobox = ttk.Combobox(pet_info_frame, values=["","Dog", "Cat","Other"])
pet_species_label.grid(row=0, column=1)
pet_species_combobox.grid(row=1, column=1)

petage_label = Label(pet_info_frame, text="Pet Age")
petage_spinbox = Spinbox(pet_info_frame, from_=0, to=20)
petage_label.grid(row=0, column=2)
petage_spinbox.grid(row=1, column=2)

pet_gender_label = Label(pet_info_frame, text="Gender")
pet_gender_combobox = ttk.Combobox(pet_info_frame, values=["Male", "Female", "Neutered Male", "Spayed Female"])
pet_gender_label.grid(row=2, column=0)
pet_gender_combobox.grid(row=3, column=0)


dogbreed_label = Label(pet_info_frame, text="Dog Breeds")
dogbreed_combobox = ttk.Combobox(pet_info_frame, values=["Not Dog","Bulldog", "Beagle", "French Bulldog", "German Shepherd","Golden Retriever","Australian Shepherd",
                                                        "Corgi","Goldendoodle","Mixed Breed","Labrador Retriever","Dachshund", "Great Dane","Husky"])
dogbreed_label.grid(row=2, column=1)
dogbreed_combobox.grid(row=3,column=1)

catbreed_label = Label(pet_info_frame, text="Cat Breeds")
catbreed_combobox = ttk.Combobox(pet_info_frame, values=["Not Cat","Domestic Shorthair", "Domestic Mediumhair", "Domestic Longhair", "Scottish Fold","Maine Coon",
                                                         "Persain","Ragdoll", "Siamese","Bengal","Manx","Munchkin","Russian Blue", "Sphynx"])
catbreed_label.grid(row=2, column=2)
catbreed_combobox.grid(row=3, column=2)

for widget in pet_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button creation
add_button = Button(frame, text="Add Info", command=add)
add_button.grid(row=4,column=0,sticky="news",padx=20, pady=10)

save_button = Button(frame, text="Save Info", command=save)
save_button.grid(row=5, column=0,sticky="news", padx=20, pady=10)

clear_button = Button(frame, text="Clear", command= clear)
clear_button.grid(row=6, column=0, sticky="news", padx=20, pady=10)





window.mainloop()



