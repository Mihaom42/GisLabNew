import math
from tkinter import *
from ant_colony import *
from estimate import *

class GUI:
    def __init__(self, length, inputs, outputs):
        #getting data
        self.length = length
        self.inputs = inputs
        self.outputs = outputs

        #window param
        self.window = Tk()
        self.window.columnconfigure([0, 1, 2], minsize=50)
        self.window.rowconfigure([x for x in range(20)], minsize=10)

        self.laptop_arr_of_vars = []

        self.user_data_string = [
            "Age(0 - 15 in years):",
            "Sound(5 - 60 in dB):",
            "Temperature(30-100 in °C):",
            "How long does the charge last(1 - 11 in H): "
        ]

        self.solutions = [ "change_battery", "clean_laptop", "change_cooling_system", "reinstall_OS" ]
        self.laptop_vars = [StringVar() for i in range(self.length)]
        self.graph_vars = [[StringVar() if i != j else None for j in range(len(self.solutions))] for i in range(len(self.solutions))]

        for i in range(len(self.user_data_string)):
            self.show_strings(self.user_data_string[i], i, 0, self.window, self.laptop_vars[i])

        row_numbers = len(self.user_data_string)

        Button(self.window, text = "Result", command = self.get_values).grid(row=row_numbers, column=0)
        self.end_row = row_numbers

    def show_strings(self, text, row, column, window, var, grade = False, input = True):
        Label(text = text).grid(row = row, column=column)
        if grade:
            var.set(5)
        if input:
            Entry(window, textvariable = var).grid(row = row, column=column + 1)

    def get_values(self):
        self.laptop_arr_of_vars = [int(self.laptop_vars[i].get()) for i in range(self.length)]
        self.graph = [[self.graph_vars[i][j].get() if i != j else math.inf for j in range(len(self.solutions))] for i in range(len(self.solutions))]
        solutions_number = [x for x in range(len(self.solutions))]
        best_order = ant_colony_optimization(points=solutions_number, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1, graph=self.graph)
        print(best_order)
        Expert = Estimate_System(self.inputs, self.outputs, self.laptop_arr_of_vars)
        results = Expert.apply_estimate_system()
        self.show_results(results, best_order)

    def show_results(self, results, best_order):
        row_number = 1
        for key,x in zip(results, range(len(self.solutions))):
            self.show_strings(self.solutions[best_order[x]], self.end_row + row_number, self.window, None, input=False)
            self.show_strings(self.get_solution_by_key(self.solutions[best_order[x]], results), self.end_row + row_number, 1, self.window, None, input=False)
            row_number = row_number + 1

    def get_solution_by_key(self, x, results):
        if x == "change_battery":
            return results["Battery_Failure"]
        if x == "clean_laptop":
            return results["Cleanliness_Failure"]
        if x == "change_cooling_system":
            return results["Cooling_Failure"]
        if x == "reinstall_OS":
            return results["OS_Failure"]