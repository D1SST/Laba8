import tkinter as tk
from tkinter import messagebox
import itertools

class ApplicantDistributorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Набор вакансий.")

        self.women = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']
        self.men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8']

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Набор вакансий")
        self.label.pack()

        self.distribute_button = tk.Button(self.root, text="Выполнить", command=self.distribute)
        self.distribute_button.pack()

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()

    def distribute(self):
        self.clear_options()

        distributor = ApplicantDistributor(self.women, self.men)
        distributor.distribute()

        if distributor.options:
            self.display_options(distributor.options)
        else:
            messagebox.showinfo("No Options", "No valid options found.")

    def display_options(self, options):
        for i, option in enumerate(options, 1):
            option_label = tk.Label(self.options_frame, text=f"Option {i}")
            option_label.pack()

            for specialty, employees in option.items():
                specialty_label = tk.Label(self.options_frame, text=f"{specialty}: {employees}")
                specialty_label.pack()

            separator = tk.Frame(self.options_frame, height=1, bd=1, relief=tk.SUNKEN)
            separator.pack(fill=tk.X, padx=5, pady=5)

    def clear_options(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

class ApplicantDistributor:
    def __init__(self, women, men):
        self.women = women
        self.men = men
        self.options = []

    def distribute(self):
        self.options.clear()

        for women_option in itertools.combinations(self.women, 4):
            remaining_women = [w for w in self.women if w not in women_option]

            for men_option in itertools.combinations(self.men, 6):
                remaining_men = [m for m in self.men if m not in men_option]

                for women_option_specialty3 in itertools.combinations(remaining_women, 2):
                    remaining_women_specialty3 = [w for w in remaining_women if w not in women_option_specialty3]

                    for man_option_specialty3 in itertools.combinations(remaining_men, 1):
                        option = {
                            'Specialty 1 (women)': list(women_option),
                            'Specialty 2 (men)': list(men_option),
                            'Specialty 3': list(women_option_specialty3) + list(man_option_specialty3)
                        }

                        if 'W5' in option['Specialty 1 (women)'] or 'W6' in option['Specialty 1 (women)']:
                            continue

                        if len(option['Specialty 2 (men)']) < 4:
                            continue

                        self.options.append(option)

        for women_option in itertools.combinations(self.women, 4):
            remaining_women = [w for w in self.women if w not in women_option]

            for men_option in itertools.combinations(self.men, 6):
                remaining_men = [m for m in self.men if m not in men_option]

                for woman_option_specialty3 in itertools.combinations(remaining_women, 1):
                    remaining_women_specialty3 = [w for w in remaining_women if w != woman_option_specialty3[0]]

                    for men_option_specialty3 in itertools.combinations(remaining_men, 2):
                        option = {
                            'Specialty 1 (women)': list(women_option),
                            'Specialty 2 (men)': list(men_option),
                            'Specialty 3': list(woman_option_specialty3) + list(men_option_specialty3)
                        }

                        if 'W5' in option['Specialty 1 (women)'] or 'W6' in option['Specialty 1 (women)']:
                            continue

                        if len(option['Specialty 2 (men)']) < 4:
                            continue

                        self.options.append(option)

root = tk.Tk()
app = ApplicantDistributorGUI(root)
root.mainloop()