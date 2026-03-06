from pydantic import BaseModel, Field, field_serializer
from typing import Optional, Dict, Any
from datetime import datetime

class ErrorResponse(BaseModel):
    success: bool = False
    error: Dict[str, Any] = Field(
        default_factory=dict,
        description="Детали ошибки"
    )
    timestamp: datetime = Field(default_factory=datetime.now)
    path: Optional[str] = None
    
    @field_serializer('timestamp')
    def serialize_datetime(self, dt):
        return dt.strftime("%d.%m.%Y %H:%M")
