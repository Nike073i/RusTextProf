from typing import Dict
import yaml


with open("config.yaml") as f:
    cfg = yaml.safe_load(f)

def resolve_config():
    return cfg

class Model:
    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path
    

class ProfilingSection:
    models: Dict[str, Model]
    
    def __init__(self, models):
        self.models = models
    
    @staticmethod
    def from_yaml(config: dict):
        profiling = config.get('profiling', {})
        models = { model["id"]: Model(**model) for model in profiling.get('models', []) }
        
        return ProfilingSection(models=models)
