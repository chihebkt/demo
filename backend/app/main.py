"""
FastAPI Hello World Application

A simple but production-ready Hello World API with:
- CORS support
- Health check endpoint
- Structured logging
- OpenAPI documentation
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Dict
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Hello World API",
    description="A simple Hello World API with DevSecOps best practices",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Hello World API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/hello")
async def get_hello() -> Dict[str, str]:
    """
    Get a Hello World message with timestamp.
    
    Returns:
        dict: JSON response with greeting message and timestamp
    """
    logger.info("Hello endpoint accessed")
    return {
        "message": "Hello, World!",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        dict: JSON response with health status
    """
    return {
        "status": "healthy",
        "service": "hello-world-api",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
