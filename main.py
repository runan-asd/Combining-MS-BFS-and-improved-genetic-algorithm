import sys
import os
import tkinter as tk
import pickle
import pandas as pd
from tkinter import Canvas,font,filedialog,ttk
from PIL import ImageTk


from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx

sys.path.append(os.getcwd() + "/GUI")
sys.path.append(os.getcwd() + "/Objects")

from loginpage import LoginPage


if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)
    root.mainloop()