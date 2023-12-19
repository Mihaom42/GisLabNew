from fuzzy_system import*

class Estimate_System:
    def __init__(self, inputs, outputs, values):
        self.inputs = inputs
        self.outputs = outputs
        self.values = values
        self.FSI = FuzzySystemClass(self.inputs, self.outputs)
        self.FSI.fuzzy_rules_and_system_create()

    def apply_estimate_system(self):
        results = self.FSI.use_fuzzy_system(self.values)
        self.results = results
        return results
    