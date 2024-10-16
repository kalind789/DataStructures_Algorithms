import tkinter as tk
from tkinter import ttk
import random
from SortAlgos.SortingAlgorithm import SortingAlgorithm  # Import SortingAlgorithm class

class SortingVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, width=700, height=400, bg="white")
        self.canvas.pack(pady=20)
        
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.data = []
        self.speed = 50

        # Initialize control widgets
        self.init_controls()
        self.reset_array()

    def init_controls(self):
        # Sorting algorithm options (Dropdown)
        algorithm_label = tk.Label(self.control_frame, text="Algorithm: ")
        algorithm_label.grid(row=0, column=0, padx=5, pady=5)
        self.algorithm_var = tk.StringVar()
        algorithm_menu = ttk.Combobox(self.control_frame, textvariable=self.algorithm_var, values=["Bubble Sort", "Selection Sort"])
        algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
        algorithm_menu.current(0)

        # Speed Slider
        speed_label = tk.Label(self.control_frame, text="Speed (ms): ")
        speed_label.grid(row=1, column=0, padx=5, pady=5)
        self.speed_slider = tk.Scale(self.control_frame, from_=10, to=1000, length=200, orient='horizontal')
        self.speed_slider.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        start_button = tk.Button(self.control_frame, text="Start", command=self.start_sorting)
        start_button.grid(row=2, column=0, padx=5, pady=5)

        reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_array)
        reset_button.grid(row=2, column=1, padx=5, pady=5)

        quit_button = tk.Button(self.control_frame, text="Quit", command=quit)
        quit_button.grid(row=2, column=2, padx=5, pady=5)

    def draw_array(self, color_array):
        self.canvas.delete("all")
        c_width = 700
        c_height = 400
        bar_width = c_width / (len(self.data) + 1)
        offset = 30
        spacing = 5

        normalized_data = [i / max(self.data) for i in self.data]

        for i, height in enumerate(normalized_data):
            x0 = i * bar_width + spacing + offset
            y0 = c_height - height * 350
            x1 = (i + 1) * bar_width + offset
            y1 = c_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        
        self.root.update_idletasks()

    def reset_array(self):
        self.data = [random.randint(10, 100) for _ in range(30)]
        self.draw_array(["blue" for _ in range(len(self.data))])

    def start_sorting(self):
        algorithm = self.algorithm_var.get()
        if algorithm == "Bubble Sort":
            self.sorting_algorithm = SortingAlgorithm(self)
            self.sorting_algorithm.bubble_sort_step(0, 0)
        elif algorithm == "Selection Sort":
            self.sorting_algorithm = SortingAlgorithm(self)
            self.sorting_algorithm.min_idx = 0
            self.sorting_algorithm.selection_sort_step(0,0)