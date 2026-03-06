from fastapi import APIRouter
from .list_available_models.list_available_models import register as reg_list_of_available_models 
from .extract_text_metrics.extract_text_metrics import register as reg_extract_text_metrics 
from .predict.predict import register as reg_predict_profile 

router = APIRouter(prefix="/v1/profiling")
reg_list_of_available_models(router)
reg_extract_text_metrics(router)
reg_predict_profile(router)
