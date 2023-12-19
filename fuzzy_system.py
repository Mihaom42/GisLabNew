from simpful import *

class FuzzySystemClass:
    def __init__(self, inputs, outputs):
        self.FS = None 
        self.inputs = inputs
        self.outputs = outputs       

    def fuzzy_rules_and_system_create():
        FS = FuzzySystem()

        S_1 = FuzzySet(function=Triangular_MF(a=5, b=15, c=35), term="quiet")
        S_2 = FuzzySet(function=Triangular_MF(a=35, b=40, c=45), term="medium")
        S_3 = FuzzySet(function=Triangular_MF(a=45, b=50, c=60), term="loud")
        FS.add_linguistic_variable("Sound", LinguisticVariable([S_1, S_2, S_3], concept="Laptop sound",
                                                                universe_of_discourse=[5, 60]))
        T_1 = FuzzySet(function=Triangular_MF(a=30, b=30, c=50), term="low")
        T_2 = FuzzySet(function=Triangular_MF(a=55, b=60, c=70), term="medium")
        T_3 = FuzzySet(function=Triangular_MF(a=70, b=85, c=100), term="high")
        FS.add_linguistic_variable("Temperature", LinguisticVariable([T_1, T_2, T_3], concept="Laptop temperature",
                                                                universe_of_discourse=[30, 100]))

        A_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=2), term="young")
        A_2 = FuzzySet(function=Triangular_MF(a=1, b=5, c=6), term="medium")
        A_3 = FuzzySet(function=Triangular_MF(a=4, b=7, c=10), term="old")
        FS.add_linguistic_variable("Age", LinguisticVariable([A_1, A_2, A_3], concept="Laptop age",
                                                                universe_of_discourse=[0, 10]))
        
        B_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=2), term="short")
        B_2 = FuzzySet(function=Triangular_MF(a=1, b=5, c=6), term="normal")
        B_3 = FuzzySet(function=Triangular_MF(a=4, b=7, c=10), term="long")
        FS.add_linguistic_variable("BatteryWorking", LinguisticVariable([B_1, B_2, B_3], concept="Laptop battery",
                                                                universe_of_discourse=[1, 11]))

        FS.add_linguistic_variable("Cleanliness_Failure", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=20), term="small"),
                                                                            FuzzySet(function=Triangular_MF(a=10, b=30, c=40), term="average"),
                                                                            FuzzySet(function=Trapezoidal_MF(a=30, b=40, c=55, d=100), term="high")],
                                                                            universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("Cooling_Failure", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small"),
                                                                            FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average"),
                                                                            FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")],
                                                                            universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("OS_Failure",
                                   LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="small"),
                                                       FuzzySet(function=Triangular_MF(a=20, b=30, c=60), term="average"),
                                                       FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=70, d=100), term="high")],
                                                       universe_of_discourse=[0, 100]))

        FS.add_linguistic_variable("Battery_Failure",
                                   LinguisticVariable([FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small"),
                                                       FuzzySet(function=Triangular_MF(a=5, b=30, c=80), term="average"),
                                                       FuzzySet(function=Trapezoidal_MF(a=70, b=75, c=85, d=100), term="high")],
                                                       universe_of_discourse=[0, 100]))

        R1 = "IF (Temperature IS high) THEN (Cooling_Failure IS high)"
        R2 = "IF (Temperature IS low) AND (Sound IS quiet) OR (Age IS young) AND (BatteryWorking IS short) THEN (Battery_Failure IS high)"
        R3 = "IF (Temperature IS medium) AND (Age IS young) OR (Sound IS medium) AND (BatteryWorking IS normal) THEN (Cooling_Failure IS average)"
        R4 = "IF (Temperature IS medium) AND (Age IS young) OR (Sound IS loud) AND (BatteryWorking IS normal) THEN (Cleanliness_Failure IS high)"
        R5 = "IF (Temperature IS medium) AND (Age IS old) OR (Sound IS medium) AND (BatteryWorking IS normal) THEN (OS_Failure IS high)"
        R6 = "IF (Temperature IS low) AND (Age IS medium) OR (Sound IS quiet) AND (BatteryWorking IS normal) THEN (Battery_Failure IS average)"
        R7 = "IF (Temperature IS low) AND (Age IS old) OR (Sound IS loud) AND (BatteryWorking IS short) THEN (BatteryWorking IS high)"
        FS.add_rules([R1, R2, R3, R4, R5, R6, R7])

        self.FS = FS

    # def use_fuzzy_system(FS):
    #     result_vars = ["Hardware_Failure"]
    #     results = FS.Mamdani_inference(result_vars)
    #     # Возвращаем значения для алгоритма муравьиной колонии в виде списка
    #     return [results[var] for var in result_vars]
    
    def use_fuzzy_system(self, values):
        for text, arg in zip(self.args_in, values):
            self.FS.set_variable(text, arg)
        results = self.FS.Mamdani_inference(self.args_out)
        return results