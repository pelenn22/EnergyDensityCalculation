import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import pathlib
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import customtkinter as ctk
import datetime as dt
import pandas as pd
from datetime import datetime
import os



class Datasets:
    def __init__(self, master):
        self.master = master
        self.dataset = []
        self.toplabel1 = ctk.CTkLabel(self.master, text="Templates ⓘ")
        self.toplabel1.grid(row=0, column=0, sticky="w")
        self.toplabel2 = ctk.CTkLabel(self.master, text="Plot")
        #self.toplabel2.grid(row=0, column=1, padx=50, sticky="w")
        self.highlighted_label = None
        self.tooltip = Tooltip(self.master, "Click on a template to modify it")
        self.toplabel1.bind("<Enter>", self.tooltip.show)
        self.toplabel1.bind("<Leave>", self.tooltip.hide)
        self.labellist = []
        self.checkbuttonlist = []
        self.datalistall = []

        for i in range(len(self.dataset)):
            self.label = ctk.CTkLabel(self.master, text=str(self.dataset[i]))
            self.labellist.append(self.label)
            self.label.grid(row=i + 1, column=0, columnspan=1, sticky="w")

            self.label.bind("<Button-1>", lambda event, index=i, lbl=self.label: self.select_dataset(event, index, lbl))
            self.checkbutton = ctk.CTkCheckBox(self.master, text="",
                                          command=lambda index=i, lbl=self.label: self.show_plot(index, lbl))
            self.checkbuttonlist.append(self.checkbutton)
            #self.checkbutton.grid(row=i + 1, column=1, padx=50, columnspan=1, sticky="w")


    def gridlines(self):
        for labeli in self.labellist:
            labeli.grid_forget()
        self.labellist = []
        for checki in self.checkbuttonlist:
            checki.grid_forget()
        self.checkbuttonlist = []
        for i in range(len(self.dataset)):
            self.label = ctk.CTkLabel(self.master, text=str(self.dataset[i]))
            self.labellist.append(self.label)
            self.label.grid(row=i + 1, column=0, columnspan=1, sticky="w")

            self.label.bind("<Button-1>",
                            lambda event, index=i, lbl=self.label: self.select_dataset(event, index, lbl))
            self.checkbutton = ctk.CTkCheckBox(self.master, text="",
                                          command=lambda index=i, lbl=self.label: self.show_plot(index, lbl))
            self.checkbuttonlist.append(self.checkbutton)
            #self.checkbutton.grid(row=i + 1, column=1, padx=50, columnspan=1, sticky="w")

    def select_dataset(self, event, index, label):
        highlightcolor = "#3A8EE6"

        if self.highlighted_label is not None:
            self.highlighted_label.configure(fg_color="transparent")

        if label.cget("fg_color") != highlightcolor:
            label.configure(fg_color=highlightcolor)
            self.highlighted_label = label
        else:
            self.highlighted_label = None
        valuelist = self.datalistall[index]
        slider_a.initialize(valuelist[6])
        slider_b.initialize(valuelist[7])
        slider_c.initialize(valuelist[8])
        slider_d.initialize(valuelist[9])
        slider_e.initialize(valuelist[10])
        slider_f.initialize(valuelist[11])
        slider_g.initialize(valuelist[12])
        slider_h.initialize(valuelist[13])
        slider_i.initialize(valuelist[14])
        slider_j.initialize(valuelist[15])
        slider_k.initialize(valuelist[16])
        slider_l.initialize(valuelist[17])
        slider_m.initialize(valuelist[18])
        slider_n.initialize(valuelist[19])
        slider_o.initialize(valuelist[20])
        slider_p.initialize(valuelist[21])
        slider_q.initialize(valuelist[22])
        slider_r.initialize(valuelist[23])
        slider_s.initialize(valuelist[24])
        slider_t.initialize(valuelist[25])
        slider_u.initialize(valuelist[26])
        update_plot()

    def show_plot(self, index, label):
        print("Show plot:", self.dataset[index])

class SliderApp:
    def __init__(self, master):
        self.master = master
        self.lowerb = 0
        self.uperb = 100
        self.step = 100
        # Slider Widget
        self.slider = ctk.CTkSlider(self.master, from_=self.lowerb, to=self.uperb, orientation="horizontal", command=self.update_entry, number_of_steps=self.step)
        self.slider.grid(row=0, column=0, columnspan=3, sticky="e")

        # Entry Widget to set Slider Value
        self.entry = ctk.CTkEntry(self.master, width=50)
        self.entry.bind("<KeyRelease>", self.set_value)

        self.entry.grid(row=1, column=0, columnspan=3)

        self.rounder = 1

        # Unit Label
        self.unit = ctk.CTkLabel(self.master, text="")

        # cathode extra button
        self.catdense_check = ctk.CTkCheckBox(self.master, text="Fixed cathode density", command=self.cathode_density_fix)

    def boundaries(self, lowerb, uperb, step):
        self.lowerb = lowerb
        self.uperb = uperb
        self.step = step
        self.slider.configure(from_=self.lowerb, to=self.uperb, number_of_steps=self.step)

    def update_entry(self, value):
        self.entry.delete(0, tk.END)
        self.entry.configure(fg_color="white")
        if self.rounder == 0:
            self.entry.insert(0, str(int(round(value,self.rounder))))
        else:
            self.entry.insert(0, str(round(value,self.rounder)))
        update_plot()

    def set_value(self, event):
        try:
            value = float(self.entry.get())
            self.entry.configure(fg_color="white")
            if self.lowerb <= value <= self.uperb:
                self.slider.set(value)
                update_plot()
            elif value < 0 or value > self.uperb or value < self.lowerb:
                self.entry.configure(fg_color="red")
                update_plot()
        except ValueError:
            self.entry.configure(fg_color="red")
            update_plot()

    def get(self):
        return self.slider.get()

    def gridpackage(self, row, column, columnspan):
        self.label.grid(row=row, column=column, columnspan=columnspan, sticky="w")
        self.slider.grid(row=row, column=column+1, columnspan=columnspan, sticky="e")
        self.entry.grid(row=row, column=column+2, columnspan=columnspan, sticky="w")
        self.unit.grid(row=row, column=column+3, columnspan=columnspan, sticky="w")

    def cathode_density_extra(self):
        self.slider.grid_forget()
        #self.entry.configure(state='readonly')
        #self.catdense_check.grid(row=4, column=1, columnspan=1, sticky="w")

    def cathode_density_fix(self):
        if self.catdense_check.get() == 1:
            self.entry.configure(state='disabled')
        else:
            self.entry.configure(state='normal')

    def set_unit(self, label):
        self.unit = ctk.CTkLabel(self.master, text=label)

    def set_label(self, label):
        self.label = ctk.CTkLabel(self.master, text=label, anchor="w")

    def initialize(self,value):
        self.slider.set(value)
        self.entry.delete(0, tk.END)
        if self.rounder == 0:
            self.entry.insert(0, str(int(value)))
        else:
            self.entry.insert(0, str(round(value, self.rounder)))

class ResultsTable:
    def __init__(self, master):
        self.master = master
        self.names = ["Energy Density (Wh/L)", "Specific Energy (Wh/kg)", "Cell capacity (Ah)", "Total thickness (mm)", "Total volume (cm³)",
                      "Total weight (g)"]
        self.export_names = ["Column 1",
                             "Energy Density (Wh/L)",
                             "Specific Energy (Wh/kg)",
                             "Cell capacity (Ah)",
                             "Total thickness (mm)",
                             "Total volume (cm³)",
                             "Total weight (g)",
                             "Voltage (V)",
                             "Specific capacity (mAh/g)",
                             "Electrolyte thickness (µm)",
                             "Electrolyte density (g/cm³)",
                             "Anode thickness (µm)",
                             "Anode density (g/cm³)",
                             "Active material content (wt%)",
                             "Active mass loading (mg/cm²)",
                             "Cathode thickness (µm)",
                             "Cathode density (g/cm³)",
                             "Number of layers",
                             "Anode current collector thickness (µm)",
                             "Anode current collector density (g/cm³)",
                             "Cathode current collector thickness (µm)",
                             "Cathode current collector density (g/cm³)",
                             "Casing thickness (µm)",
                             "Casing density (g/cm³)",
                             "Active area (cm²)",
                             "Separator oversizing factor",
                             "Anode oversizing factor",
                             "Casing oversizing factor"]
        self.export_values = []

        self.total_rows = len(self.names)
        self.calculation_result = calculation()  # Call the calculation function once
        self.values = [self.calculation_result[1], self.calculation_result[0], self.calculation_result[2],
                       self.calculation_result[3], self.calculation_result[4], self.calculation_result[5]]

        self.f_entries = []  # List to store entry widgets in the second column

        for i in range(self.total_rows):
            self.e = ctk.CTkEntry(master, width=200, corner_radius=3, border_width=1, font=('Arial', 14))
            self.f = ctk.CTkEntry(master, width=60, corner_radius=3, border_width=1, font=('Arial', 14))
            self.e.grid(row=i, column=0)
            self.f.grid(row=i, column=1)
            self.e.insert(tk.END, self.names[i])
            self.f.insert(tk.END, "0")
            self.e.configure(state='disabled')
            self.f.configure(state='disabled')
            self.f_entries.append(self.f)  # Store entry widget in the list

    def update(self):
        self.calculation_result = calculation()
        self.values = [self.calculation_result[1], self.calculation_result[0], self.calculation_result[2],
                       self.calculation_result[3], self.calculation_result[4], self.calculation_result[5]]
        for i in range(self.total_rows):
            # Retrieve the corresponding value from the calculation results

            if i <= 1:
                updated_value = int(self.values[i])
            elif i == 2:
                updated_value = round(self.values[i], 3)
            else:
                updated_value = round(self.values[i], 1)



            # Get the existing entry widget associated with this row and column
            entry_widget = self.f_entries[i]

            # Update the value in the entry widget
            entry_widget.configure(state='normal')  # Enable the widget for editing
            entry_widget.delete(0, tk.END)
            entry_widget.insert(tk.END, updated_value)
            entry_widget.configure(state='disabled')  # Disable the widget after editing

    def export_results(self):
        self.calculation_result = calculation()  # Call the calculation function once
        self.values = [self.calculation_result[1], self.calculation_result[0], self.calculation_result[2],
                       self.calculation_result[3], self.calculation_result[4], self.calculation_result[5]]
        voltage = round(slider_a.get(), slider_a.rounder)
        specific_capacity = int(round(slider_b.get(), slider_b.rounder))
        electrolyte_thickness = int(round(slider_c.get(), slider_c.rounder))
        electrolyte_density = round(slider_d.get(), slider_d.rounder)
        anode_thickness = int(round(slider_e.get(), slider_e.rounder))
        anode_density = round(slider_f.get(), slider_f.rounder)
        active_material_ctd = int(round(slider_g.get(), slider_g.rounder))
        active_massloading = round(slider_h.get(), slider_h.rounder)
        cathode_thickness = int(round(slider_i.get(), slider_i.rounder))
        cathode_density = round(10 * active_massloading / (0.01 * active_material_ctd * cathode_thickness),2)
        layers = int(round(slider_k.get(), slider_k.rounder))
        anode_cc_thickness = int(round(slider_l.get(), slider_l.rounder))
        anode_cc_density = round(slider_m.get(), slider_m.rounder)
        cathode_cc_thickness = int(round(slider_n.get(), slider_n.rounder))
        cathode_cc_density = round(slider_o.get(), slider_o.rounder)
        casing_thickness = int(round(slider_p.get(), slider_p.rounder))
        casing_density = round(slider_q.get(), slider_q.rounder)
        active_area = round(slider_r.get(), slider_r.rounder)
        separator_oversizing = round(slider_s.get(),slider_s.rounder)
        anode_oversizing = round(slider_t.get(),slider_t.rounder)
        casing_oversizing = round(slider_u.get(),slider_u.rounder)
        self.export_values = [
            "Column 2",
            self.values[0],
            self.values[1],
            self.values[2],
            self.values[3],
            self.values[4],
            self.values[5],
            voltage,
            specific_capacity,
            electrolyte_thickness,
            electrolyte_density,
            anode_thickness,
            anode_density,
            active_material_ctd,
            active_massloading,
            cathode_thickness,
            cathode_density,
            layers,
            anode_cc_thickness,
            anode_cc_density,
            cathode_cc_thickness,
            cathode_cc_density,
            casing_thickness,
            casing_density,
            active_area,
            separator_oversizing,
            anode_oversizing,
            casing_oversizing
        ]
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        # Check if a file path was selected
        if file_path:
            current_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file_path, "w") as file:
                # Write the header with the current date and time
                file.write(f"Dataset saved - {current_datetime}\n")
                # Write the data rows
                data_rows = "\n".join("\t".join(map(str, row)) for row in zip(self.export_names, self.export_values))
                file.write(data_rows)

class CubePlotApp:
    def __init__(self, master):
        self.master = master
        self.fig = plt.figure(2,figsize=(3, 5), facecolor='lightgrey')
        plt.tight_layout()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor('lightgrey')

        #self.colors = ['orange', 'grey', 'yellow', 'black', 'silver']
        self.colors = [(230/255,146/255, 0/255, 0.95), # orange
                       (127/255,126/255,121/255,0.95), # grey
                       (247/255,217/255,67/255,0.95), # yellow
                       (5/255,5/255,2/255,0.95), # black
                       (192/255,192/255,192/255,0.95)] # silver
        self.num_cubes = len(self.colors)
        self.cube_heights = [0.2, 0.1, 0.2, 0.5, 0.1]
        self.position_lst = [0, 0, 0, 0, 0]

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, sticky="w")

        self.update()  # Initial plot

    def plot_cube(self, position, height, color):
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, height],
            [1, 0, height],
            [1, 1, height],
            [0, 1, height]
        ]) + position

        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[7], vertices[6], vertices[2], vertices[3]],
            [vertices[0], vertices[4], vertices[7], vertices[3]],
            [vertices[1], vertices[5], vertices[6], vertices[2]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]
        ]

        cube = Poly3DCollection(faces, facecolors=color, edgecolors='black', linewidths=0.5)
        self.ax.add_collection3d(cube)
        self.ax.view_init(elev=20, azim=10)

    def update(self):
        self.ax.clear()
        self.ax.set_title(f"Single layer \nthickness /µm")
        elthick = slider_c.get()
        anothick = slider_e.get()
        cathick = slider_i.get()
        accolthick = slider_l.get()
        ccolthick = slider_n.get()

        self.cube_heights = [accolthick, anothick, elthick,  cathick,  ccolthick]
        self.position_lst = [0, 0+accolthick, accolthick+anothick, accolthick+anothick+elthick, accolthick+anothick+elthick+cathick]
        for i, color in enumerate(self.colors):
            position = np.array([0, 0, self.position_lst[i]])
            #self.cube_heights[i] = 1
            self.plot_cube(position, self.cube_heights[i], color)
        zlim = 1.2 * (accolthick+anothick+elthick+cathick+ccolthick)
        self.ax.set_xlim([0, 1])
        self.ax.set_ylim([0, 1])
        self.ax.set_zlim([0, zlim])
        #self.ax.set_xlabel('X')
        #self.ax.set_ylabel('Y')
        #self.ax.set_zlabel('Z/µm')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        # Create proxy artists for the legend
        legends = [f"Anode current collector ({int(round(accolthick,0))} µm)", f"Anode ({int(round(anothick,0))} µm)", f"Electrolyte ({int(round(elthick,0))} µm)", f"Cathode ({int(round(cathick,0))} µm)", f"Cathode current collector ({int(ccolthick)} µm)"]
        proxies = [
            plt.Line2D([0], [0], marker='o', color='lightgrey', markerfacecolor=color, markersize=10, label=legends[i]) for
            i, color in enumerate(self.colors)]

        # Add legend below the plot
        legend = self.ax.legend(handles=proxies, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=1)
        #master_bg_color = self.master.cget("fg_color")
        #legend.get_frame().set_facecolor(master_bg_color)
        legend.get_frame().set_facecolor("lightgrey")
        # Adjust legend font size (optional)
        for text in legend.get_texts():
            text.set_fontsize('medium')

        # Manually adjust the layout to ensure the legend is visible
        self.fig.subplots_adjust(bottom=0.25)

        #plt.tight_layout()
        self.canvas.draw()

class ScatterPlotApp:
    def __init__(self, master):
        #initialize()
        self.master = master
        self.fig = plt.figure(1, figsize=(5, 5), facecolor='lightgrey')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('lightgrey')
        self.fig.set_facecolor('lightgrey')
        self.calculation_result = calculation()
        self.endensity = self.calculation_result[1]
        self.specen = self.calculation_result[0]
        self.ax.set_xlabel("Energy Density (Wh/L)")
        self.ax.set_ylabel("Specific Energy (Wh/kg)")
        self.ax.set_xlim([0, 1])
        self.ax.set_ylim([0, 1])
        self.ax.set_aspect('equal')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()
        plt.tight_layout()
        self.canvas.draw()

    def update(self):
        self.calculation_result = calculation()
        self.endensity = self.calculation_result[1]
        self.specen = self.calculation_result[0]
        self.ax.clear()
        self.ax.scatter(self.endensity, self.specen, color="red", s=20)
        self.ax.set_xlabel("Energy Density (Wh/L)")
        self.ax.set_ylabel("Specific Energy (Wh/kg)")
        if appearance_mode_menu.get() == "Dark":
            self.ax.yaxis.label.set_color('white')
            self.ax.xaxis.label.set_color('white')
        self.ax.set_xlim([0, 1500])
        self.ax.set_ylim([0, 1000])
        if self.endensity > 1500:
            self.ax.set_xlim([0, self.endensity+100])
        if self.specen > 1000:
            self.ax.set_ylim([0, self.specen+100])
        self.canvas.draw()

class Tooltip:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.tooltip_visible = False
        self.tooltip_window = None
        self.delayed_show_id = None

    def show(self, event):
        self.delayed_show_id = self.master.after(200, lambda: self._show(event))

    def _show(self, event):
        if not self.tooltip_visible:
            self.tooltip_window = tk.Toplevel(self.master)
            self.tooltip_window.overrideredirect(True)  # Remove window decorations
            self.tooltip_window.withdraw()  # Hide initially
            label = tk.Label(self.tooltip_window, text=self.text, bg="white", relief="solid", borderwidth=1)
            label.pack()

            x = event.widget.winfo_rootx() + 25
            y = event.widget.winfo_rooty() + event.widget.winfo_height() + 5

            self.tooltip_window.geometry(f"+{x}+{y}")
            self.tooltip_window.deiconify()  # Show the tooltip window
            self.tooltip_visible = True

    def hide(self, event):
        if self.delayed_show_id:
            self.master.after_cancel(self.delayed_show_id)
            self.delayed_show_id = None

        if self.tooltip_visible:
            self.tooltip_window.withdraw()  # Hide the tooltip window
            self.tooltip_visible = False

class TooltipImage:
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = image_path
        self.tooltip_visible = False
        self.tooltip_window = None
        self.delayed_show_id = None

    def show(self, event):
        self.delayed_show_id = self.master.after(200, lambda: self._show(event))

    def _show(self, event):
        if not self.tooltip_visible:
            self.tooltip_window = tk.Toplevel(self.master)
            self.tooltip_window.overrideredirect(True)  # Remove window decorations
            self.tooltip_window.withdraw()  # Hide initially

            image = Image.open(self.image_path)
            image = image.resize((400, 350), Image.LANCZOS)  # Resize the image
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(self.tooltip_window, image=photo, relief="solid", borderwidth=1)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack()

            x = event.widget.winfo_rootx() + 25
            y = event.widget.winfo_rooty() + event.widget.winfo_height() - 305

            self.tooltip_window.geometry(f"+{x}+{y}")
            self.tooltip_window.deiconify()  # Show the tooltip window
            self.tooltip_visible = True

    def hide(self, event):
        if self.delayed_show_id:
            self.master.after_cancel(self.delayed_show_id)
            self.delayed_show_id = None

        if self.tooltip_visible:
            self.tooltip_window.withdraw()  # Hide the tooltip window
            self.tooltip_visible = False

def calculation():
    voltage = round(slider_a.get(),slider_a.rounder)
    specific_capacity = round(slider_b.get(),slider_b.rounder)
    electrolyte_thickness = round(slider_c.get(),slider_c.rounder)
    electrolyte_density = round(slider_d.get(),slider_d.rounder)
    anode_thickness = round(slider_e.get(),slider_e.rounder)
    anode_density = round(slider_f.get(),slider_f.rounder)
    active_material_ctd = round(slider_g.get(),slider_g.rounder)
    active_massloading = round(slider_h.get(),slider_h.rounder)
    cathode_thickness = round(slider_i.get(),slider_i.rounder)
    cathode_density = 10*active_massloading/(0.01*active_material_ctd*cathode_thickness)
    layers = round(slider_k.get(),slider_k.rounder)
    #print(layers)
    anode_cc_thickness = round(slider_l.get(),slider_l.rounder)
    anode_cc_density = round(slider_m.get(),slider_m.rounder)
    cathode_cc_thickness = round(slider_n.get(),slider_n.rounder)
    cathode_cc_density = round(slider_o.get(),slider_o.rounder)
    casing_thickness = round(slider_p.get(),slider_p.rounder)
    casing_density = round(slider_q.get(),slider_q.rounder)
    active_area = round(slider_r.get(),slider_r.rounder)
    separator_oversizing = round(slider_s.get(),slider_s.rounder)
    anode_oversizing = round(slider_t.get(),slider_t.rounder)
    casing_oversizing = round(slider_u.get(),slider_u.rounder)

    slider_j.slider.set(cathode_density)
    slider_j.entry.delete(0, tk.END)
    slider_j.entry.insert(0, str(round(cathode_density,2)))

    if slider_j.catdense_check.get() == 1:
        cathode_density = slider_j.slider.get()
        cathode_thickness = 10*active_massloading/(0.01*active_material_ctd*cathode_density)
        slider_i.slider.set(cathode_thickness)
        slider_i.entry.delete(0, tk.END)
        slider_i.entry.insert(0, str(round(cathode_thickness,2)))

    if slider_j.get() > 4:
        slider_j.entry.configure(fg_color="red")
    else:
        slider_j.entry.configure(fg_color="white")

    # unit: mm
    totalthickness = 0.001*(layers*(electrolyte_thickness + anode_thickness + cathode_thickness) + ((layers+1)/2)*(anode_cc_thickness + cathode_cc_thickness) + 2*casing_thickness)

    # unit: cm³
    totalvolume = 0.1*totalthickness*active_area*casing_oversizing

    # unit: g
    totalweight = 0.0001*(layers*(10*active_area*active_massloading/(0.01*active_material_ctd) + anode_density*anode_thickness*active_area*anode_oversizing + electrolyte_density*electrolyte_thickness*active_area*separator_oversizing)
                   + ((layers+1)/2)*(anode_cc_density*anode_cc_thickness*active_area*anode_oversizing + cathode_cc_density*cathode_cc_thickness*active_area)
                   + 2*casing_density*casing_thickness*casing_oversizing*active_area)
    # unit: Wh
    totalenergy = 0.000001*specific_capacity*active_massloading*voltage*active_area*layers

    # unit: Ah

    absolute_capacity = 0.000001*specific_capacity*active_massloading*active_area*layers
    if absolute_capacity < 0.1:
        roundcap = round(absolute_capacity,3)
    else: roundcap = round(absolute_capacity,1)
    # unit: Wh/kg
    specificenergy = 1000*totalenergy/totalweight

    #unit: Wh/L
    energydensity = totalenergy/(0.001*totalvolume)

    # exclude division by zero

    return int(round(specificenergy,0)), int(round(energydensity,0)), roundcap, round(totalthickness,1), round(totalvolume,1), round(totalweight,1)

def update_plot(event=None):
    scatterplot.update()
    cubeplot.update()
    tableofresults.update()
    slider_u.unit.configure(text=f"{round(slider_u.get() * slider_r.get(),1)} cm²")
    slider_s.unit.configure(text=f"{round(slider_s.get() * slider_r.get(),1)} cm²")
    slider_t.unit.configure(text=f"{round(slider_t.get() * slider_r.get(),1)} cm²")
    slider_j.cathode_density_extra()
def export_data():
    print(calculation()[0])
    #np.savetxt("graph_data.csv", np.column_stack((x_vals, y_vals)), delimiter=",")
def save_configuration():
    tableofresults.export_results()
def load_configuration():
    text_files = filedialog.askopenfilenames()
    text_list = list(text_files)
    labellist_all = []
    datasets.datalistall = []
    for record in text_list:
        path = pathlib.PurePath(record)
        labellist_all.append(path.name[:-4])
    datasets.dataset = labellist_all
    datasets.gridlines()

    for item in text_list:
        seti = pd.read_csv(item, sep="\t", header=1, encoding='latin1')
        #seti_list = seti.values.tolist()
        #print(seti['Column 1'].tolist())
        valuelist = seti['Column 2'].tolist()
        datasets.datalistall.append(valuelist)
    #print(datasets.datalistall)
    #print(datasets.datalistall)

def initialize0():
    #start_busy()
    slider_a.initialize(3.5)
    slider_b.initialize(175)
    slider_c.initialize(100)
    slider_d.initialize(1.5)
    slider_e.initialize(50)
    slider_f.initialize(0.54)
    slider_g.initialize(70)
    slider_h.initialize(6)
    slider_i.initialize(65)
    slider_j.initialize(3.0)
    slider_k.initialize(15)
    slider_l.initialize(10)
    slider_m.initialize(9)
    slider_n.initialize(20)
    slider_o.initialize(3)
    slider_p.initialize(100)
    slider_q.initialize(2)
    slider_r.initialize(20)
    slider_s.initialize(1.2)
    slider_t.initialize(1.1)
    slider_u.initialize(1.4)
    update_plot()
    #stop_busy()
def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)
    if new_appearance_mode == "Dark":
        scatterplot.ax.set_facecolor('#302f2f')
        scatterplot.fig.set_facecolor('#302f2f')
        scatterplot.ax.spines['bottom'].set_color('white')
        scatterplot.ax.spines['top'].set_color('white')
        scatterplot.ax.spines['right'].set_color('white')
        scatterplot.ax.spines['left'].set_color('white')
        scatterplot.ax.tick_params(axis='x', colors='white')
        scatterplot.ax.tick_params(axis='y', colors='white')
        scatterplot.ax.yaxis.label.set_color('white')
        scatterplot.ax.xaxis.label.set_color('white')
        scatterplot.canvas.draw()
        cubeplot.ax.set_facecolor('#302f2f')
        cubeplot.fig.set_facecolor('#302f2f')
        cubeplot.ax.spines['bottom'].set_color('white')
        cubeplot.ax.spines['top'].set_color('white')
        cubeplot.ax.spines['right'].set_color('white')
        cubeplot.ax.spines['left'].set_color('white')
        cubeplot.ax.zaxis.line.set_color("white")
        cubeplot.ax.tick_params(axis='x', colors='white')
        cubeplot.ax.tick_params(axis='y', colors='white')
        cubeplot.ax.tick_params(axis='z', colors='white')
        cubeplot.ax.yaxis.label.set_color('white')
        cubeplot.ax.xaxis.label.set_color('white')
        cubeplot.ax.zaxis.label.set_color('white')
        cubeplot.ax.title.set_color('white')
        cubeplot.canvas.draw()

    if new_appearance_mode == "Light":
        scatterplot.ax.set_facecolor('lightgrey')
        scatterplot.fig.set_facecolor('lightgrey')
        scatterplot.ax.spines['bottom'].set_color('black')
        scatterplot.ax.spines['top'].set_color('black')
        scatterplot.ax.spines['right'].set_color('black')
        scatterplot.ax.spines['left'].set_color('black')
        scatterplot.ax.tick_params(axis='x', colors='black')
        scatterplot.ax.tick_params(axis='y', colors='black')
        scatterplot.ax.yaxis.label.set_color('black')
        scatterplot.ax.xaxis.label.set_color('black')
        scatterplot.canvas.draw()
        cubeplot.ax.set_facecolor('lightgrey')
        cubeplot.fig.set_facecolor('lightgrey')
        cubeplot.ax.spines['bottom'].set_color('black')
        cubeplot.ax.spines['top'].set_color('black')
        cubeplot.ax.spines['right'].set_color('black')
        cubeplot.ax.spines['left'].set_color('black')
        cubeplot.ax.zaxis.line.set_color("black")
        cubeplot.ax.tick_params(axis='x', colors='black')
        cubeplot.ax.tick_params(axis='y', colors='black')
        cubeplot.ax.tick_params(axis='z', colors='black')
        cubeplot.ax.yaxis.label.set_color('black')
        cubeplot.ax.xaxis.label.set_color('black')
        cubeplot.ax.zaxis.label.set_color('black')
        cubeplot.ax.title.set_color('black')
        cubeplot.canvas.draw()
def start_busy():
    root.configure(cursor="watch")
    #print("busy")
    #root.after(3000, stop_busy)
def stop_busy():
    root.configure(cursor="arrow")

def resize_mouse(event):
    global scalevalue
    if event.delta > 0:
        scalevalue += 0.1
        ctk.set_widget_scaling(scalevalue)

    if event.delta < 0:
        scalevalue -= 0.1
        ctk.set_widget_scaling(scalevalue)

def on_closing():
    root.destroy()
    os._exit(0)


root = ctk.CTk()
root.protocol("WM_DELETE_WINDOW", on_closing)
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
root.title("ProSpecDense")
root.iconbitmap("icon3.ico")
fullwidth = root.winfo_screenwidth()
fullheight = root.winfo_screenheight()
#root_width = fullwidth-250
root_width = 1400
#root_height = fullheight-150
root_height = 870
xpos = int((fullwidth-root_width)/2)
ypos = int((fullheight-root_height)/2)-20


scalevalue = 1.0
ctk.set_widget_scaling(scalevalue)
#ctk.set_window_scaling(scalevalue)

root.bind("<Control-MouseWheel>", resize_mouse)
#root.geometry("%dx%d" % (fullwidth, fullheight))
#root.geometry(f"{root_width}x{root_height}+{xpos}+{ypos}")
root.geometry(f"{root_width}x{root_height}")
#root.attributes('-fullscreen', True)
#root.attributes('-topmost',0)

### top frame ###
top_frame = ctk.CTkFrame(root, width=140, corner_radius=0)
top_frame.grid(row=0, column=1, columnspan=3,rowspan=1, pady=10, padx=10, sticky="nsew")

### bottom frame ###
bottom_frame = ctk.CTkFrame(root, width=140, corner_radius=0,fg_color="#f0f0f0")
bottom_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")
copyright_label = ctk.CTkLabel(bottom_frame,text=f"© {dt.datetime.now().year} Peter Lennartz, Forschungszentrum Jülich GmbH, Helmholtz-Institute Münster")
copyright_label.grid(row=0, column=0)

# Buttons
button_frame = ctk.CTkFrame(top_frame, width=140, corner_radius=5)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
initializebtn = ctk.CTkButton(button_frame, text="Reset", command=initialize0)
savebtn = ctk.CTkButton(button_frame, text="Save configuration", command=save_configuration)
loadbtn = ctk.CTkButton(button_frame, text="Load configuration(s)", command=load_configuration)
resize_reset_btn = ctk.CTkButton(button_frame, text="Reset scaling", command=lambda: ctk.set_widget_scaling(1.0))


initializebtn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")
savebtn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="n")
loadbtn.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# appearance mode
appearance_frame = ctk.CTkFrame(top_frame, width=140, corner_radius=5)
#appearance_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
appearance_label = ctk.CTkLabel(appearance_frame, text="Appearance mode")
appearance_label.grid(row=0, column=0, padx=10, sticky="nsew")
appearance_mode_menu = ctk.CTkOptionMenu(appearance_frame, values=["Light", "Dark"], command=change_appearance_mode_event)
appearance_mode_menu.grid(row=1, column=0, padx=10, sticky="nsew")

# templates list
scrollable_frame = ctk.CTkScrollableFrame(top_frame, label_text="Data sets")
scrollable_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="w")
scrollable_frame.grid_columnconfigure(2, weight=1)
scrollable_frame_entries = []

# table of results
tableframe = ctk.CTkFrame(top_frame, width=140, corner_radius=0)
tableframe.grid(row=0, column=2, rowspan=2, columnspan=2, padx=10, pady=10, sticky="nsew")

### left frame ###
left_frame = ctk.CTkFrame(root, width=140, corner_radius=0)
left_frame.grid(row=0, column=0,rowspan=2, sticky="nsew", padx=10, pady=10)

### Sub frames ###
frame_headline = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_opper = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_ele = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_ano = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_cat = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_cas = ctk.CTkFrame(left_frame, width=140, corner_radius=0)
frame_geo = ctk.CTkFrame(left_frame, width=140, corner_radius=0)

frame_headline.grid(row=0, column=0, sticky="nsew")
frame_opper.grid(row=1, column=0, sticky="nsew")
frame_ele.grid(row=2, column=0, sticky="nsew")
frame_ano.grid(row=3, column=0, sticky="nsew")
frame_cat.grid(row=4, column=0, sticky="nsew")
frame_cas.grid(row=5, column=0, sticky="nsew")
frame_geo.grid(row=6, column=0, sticky="nsew")

### Headline ###
headline = ctk.CTkLabel(frame_headline, text="Enter Parameters of Your Cell", font=("Arial", 20, "bold"))
headline.grid(row=0, column=0, padx=10, pady=10, sticky="w")

### sliders ###
slider_a = SliderApp(frame_opper)
slider_a.set_label("Operating Voltage")
slider_a.set_unit("V")
slider_a.boundaries(0.1, 5, 50)
tooltip_a = Tooltip(frame_opper, "The average voltage of the cell during discharge")
slider_a.label.bind("<Enter>", tooltip_a.show)
slider_a.label.bind("<Leave>", tooltip_a.hide)
#slider_a.initialize(3.5)

slider_b = SliderApp(frame_opper)
slider_b.set_label("Average Capacity")
slider_b.set_unit("mAh/g")
slider_b.rounder = 0
slider_b.boundaries(1, 1200, 1199)
tooltip_b = Tooltip(frame_opper, "The average specific capacity of the cell during discharge")
slider_b.label.bind("<Enter>", tooltip_b.show)
slider_b.label.bind("<Leave>", tooltip_b.hide)
#slider_b.initialize(175)

slider_c = SliderApp(frame_ele)
slider_c.set_label("Electrolyte thickness")
slider_c.set_unit("µm")
slider_c.boundaries(1, 300, 299)
slider_c.rounder = 0
tooltip_c = Tooltip(frame_ele, "The thickness of the separator/electrolyte membrane")
slider_c.label.bind("<Enter>", tooltip_c.show)
slider_c.label.bind("<Leave>", tooltip_c.hide)
#slider_c.initialize(100)

slider_d = SliderApp(frame_ele)
slider_d.set_label("Electrolyte density")
slider_d.set_unit("g/cm³")
slider_d.boundaries(0.01, 50, 5000)
tooltip_d = Tooltip(frame_ele, "The density of the separator/electrolyte membrane")
slider_d.label.bind("<Enter>", tooltip_d.show)
slider_d.label.bind("<Leave>", tooltip_d.hide)
#slider_d.initialize(1.5)

slider_e = SliderApp(frame_ano)
slider_e.set_label("Anode thickness")
slider_e.set_unit("µm")
slider_e.boundaries(0, 300, 300)
slider_e.rounder = 0
tooltip_e = Tooltip(frame_ano, "The thickness of the anode without current collector")
slider_e.label.bind("<Enter>", tooltip_e.show)
slider_e.label.bind("<Leave>", tooltip_e.hide)
#slider_e.initialize(50)

slider_f = SliderApp(frame_ano)
slider_f.set_label("Anode density")
slider_f.set_unit("g/cm³")
slider_f.boundaries(0.1, 3, 300)
tooltip_f = Tooltip(frame_ano, "The density of the anode without current collector")
slider_f.label.bind("<Enter>", tooltip_f.show)
slider_f.label.bind("<Leave>", tooltip_f.hide)
#slider_f.initialize(0.54)

slider_g = SliderApp(frame_cat)
slider_g.set_label("Active material content")
slider_g.set_unit("wt%")
slider_g.boundaries(1, 100, 99)
slider_g.rounder = 0
tooltip_g = Tooltip(frame_cat, "The active material content of the cathode")
slider_g.label.bind("<Enter>", tooltip_g.show)
slider_g.label.bind("<Leave>", tooltip_g.hide)
#slider_g.initialize(70)

slider_h = SliderApp(frame_cat)
slider_h.set_label("Active mass loading")
slider_h.set_unit("mg/cm²")
slider_h.boundaries(0.1, 150, 1500)
tooltip_h = Tooltip(frame_cat, "The mass of active material per area of the cathode")
slider_h.label.bind("<Enter>", tooltip_h.show)
slider_h.label.bind("<Leave>", tooltip_h.hide)
#slider_h.initialize(6)

slider_i = SliderApp(frame_cat)
slider_i.set_label("Cathode thickness (without current collector)")
slider_i.set_unit("µm")
slider_i.boundaries(1, 400, 399)
slider_i.rounder = 0
tooltip_i = Tooltip(frame_cat, "The thickness of the cathode without current collector")
slider_i.label.bind("<Enter>", tooltip_i.show)
slider_i.label.bind("<Leave>", tooltip_i.hide)
#slider_i.initialize(65)

slider_j = SliderApp(frame_cat)
slider_j.set_label("Cathode density")
slider_j.set_unit("g/cm³")
slider_j.boundaries(0.01, 6, 600)
tooltip_j = Tooltip(frame_cat, "The density of the cathode without current collector")
slider_j.label.bind("<Enter>", tooltip_j.show)
slider_j.label.bind("<Leave>", tooltip_j.hide)
#slider_j.entry.configure(state="disabled")
#slider_j.initialize(3.0)

slider_k = SliderApp(frame_geo)
slider_k.set_label("Layers")
slider_k.set_unit("ⓘ")
tooltip_layers = TooltipImage(frame_geo, "layers.png")
tooltip_k = Tooltip(frame_geo, "The number of anode|electrolyte|cathode layers in the cell")
slider_k.unit.bind("<Enter>", lambda event: tooltip_layers.show(event))
slider_k.unit.bind("<Leave>", lambda event: tooltip_layers.hide(event))
slider_k.label.bind("<Enter>", lambda event: tooltip_k.show(event))
slider_k.label.bind("<Leave>", lambda event: tooltip_k.hide(event))
slider_k.boundaries(1, 100, 99)
slider_k.rounder = 0
#slider_k.initialize(15)

slider_l = SliderApp(frame_ano)
slider_l.set_label("Anode current collector thickness")
slider_l.set_unit("µm")
slider_l.boundaries(0, 100, 100)
slider_l.rounder = 0
tooltip_l = Tooltip(frame_ano, "The thickness of the anode current collector")
slider_l.label.bind("<Enter>", tooltip_l.show)
slider_l.label.bind("<Leave>", tooltip_l.hide)
#slider_l.initialize(0)

slider_m = SliderApp(frame_ano)
slider_m.set_label("Anode current collector density")
slider_m.set_unit("g/cm³")
slider_m.boundaries(0, 12, 1200)
tooltip_m = Tooltip(frame_ano, "The density of the anode current collector")
slider_m.label.bind("<Enter>", tooltip_m.show)
slider_m.label.bind("<Leave>", tooltip_m.hide)
#slider_m.initialize(9)

slider_n = SliderApp(frame_cat)
slider_n.set_label("Cathode current collector thickness")
slider_n.set_unit("µm")
slider_n.boundaries(0, 100, 100)
slider_n.rounder = 0
tooltip_n = Tooltip(frame_cat, "The thickness of the cathode current collector")
slider_n.label.bind("<Enter>", tooltip_n.show)
slider_n.label.bind("<Leave>", tooltip_n.hide)
#slider_n.initialize(20)

slider_o = SliderApp(frame_cat)
slider_o.set_label("Cathode current collector density")
slider_o.set_unit("g/cm³")
slider_o.boundaries(0, 12, 1200)
tooltip_o = Tooltip(frame_cat, "The density of the cathode current collector")
slider_o.label.bind("<Enter>", tooltip_o.show)
slider_o.label.bind("<Leave>", tooltip_o.hide)
#slider_o.initialize(3)

slider_p= SliderApp(frame_cas)
slider_p.set_label("Casing thickness")
slider_p.set_unit("µm")
slider_p.boundaries(0, 200, 200)
slider_p.rounder = 0
tooltip_p = Tooltip(frame_cas, "The thickness of the casing")
slider_p.label.bind("<Enter>", tooltip_p.show)
slider_p.label.bind("<Leave>", tooltip_p.hide)
#slider_p.initialize(100)

slider_q = SliderApp(frame_cas)
slider_q.set_label("Casing density")
slider_q.set_unit("g/cm³")
slider_q.boundaries(0, 12, 1200)
tooltip_q = Tooltip(frame_cas, "The density of the casing")
slider_q.label.bind("<Enter>", tooltip_q.show)
slider_q.label.bind("<Leave>", tooltip_q.hide)
#slider_q.initialize(2)

slider_r = SliderApp(frame_geo)
slider_r.set_label("Active area (single layer)")
slider_r.set_unit("cm²")
slider_r.boundaries(1, 1000, 999)
slider_r.rounder = 0
tooltip_r = Tooltip(frame_geo, "The active area of a single layer of the cell")
slider_r.label.bind("<Enter>", tooltip_r.show)
slider_r.label.bind("<Leave>", tooltip_r.hide)

slider_s = SliderApp(frame_geo)
slider_s.set_label("Separator oversizing factor")
slider_s.set_unit(" ")
slider_s.boundaries(1, 2, 19)
tooltip_s = Tooltip(frame_geo, "The oversizing factor of the separator area")
slider_s.label.bind("<Enter>", tooltip_s.show)
slider_s.label.bind("<Leave>", tooltip_s.hide)

slider_t = SliderApp(frame_geo)
slider_t.set_label("Anode oversizing factor")
slider_t.set_unit(" ")
slider_t.boundaries(1, 2, 19)
tooltip_t = Tooltip(frame_geo, "The oversizing factor of the anode area")
slider_t.label.bind("<Enter>", tooltip_t.show)
slider_t.label.bind("<Leave>", tooltip_t.hide)

slider_u = SliderApp(frame_geo)
slider_u.set_label("Casing oversizing factor")
slider_u.set_unit("")
slider_u.boundaries(1, 2, 19)
tooltip_u = Tooltip(frame_geo, "The oversizing factor of the casing area")
slider_u.label.bind("<Enter>", tooltip_u.show)
slider_u.label.bind("<Leave>", tooltip_u.hide)

# operating parameters
operatingparameters = ctk.CTkLabel(frame_opper, text="Operating parameters", font=("Arial", 15, "bold"))
operatingparameters.grid(row=0, column=0, sticky="W")
slider_a.gridpackage(row=1, column=0, columnspan=1)
slider_b.gridpackage(row=2, column=0, columnspan=1)

# electrolyte parameters
electrolyteparameters = ctk.CTkLabel(frame_ele, text="Electrolyte", font=("Arial", 15, "bold"))
electrolyteparameters.grid(row=0, column=0, sticky="W")
slider_c.gridpackage(1, 0, 1)
slider_d.gridpackage(2, 0, 1)

# anode parameters
anodeparameters = ctk.CTkLabel(frame_ano, text="Anode", font=("Arial", 15, "bold"))
anodeparameters.grid(row=0, column=0, sticky="W")
slider_e.gridpackage(1, 0, 1)
slider_f.gridpackage(2, 0, 1)
slider_l.gridpackage(3, 0, 1)
slider_m.gridpackage(4, 0, 1)

# cathode parameters
cathodeparameters = ctk.CTkLabel(frame_cat, text="Cathode", font=("Arial", 15, "bold"))
cathodeparameters.grid(row=0, column=0, sticky="W")
slider_g.gridpackage(1, 0, 1)
slider_h.gridpackage(2, 0, 1)
slider_i.gridpackage(3, 0, 1)
slider_j.gridpackage(4, 0, 1)
slider_n.gridpackage(5, 0, 1)
slider_o.gridpackage(6, 0, 1)

# casing parameters
casingparameters = ctk.CTkLabel(frame_cas, text="Casing", font=("Arial", 15, "bold"))
casingparameters.grid(row=0, column=0, sticky="W")
slider_p.gridpackage(1, 0, 1)
slider_q.gridpackage(2, 0, 1)

# Cell geometry
cellgeometry = ctk.CTkLabel(frame_geo, text="Cell geometry", font=("Arial", 15, "bold"))
cellgeometry.grid(row=0, column=0, sticky="W")
slider_k.gridpackage(1, 0, 1)
slider_r.gridpackage(2, 0, 1)
slider_s.gridpackage(3, 0, 1)
slider_t.gridpackage(4, 0, 1)
slider_u.gridpackage(5, 0, 1)

# Erstellen Sie das rechte Frame, das die Grafik enthält
frame_figures = ctk.CTkFrame(root)
frame_figures.grid(row=1, column=1, rowspan=2, padx=5, pady=10, sticky="nw")
frame_3d = Frame(root)
frame_3d.grid(row=1, column=2, rowspan=2, padx=5, pady=10, sticky="nw")
# Erstellen Sie die Grafik

datasets = Datasets(scrollable_frame)
scatterplot = ScatterPlotApp(frame_figures)
cubeplot = CubePlotApp(frame_3d)
tableofresults = ResultsTable(tableframe)

initialize0()


root.mainloop()

#for record in text_list:
 #   path = pathlib.PurePath(record)
 #   import_tree2.insert(parent='', index='end', iid=count, text=path.name, values=record)
  #  labellist_all.append(path.name[:-4])
  #  count += 1


### Ideen ###
# Batterie mit dynamischer grafik
# Checkbox neben template treeview, um zu wählen ob konfiguration gezeigt werden soll
