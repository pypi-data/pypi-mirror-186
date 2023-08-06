class Metrics():
    def __init__(self, metrics):
        self.metrics = metrics

class FilterMetrics(Metrics):
    def __str__(self):
        passing = self.metrics['All Filters']['Pass']
        failing = self.metrics['All Filters']['Fail']
        total = passing + failing
        pass_metric = f"Pass: {100*passing/total:.2f}% ({passing} examples)"
        fail_metric = f"Fail: {100*failing/total:.2f}% ({failing} examples)"
        return f"{pass_metric}\n{fail_metric}"

class GeneratorMetrics(Metrics):
    def __str__(self):
        rare_types = self.metrics['Rare Types']
        old_coverage = self.metrics['Old Coverage']
        new_coverage = self.metrics['New Coverage']
        num_rare_types = len(rare_types)
        num_types = int(num_rare_types / (1 - old_coverage))
        rare_metric = f"Rare types ({num_rare_types} / {num_types} types): {list(rare_types)}"
        old_metric = f"Original coverage: {100*old_coverage:.2f}%"
        new_metric = f"New coverage: {100*new_coverage:.2f}%"
        return f"{rare_metric}\n{old_metric}\n{new_metric}"