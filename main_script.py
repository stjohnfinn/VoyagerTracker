import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser
import get_data

data_soup = get_data.get_data()

# Declaring all of the necessary functions

def update_earth_dist_text():
    if probe_choice.get() == 2:
        earth_dist["text"] = data_soup.find(id = "voy2_km").text
    else:
        earth_dist["text"] = data_soup.find(id = "voy1_km").text

def update_current_probe_text():
    if probe_choice.get() == 2:
        probe_label["text"] = "Currently Viewing: Voyager 2 Mission Status"
    else:
        probe_label["text"] = "Currently Viewing: Voyager 1 Mission Status"

def update_launch_date():
    print("updating LAUNCH DATE")
    if probe_choice.get() == 2:
        launch_date["text"] = "Sat, 20 Aug 1977 14:29:00 UTC"
    else:
        launch_date["text"] = "Mon, 05 Sept 1977 12:56:00 UTC"

def update_sun_dist_text():
    print("updating SUN DIST")
    if probe_choice.get() == 2:
        distance_from_sun["text"] = data_soup.find(id = "voy2_kms").text
    else:
        distance_from_sun["text"] = data_soup.find(id = "voy1_kms").text

def update_sun_dist_AU_text():
    print("updating SUN DIST AU")
    if probe_choice.get() == 2:
        distance_from_sun_AU["text"] = data_soup.find(id = "voy2_au").text
    else:
        distance_from_sun_AU["text"] = data_soup.find(id = "voy1_au").text

def update_vel_text():
    print("updating VELOCTY TEXT")
    if probe_choice.get() == 2:
        vel["text"] = data_soup.find(id = "voy2_speed").text
    else:
        vel["text"] = data_soup.find(id = "voy1_speed").text

def update_one_way_time():
    print("updating ONE WAY TIME")
    if probe_choice.get() == 2:
        one_way_time["text"] = data_soup.find(id = "voy2_lt").text + " (hh:mm:ss)"
    else:
        one_way_time["text"] = data_soup.find(id = "voy1_lt").text + " (hh:mm:ss)"

def update_elapsed_time():
    print("updating ELAPSED TIME")
    elapsed_time["text"] = ""
    counter = 0
    if probe_choice.get() == 2:
        for i in data_soup.find(id = "countdown_time_v2").contents:
            elapsed_time["text"] += i.contents[0]
            if counter < 6:
                elapsed_time["text"] += " "
            counter += 1
    else:
        for i in data_soup.find(id = "countdown_time_v1").contents:
            elapsed_time["text"] += i.contents[0]
            if counter < 6:
                elapsed_time["text"] += " "
            counter += 1

def open_golden_record_website():
    webbrowser.open("https://voyager.jpl.nasa.gov/golden-record/")

def open_mission_website():
    webbrowser.open("https://voyager.jpl.nasa.gov/mission/status/")

#def ask_nuke():
    #messagebox.askyesnocancel(message = "Would you like to nuke Japan?", icon = "warning", title = "NUKE LAUNCH")

def refresh():
    root.title("Loading...")
    data_soup = get_data.get_data()
    update()
    # print("functionality not added yet")

# def update_instruments():
#     pass

def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About the App")
    about_window.geometry("400x200")
    about_txt = tk.Text(about_window)
    about_txt["width"] = 500
    about_txt["height"] = 100
    about_txt["font"] = title_font
    about_txt.insert("1.0", "Not Affiliated with the National Aeronautics "
                    + "and Space Administration. Developed by Finn Awesome St John in partnership "
                    + "with Google LLC., a subsidiary of Alphabet Inc.")
    about_txt.pack()

def update():
    root.title("Loading...")

    update_current_probe_text()
    update_earth_dist_text()
    update_launch_date()
    update_sun_dist_text()
    update_sun_dist_AU_text()
    update_vel_text()
    update_one_way_time()
    update_elapsed_time()

    root.title("Voyager Mission Tracker")

# Declaring root window

root = tk.Tk()
root.title("Voyager Mission Tracker")
root.geometry("900x500")
root.option_add("*tearOff", "false")
root.resizable("false", "false")

# print(font.families())

frame = tk.Frame(root)
frame.grid()

voy_img_loader = Image.open("voyager.jpg")
voy_img_loader = voy_img_loader.resize((530, 460), Image.ANTIALIAS)
voy_img_pre = ImageTk.PhotoImage(voy_img_loader)
voy_img = tk.Label(frame, image = voy_img_pre)

nasa_logo_loader = Image.open("nasa-logo.jpeg")
nasa_logo_loader = nasa_logo_loader.resize((150, 35), Image.ANTIALIAS)
nasa_logo_pre = ImageTk.PhotoImage(nasa_logo_loader)
nasa_logo = tk.Label(frame, image = nasa_logo_pre)

# Declaring all of the class variables here for use in labels and such

measurement_system = tk.StringVar(frame)
measurement_system.set("imperial")

units_pref = tk.StringVar(frame)
units_pref.set("imperial")

probe_choice = tk.IntVar(frame)

# Declaring all of the tkinter widgets and setting options

main_font = font.Font()
main_font["family"] = "device"
main_font["size"] = 10
main_font["weight"] = "bold"

instrument_font = font.Font()
instrument_font["size"] = 8

title_font = font.Font()
title_font["weight"] = "bold"
title_font["size"] = 11

small_font = font.Font()
small_font["size"] = 7
small_font["family"] = "Consolas"

big_font = font.Font()
big_font["size"] = 14
big_font["family"] = "Consolas"

space_font = font.Font()
space_font["size"] = 8
space_font["family"] = "Lenovo Do Regular"
space_font["weight"] = "bold"

space_font2 = font.Font()
space_font2["size"] = 10
space_font2["family"] = "Lenovo Do Regular"

voy1_btn = tk.Radiobutton(frame)
voy1_btn["text"] = "Voyager 1 Mission Status"
voy1_btn["width"] = 25
voy1_btn["command"] = update
voy1_btn["height"] = 2
voy1_btn["variable"] = probe_choice
voy1_btn["value"] = 1
voy1_btn["indicatoron"] = 0
voy1_btn["font"] = space_font2

voy2_btn = tk.Radiobutton(frame)
voy2_btn["text"] = "Voyager 2 Mission Status"
voy2_btn["width"] = 25
voy2_btn["command"] = update
voy2_btn["height"] = 2
voy2_btn["variable"] = probe_choice
voy2_btn["value"] = 2
voy2_btn["indicatoron"] = 0
voy2_btn["font"] = space_font2

probe_label = tk.Label(frame)
probe_label["text"] = "Currently Viewing: -------------"
probe_label["font"] = main_font
probe_label["justify"] = "left"
probe_label["foreground"] = "#545ED9"
probe_label["width"] = 40
probe_label["pady"] = 3

imperial = tk.Radiobutton(frame)
imperial["text"] = "Imperial"
imperial["variable"] = measurement_system
imperial["value"] = "imperial"
imperial["width"] = 8
imperial["height"] = 2

metric = tk.Radiobutton(frame)
metric["text"] = "Metric"
metric["variable"] = measurement_system
metric["value"] = "metric"
metric["width"] = 8
metric["height"] = 2

earth_dist_title = tk.Label(frame)
earth_dist_title["text"] = "Distance from Earth: "
earth_dist_title["font"] = title_font

earth_dist = tk.Label(frame)
earth_dist["text"] = "--------------"
# earth_dist["font"] = space_font

launch_date_title = tk.Label(frame)
launch_date_title["text"] = "Launch Date: "
launch_date_title["font"] = title_font

launch_date = tk.Label(frame)
launch_date["text"] = "--------------"
# launch_date["font"] = space_font

distance_from_sun_title = tk.Label(frame)
distance_from_sun_title["text"] = "Distance from Sun: "
distance_from_sun_title["font"] = title_font

distance_from_sun = tk.Label(frame)
distance_from_sun["text"] = "--------------"
# distance_from_sun["font"] = space_font

distance_from_sun_AU = tk.Label(frame)
distance_from_sun_AU["text"] = "--------------"
# distance_from_sun_AU["font"] = space_font

distance_from_sun_AU_title = tk.Label(frame)
distance_from_sun_AU_title["text"] = "Distance from Sun (AU): "
distance_from_sun_AU_title["font"] = title_font

vel_title = tk.Label(frame)
vel_title["text"] = "Current Velocity: "
vel_title["font"] = title_font

vel = tk.Label(frame)
vel["text"] = "--------------"
# vel["font"] = space_font

one_way_time_title = tk.Label(frame)
one_way_time_title["text"] = "One-Way Light Time: "
one_way_time_title["font"] = title_font

one_way_time = tk.Label(frame)
one_way_time["text"] = "--------------"
# one_way_time["font"] = space_font

elapsed_time_title = tk.Label(frame)
elapsed_time_title["text"] = "Mission Elapsed Time: "
elapsed_time_title["font"] = title_font

elapsed_time = tk.Label(frame)
elapsed_time["text"] = "------------------------------"
elapsed_time["font"] = big_font

elapsed_time_under = tk.Label(frame)
elapsed_time_under["text"] = "YRS   MOS   DAY   HRS   MIN   SEC  "
elapsed_time_under["font"] = small_font

# crs = tk.Label(frame)
# crs["font"] = instrument_font
# crs["text"] = "-----"
#
# crs_title = tk.Label(frame)
# crs_title["text"] = "CRS"
#
# lecp = tk.Label(frame)
# lecp["font"] = instrument_font
# lecp["text"] = "-----"
#
# lecp_title = tk.Label(frame)
# lecp_title["text"] = "LECP"
#
# mag = tk.Label(frame)
# mag["font"] = instrument_font
# mag["text"] = "-----"
#
# mag_title = tk.Label(frame)
# mag_title["text"] = "MAG"
#
# pws = tk.Label(frame)
# pws["font"] = instrument_font
# pws["text"] = "-----"
#
# pws_title = tk.Label(frame)
# pws_title["text"] = "PWS"
#
# pls = tk.Label(frame)
# pls["font"] = instrument_font
# crs["text"] = "-----"
#
# pls_title = tk.Label(frame)
# pls_title["text"] = "PLS"
#
# iss = tk.Label(frame)
# iss["font"] = instrument_font
# iss["text"] = "-----"
#
# iss_title = tk.Label(frame)
# iss_title["text"] = "ISS"
#
# iris = tk.Label(frame)
# iris["font"] = instrument_font
# iris["text"] = "-----"
#
# iris_title = tk.Label(frame)
# iris_title["text"] = "IRIS"
#
# pps = tk.Label(frame)
# pps["font"] = instrument_font
# pps["text"] = "-----"
#
# pps_title = tk.Label(frame)
# pps_title["text"] = "PPS"
#
# pra = tk.Label(frame)
# pra["font"] = instrument_font
# pra["text"] = "-----"
#
# pra_title = tk.Label(frame)
# pra_title["text"] = "PRA"
#
# uvs = tk.Label(frame)
# uvs["font"] = instrument_font
# uvs["text"] = "-----"
#
# uvs_title = tk.Label(frame)
# uvs_title["text"] = "UVS"

# Create menu bar

menubar = tk.Menu(root)
root["menu"] = menubar
menu_file = tk.Menu(menubar)
menu_view = tk.Menu(menubar)
# menu2_metric = tk.Menu(menu_view)
# menu2_imperial = tk.Menu(menu_view)
menubar.add_cascade(menu = menu_file, label = "File")
menubar.add_cascade(menu = menu_view, label = "View")
menu_file.add_command(label = "Preferences")
menu_file.add_command(label = "Refesh Statistics", command = refresh)
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.destroy)

menu_view.add_command(label = "Explore the Golden Record", command = open_golden_record_website)
menu_view.add_command(label = "Explore the Full Mission Status", command = open_mission_website)
menu_view.add_command(label = "Launch Nuclear ICBM")

menu_view.add_separator()
menu_view.add_radiobutton(label = "Metric", variable = get_data.is_metric, value = "metric")
menu_view.add_radiobutton(label = "Imperial", variable = get_data.is_metric, value = "imperial")

menu_view.add_separator()
menu_view.add_command(label = "About this App", command = open_about_window)

# Mapping the widgets onto the frame

# imperial.grid(column = 4, row = 1)
# metric.grid(column = 3, row = 1)
voy1_btn.grid(column = 1, row = 1)
voy2_btn.grid(column = 2, row = 1)
probe_label.grid(column = 3, row = 1, columnspan = 4)
earth_dist.grid(column = 1, row = 3)
launch_date.grid(column = 2, row = 3)
launch_date_title.grid(column = 2, row = 2)
earth_dist_title.grid(column = 1, row = 2)
distance_from_sun.grid(column = 1, row = 5)
distance_from_sun_title.grid(column = 1, row = 4)
voy_img.grid(column = 3, row = 2, rowspan = 80, columnspan = 50)
nasa_logo.grid(column = 7, row = 1, columnspan = 2)
distance_from_sun_AU_title.grid(column = 2, row = 4)
distance_from_sun_AU.grid(column = 2, row = 5)
vel_title.grid(column = 1, row = 6)
vel.grid(column = 1, row = 7)
one_way_time_title.grid(column = 2, row = 6)
one_way_time.grid(column = 2, row = 7)
elapsed_time_title.grid(column = 1, row = 8, columnspan = 2)
elapsed_time.grid(column = 1, row = 9, columnspan = 2)
elapsed_time_under.grid(column = 1, row = 11, columnspan = 2)

# Running the loop

root.mainloop()
