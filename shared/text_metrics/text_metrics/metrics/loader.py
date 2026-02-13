from typing import List
from pathlib import Path
import importlib.util
from ..core.metric import Metric

METRIC_NAME_ATTR = "METRIC_NAME"
METRIC_GROUP_ATTR = "METRIC_GROUP"
EXTRACT_FUNC_ATTR = "extract"

def load_from_file(file_path: Path):
    if file_path.name == "__init__.py" or not file_path.suffix == '.py':
        return None
    
    module_name = file_path.stem
    
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        return None
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if not hasattr(module, EXTRACT_FUNC_ATTR):
        return None
    
    extract_func = getattr(module, EXTRACT_FUNC_ATTR)
    
    name = getattr(module, METRIC_NAME_ATTR, module_name)
    group = getattr(module, METRIC_GROUP_ATTR, None)
    
    return Metric(
        name=name,
        group=group,
        extract_func=extract_func,
    )
        
def load_by_directories(directories: List[Path]) -> List[Metric]:
    metrics = []
    
    for directory in directories:
        if not directory.exists():
            raise FileNotFoundError(f"Директория {directory} не найдена")

        for file_path in directory.glob("*.py"):
            metric = load_from_file(file_path)
            if metric:
                metrics.append(metric)
                
    return metrics
    
        
