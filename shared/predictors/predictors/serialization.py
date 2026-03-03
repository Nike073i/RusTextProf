import json
import pickle


def write_model(path, model):
    with open(path.with_suffix(".pkl"), 'wb') as file:
        pickle.dump(model, file)
    
def write_dict(path, data):
    with open(path.with_suffix(".json"), 'w') as file:
        json.dump(data, file)

def save_model(base_dir, model, name, model_params = None, scores = None):
    if not base_dir.exists():
        return FileNotFoundError("Папка с моделями не найдена")
    
    model_dir = base_dir / name
    model_dir.mkdir()
    
    write_model(model_dir / "model", model)
    
    if model_params:
        write_dict(model_dir / "params", model_params)
    
    if scores:
        write_dict(model_dir / "scores", scores)


def load_model(path):
    with open(path, 'rb') as file:
        return pickle.load(file)