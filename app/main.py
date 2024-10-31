from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, chat, actions, subminds
from .core.config import settings
from .core.security import verify_api_key

app = FastAPI(title="AI API Server")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(
    chat.router, 
    prefix="/chat", 
    tags=["chat"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    actions.router, 
    prefix="/actions", 
    tags=["actions"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    subminds.router, 
    prefix="/subminds", 
    tags=["subminds"],
    dependencies=[Depends(verify_api_key)]
)