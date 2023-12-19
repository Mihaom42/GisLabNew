# import numpy as np
# from ant_colony import AntColony
# from fuzzy_system import FuzzySystem, LinguisticVariable, FuzzySet, Triangular_MF, Trapezoidal_MF

from GUI import*

Inputs = ["Temperature", "Age", "Sound", "Charging"]
Outputs = ["Cooling_Failure", "Charging_Failure", "OS_Failure"]

App = GUI(len(Inputs), Inputs, Outputs)
App.window.mainloop()


# class HybridSystem:
#     def __init__(self):
#         self.fuzzy_system = self.fuzzy_rules_and_system_create()

#     def fuzzy_rules_and_system_create(self):
#         FS = FuzzySystem()

#         S_1 = FuzzySet(function=Triangular_MF(a=5, b=15, c=35), term="quiet")
#         S_2 = FuzzySet(function=Triangular_MF(a=35, b=40, c=45), term="medium")
#         S_3 = FuzzySet(function=Triangular_MF(a=45, b=50, c=60), term="loud")
#         FS.add_linguistic_variable("Sound", LinguisticVariable([S_1, S_2, S_3], concept="Laptop sound",
#                                                                universe_of_discourse=[5, 60]))
#         S_11 = FuzzySet(function=Triangular_MF(a=30, b=30, c=50), term="low")
#         S_22 = FuzzySet(function=Triangular_MF(a=55, b=60, c=70), term="medium")
#         S_33 = FuzzySet(function=Triangular_MF(a=70, b=85, c=100), term="high")
#         FS.add_linguistic_variable("Temperature", LinguisticVariable([S_11, S_22, S_33], concept="Laptop temperature",
#                                                                      universe_of_discourse=[30, 100]))

#         S_111 = FuzzySet(function=Triangular_MF(a=0, b=0, c=2), term="young")
#         S_222 = FuzzySet(function=Triangular_MF(a=1, b=5, c=6), term="medium")
#         S_333 = FuzzySet(function=Triangular_MF(a=4, b=7, c=10), term="old")
#         FS.add_linguistic_variable("Age", LinguisticVariable([S_111, S_222, S_333], concept="Laptop age",
#                                                              universe_of_discourse=[0, 10]))

#         T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=20), term="small")
#         T_2 = FuzzySet(function=Triangular_MF(a=10, b=30, c=40), term="average")
#         T_3 = FuzzySet(function=Trapezoidal_MF(a=30, b=40, c=55, d=100), term="high")
#         FS.add_linguistic_variable("Hardware_Failure", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0, 100]))

#         R1 = "IF (Temperature IS high) THEN (Hardware_Failure IS high)"
#         R2 = "IF (Temperature IS low) AND (Sound IS quiet) OR (Age IS young) THEN (Hardware_Failure IS small)"
#         R3 = "IF (Temperature IS medium) OR (Age IS young) AND (Sound IS medium) THEN (Hardware_Failure IS average)"
#         R4 = "IF (Temperature IS medium) OR (Age IS young) AND (Sound IS loud) THEN (Hardware_Failure IS high)"
#         R5 = "IF (Temperature IS medium) AND (Age IS old) AND (Sound IS medium) THEN (Hardware_Failure IS average)"
#         R6 = "IF (Temperature IS low) AND (Age IS medium) AND (Sound IS quiet) THEN (Hardware_Failure IS small)"
#         R7 = "IF (Temperature IS low) AND (Age IS old) AND (Sound IS loud) THEN (Hardware_Failure IS high)"
#         FS.add_rules([R1, R2, R3, R4, R5, R6, R7])

#         # Добавим еще одну переменную "City" для примера
#         C_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=1), term="city1")
#         C_2 = FuzzySet(function=Triangular_MF(a=0.5, b=1, c=1.5), term="city2")
#         C_3 = FuzzySet(function=Triangular_MF(a=1, b=2, c=2), term="city3")
#         FS.add_linguistic_variable("City", LinguisticVariable([C_1, C_2, C_3], concept="City",
#                                                              universe_of_discourse=[0, 2]))

#         # Правила для переменной "City"
#         RC1 = "IF (City IS city1) THEN (Hardware_Failure IS small)"
#         RC2 = "IF (City IS city2) THEN (Hardware_Failure IS average)"
#         RC3 = "IF (City IS city3) THEN (Hardware_Failure IS high)"
#         FS.add_rules([RC1, RC2, RC3])

#         return FS

#     def use_hybrid_system(self, sound, temperature, age, city):
#         self.fuzzy_system.set_variable("Sound", sound)
#         self.fuzzy_system.set_variable("Temperature", temperature)
#         self.fuzzy_system.set_variable("Age", age)
#         self.fuzzy_system.set_variable("City", city)

#         fuzzy_result = self.fuzzy_system.Mamdani_inference(["Hardware_Failure"])

#         n_ants = int(fuzzy_result["Hardware_Failure"])

#         # Зададим матрицу расстояний для алгоритма муравьиной колонии
#         distances_matrix = np.array([[0, 0.3, 0.7],
#                                      [0.3, 0, 0.5],
#                                      [0.7, 0.5, 0]])

#         # Создадим экземпляр AntColony с учетом параметров
#         ant_colony = AntColony(distances_matrix, n_ants, 1, 100, 0.95, alpha=1, beta=1)

#         # Запустим алгоритм муравьиной колонии
#         shortest_path = ant_colony.run()

#         return shortest_path

# # Пример использования:
# hybrid_system = HybridSystem()
# result = hybrid_system.use_hybrid_system(59, 99, 19, 1)
# print("Combined result:", result)
