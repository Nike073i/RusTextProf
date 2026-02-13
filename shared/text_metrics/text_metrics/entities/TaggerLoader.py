import importlib
from pathlib import Path
from text_metrics.core.tagger import Tagger
from typing import List, Optional, Set

TAGGERS_DIR_NAME = "taggers"
TAG_NAME_ATTR = "TAG_NAME"
TAG_FN_ATTR = "tag"

class TaggerLoader:
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = base_path or Path(__file__).parent
        self.taggers_dir = (self.base_path / TAGGERS_DIR_NAME).resolve()
    
    def __load_from_file(self, tagger_path: Path) -> Optional[Tagger]:
        if not tagger_path.exists():
            return None
            
        module_name = tagger_path.stem
        
        if module_name == "__init__" or not tagger_path.suffix == '.py':
            return None
            
        spec = importlib.util.spec_from_file_location(module_name, tagger_path)
        if spec is None or spec.loader is None:
            return None
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        tag_name = getattr(module, TAG_NAME_ATTR, None)
        tag_func = getattr(module, TAG_FN_ATTR, None)
        
        if tag_name is not None and tag_func is not None:
            return Tagger(
                name=tag_name,
                tag_func=tag_func
            )
        
        return None
    
    def load_by_tagger_names(self, names: List[str]) -> List[Tagger]:
        taggers = []
        
        for name in names:
            file_path = self.taggers_dir / f"{name}.py"
            tagger = self.__load_from_file(file_path)
            if tagger:
                taggers.append(tagger)
                
        return taggers
    
    def get_tagger_names(self) -> Set[str]:
        tagger_names = set()
        
        if not self.taggers_dir.exists():
            return tagger_names
        
        for file_path in self.taggers_dir.glob("*.py"):
            if file_path.stem != "__init__":
                tagger_names.add(file_path.stem)
        
        return tagger_names
    