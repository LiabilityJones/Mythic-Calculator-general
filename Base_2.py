from tkinter import *
from tkinter import messagebox
from Dictionary import body_part
from Dictionary import spc_dmg_description
from Dictionary_2 import special_table


window = Tk()
window.title("Mythic Damage Calculation")
window.config(padx=50, pady=50)


# Labels
starting_label = Label(text="Damage Calculations")
starting_label.grid(column=1, row=0)
body_location_label = Label(text="Body Location Number:")
body_location_label.grid(column=0, row=1)
armor_label = Label(text="Armor Value:")
armor_label.grid(column=0, row=3)
toughness_label = Label(text="(Mythic) Toughness Value: ")
toughness_label.grid(column=0, row=4)
pierce_label = Label(text="Pierce Value: ")
pierce_label.grid(column=0, row=5)
damage_label = Label(text="Base Damage Value: ")
damage_label.grid(column=0, row=6)

# Entries
body_location_entry = Entry(width=10)
body_location_entry.grid(column=1, row=1)
armor_entry = Entry(width=10)
armor_entry.grid(column=1, row=3, sticky="EW")
toughness_entry = Entry(width=10)
toughness_entry.grid(column=1, row=4, sticky="EW")
pierce_entry = Entry(width=10)
pierce_entry.grid(column=1, row=5, sticky="EW")
damage_entry = Entry(width=10)
damage_entry.grid(column=1, row=6, sticky="EW")


# Definitions


def hit_location(location):
    """Returns the location that was hit by the attack."""
    return body_part.get(location)


def check_location():
    """Prints the location that was hit"""
    location = int(body_location_entry.get())
    location_hit = Canvas(width=200, height=24)
    location_hit.create_text(100, 12, text=f"{hit_location(location)}")
    location_hit.grid(column=0, row=2, columnspan=2)


def damage_calculation():
    """Calculates the total damage taken"""
    location_hit = hit_location(int(body_location_entry.get()))
    damage_resist = int(armor_entry.get()) + int(toughness_entry.get())
    dr_left = damage_resist - int(pierce_entry.get())
    if dr_left < 0:
        dr_left = 0
    total_damage = int(damage_entry.get()) - dr_left
    if total_damage < 0:
        total_damage = 0
    damage_output_label = Label(text=f"The attack deals {total_damage} damage\n to the {location_hit}")
    damage_output_label.grid(column=1, row=7)


def reset():
    """Resets applications fields"""
    body_location_entry.delete(0, END)
    armor_entry.delete(0, END)
    toughness_entry.delete(0, END)
    pierce_entry.delete(0, END)
    damage_entry.delete(0, END)


def special_damage_check(part_location, damage_dealt):
    """Checks if key is in dict, returns value"""
    if damage_dealt > 84:
        raise AttributeError
    else:
        for key in special_table:
            if part_location in key:
                return special_table[key].get(damage_dealt)




def special_damage_calculation():
    """Calculates and returns special damage output"""
    global caut_checkmark

    if checked_state.get() == 1:
        special_damage = int(damage_entry.get()) + int(pierce_entry.get())
    else:
        special_damage = int(damage_entry.get())
    # if special_damage is None:
    #     raise AttributeError
    # else:
    #     pass
    location_hit = int(body_location_entry.get())
    location = hit_location(location_hit)
    try:
        special_damage_label = Label(text=special_damage_check(location, special_damage))
        special_damage_label.grid(column=1, row=9)
    except AttributeError:
        special_damage = 84
        special_damage_label = Label(text=special_damage_check(location, special_damage))
        special_damage_label.grid(column=1, row=9)
    try:
        spc_output = special_damage_check(location, special_damage)
        spc_output_1 = spc_output.split()
    except AttributeError:
        special_damage = 84
        spc_output = special_damage_check(location, special_damage)
        spc_output_1 = spc_output.split()
    spc_output_string = "".join(spc_output_1)
    for key in spc_dmg_description:
        if key in spc_output_string:
            messagebox.showinfo(title="Descriptions", message=f"{spc_dmg_description[key]}")


# Buttons
calculate_button = Button(text="DMG Calculate", command=damage_calculation)
calculate_button.grid(column=0, row=7)
location_button = Button(text="LOC Calculate", command=check_location)
location_button.grid(column=2, row=1, sticky="EW")
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=1, row=10)
special_damage_button = Button(text="SPD Calculate", command=special_damage_calculation)
special_damage_button.grid(column=0, row=9)

# Checkbox
checked_state = IntVar()
caut_checkmark = Checkbutton(text="Cauterize?", variable=checked_state)
caut_checkmark.grid(column=0, row=8)


window.mainloop()
