from distutils import command
import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":

    #User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            phone = phone_label_entry.get()
            email = email_label_entry.get()
            email_opt = email_opt_combobox.get()

        #Pet info
            pet_name = petname_entry.get()
            pet_species = pet_species_combobox.get()

            if pet_name and pet_species:
                pet_age = petage_spinbox.get()
                pet_gender = pet_gender_combobox.get()
                dog_breed = dogbreed_combobox.get()
                cat_breed = catbreed_combobox.get()
                

                print("Title:", title,"First name:", firstname, "Last name:", lastname)
                print("Phone #:", phone, "Email:", email, "Email Opt-In Service:", email_opt)
                print("Pet Name:", pet_name, "Species:", pet_species,"Pet Age:", pet_age)
                print("Gender:", pet_gender, "Dog Breed:", dog_breed, "Cat Breed:", cat_breed)
                print("----------------------------------------------------------")
            else:
                tkinter.messagebox.showwarning(title = "Error", message = "Pet name and species are required to sumbit.")
        else:
            tkinter.messagebox.showwarning(title = "Error", message = "First name and last name are required to submit.")
    else:
        tkinter.messagebox.showwarning(title = "Error", message="You have not entered all the required information.")


window = tkinter.Tk()
window.title("Vet Schedule")

frame = tkinter.Frame(window)
frame.pack()

#User Info
user_info_frame = tkinter.LabelFrame(frame, text="Owner Information")
user_info_frame.grid(row= 0, column=0, padx=25, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.","Ms.","Mrs."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

phone_label = tkinter.Label(user_info_frame, text="Phone Number")
phone_label.grid(row=2, column=0)
phone_label_entry = tkinter.Entry(user_info_frame)
phone_label_entry.grid(row=3, column=0)

email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)
email_label_entry = tkinter.Entry(user_info_frame)
email_label_entry.grid(row=3, column=1)

email_opt_label = tkinter.Label(user_info_frame, text="Email Opt-In Service")
email_opt_combobox = ttk.Combobox(user_info_frame, values=["Yes", "No", "Not now"])
email_opt_label.grid(row=2, column=2)
email_opt_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Pet info
pet_info_frame = tkinter.LabelFrame(frame, text="Pet Information")
pet_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

petname_label = tkinter.Label(pet_info_frame, text="Pet Name")
petname_entry = tkinter.Entry(pet_info_frame)
petname_label.grid(row=0, column=0)
petname_entry.grid(row=1, column=0)

pet_species_label = tkinter.Label(pet_info_frame, text="Species")
pet_species_combobox = ttk.Combobox(pet_info_frame, values=["","Dog", "Cat","Other"])
pet_species_label.grid(row=0, column=1)
pet_species_combobox.grid(row=1, column=1)

petage_label = tkinter.Label(pet_info_frame, text="Pet Age")
petage_spinbox = tkinter.Spinbox(pet_info_frame, from_=0, to=20)
petage_label.grid(row=0, column=2)
petage_spinbox.grid(row=1, column=2)

pet_gender_label = tkinter.Label(pet_info_frame, text="Gender")
pet_gender_combobox = ttk.Combobox(pet_info_frame, values=["Male", "Female", "Neutered Male", "Spayed Female"])
pet_gender_label.grid(row=2, column=0)
pet_gender_combobox.grid(row=3, column=0)


dogbreed_label = tkinter.Label(pet_info_frame, text="Dog Breeds")
dogbreed_combobox = ttk.Combobox(pet_info_frame, values=["Not Dog","Bulldog", "Beagle", "French Bulldog", "German Shepherd","Golden Retriever","Australian Shepherd",
                                                        "Corgi","Goldendoodle","Mixed Breed","Labrador Retriever","Dachshund", "Great Dane","Husky"])
dogbreed_label.grid(row=2, column=1)
dogbreed_combobox.grid(row=3,column=1)

catbreed_label = tkinter.Label(pet_info_frame, text="Cat Breeds")
catbreed_combobox = ttk.Combobox(pet_info_frame, values=["Not Cat","Domestic Shorthair", "Domestic Mediumhair", "Domestic Longhair", "Scottish Fold","Maine Coon",
                                                         "Persain","Ragdoll", "Siamese","Bengal","Manx","Munchkin","Russian Blue", "Sphynx"])
catbreed_label.grid(row=2, column=2)
catbreed_combobox.grid(row=3, column=2)

for widget in pet_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Verify Information")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I have entered the correct information.",
                                        variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Check-In", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



window.mainloop()