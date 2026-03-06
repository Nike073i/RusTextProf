from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from modules.profiling.api.v1.routes import router as profiling_v1
from core.error_handlers import setup_error_handlers

rootRouter = APIRouter(prefix='/api')
rootRouter.include_router(profiling_v1)

app = FastAPI()
setup_error_handlers(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(rootRouter)
