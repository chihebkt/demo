"""
Tests for Hello World API

Test coverage includes:
- Root endpoint
- Hello endpoint
- Health check endpoint
- Response validation
"""
import pytest
from fastapi.testclient import TestClient
from datetime import datetime

from app.main import app

client = TestClient(app)


class TestRootEndpoint:
    """Test cases for root endpoint"""
    
    def test_root_endpoint(self):
        """Test root endpoint returns correct information"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "docs" in data
        assert "health" in data
        assert data["docs"] == "/docs"
        assert data["health"] == "/health"


class TestHelloEndpoint:
    """Test cases for hello endpoint"""
    
    def test_hello_endpoint_returns_200(self):
        """Test hello endpoint returns 200 OK"""
        response = client.get("/hello")
        assert response.status_code == 200
    
    def test_hello_endpoint_returns_json(self):
        """Test hello endpoint returns JSON"""
        response = client.get("/hello")
        assert response.headers["content-type"] == "application/json"
    
    def test_hello_endpoint_message(self):
        """Test hello endpoint returns correct message"""
        response = client.get("/hello")
        data = response.json()
        assert data["message"] == "Hello, World!"
    
    def test_hello_endpoint_has_timestamp(self):
        """Test hello endpoint includes timestamp"""
        response = client.get("/hello")
        data = response.json()
        assert "timestamp" in data
        # Validate timestamp format
        timestamp = data["timestamp"]
        assert timestamp.endswith("Z")
    
    def test_hello_endpoint_has_version(self):
        """Test hello endpoint includes version"""
        response = client.get("/hello")
        data = response.json()
        assert "version" in data
        assert data["version"] == "1.0.0"


class TestHealthEndpoint:
    """Test cases for health check endpoint"""
    
    def test_health_endpoint_returns_200(self):
        """Test health endpoint returns 200 OK"""
        response = client.get("/health")
        assert response.status_code == 200
    
    def test_health_endpoint_returns_healthy_status(self):
        """Test health endpoint returns healthy status"""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"
    
    def test_health_endpoint_has_service_name(self):
        """Test health endpoint includes service name"""
        response = client.get("/health")
        data = response.json()
        assert "service" in data
        assert data["service"] == "hello-world-api"
    
    def test_health_endpoint_has_timestamp(self):
        """Test health endpoint includes timestamp"""
        response = client.get("/health")
        data = response.json()
        assert "timestamp" in data


class TestCORS:
    """Test CORS configuration"""
    
    def test_cors_headers_present(self):
        """Test CORS headers are present in response"""
        response = client.get("/hello")
        # Note: TestClient doesn't send Origin header by default
        # In real scenario, you'd test with actual CORS requests


class TestOpenAPIDocumentation:
    """Test OpenAPI documentation endpoints"""
    
    def test_openapi_json_available(self):
        """Test OpenAPI JSON schema is available"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert data["info"]["title"] == "Hello World API"
    
    def test_swagger_ui_available(self):
        """Test Swagger UI is available"""
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_redoc_available(self):
        """Test ReDoc documentation is available"""
        response = client.get("/redoc")
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=app", "--cov-report=html"])
