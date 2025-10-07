# 🌍 Hello World Full-Stack Application

A production-ready Hello World application demonstrating modern full-stack development with complete DevSecOps pipeline.

[![Backend CI/CD](https://img.shields.io/badge/Backend-CI%2FCD-success)](https://github.com/yourusername/hello-world-app)
[![Frontend CI/CD](https://img.shields.io/badge/Frontend-CI%2FCD-success)](https://github.com/yourusername/hello-world-app)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 Features

- ✅ **Backend**: Python FastAPI with async support
- ✅ **Frontend**: React 18 with Vite
- ✅ **Testing**: 80%+ code coverage (pytest + Vitest)
- ✅ **CI/CD**: GitHub Actions with automated testing
- ✅ **Security**: Bandit, Safety, npm audit, Trivy scanning
- ✅ **Docker**: Multi-stage builds, health checks
- ✅ **DevSecOps**: Complete automated pipeline
- ✅ **Documentation**: OpenAPI/Swagger, comprehensive guides

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [API Documentation](#-api-documentation)
- [Security](#-security)
- [Contributing](#-contributing)

## ⚡ Quick Start

### Prerequisites

- Docker & Docker Compose
- (Optional) Python 3.11+ and Node.js 20+ for local development

### Run with Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/hello-world-app.git
cd hello-world-app

# Start the application
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

That's it! The application is now running. 🎉

### Stop the application

```bash
docker-compose down
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│           Frontend (React + Vite)           │
│                                             │
│  • React 18 with modern hooks               │
│  • Vite for fast development                │
│  • Responsive UI with CSS                   │
│  • Error handling & loading states          │
│                                             │
│        http://localhost:3000                │
└─────────────┬───────────────────────────────┘
              │
              │ REST API
              │
┌─────────────▼───────────────────────────────┐
│          Backend (FastAPI)                  │
│                                             │
│  • Python 3.11+ with FastAPI                │
│  • Async/await support                      │
│  • OpenAPI documentation                    │
│  • CORS enabled                             │
│  • Health check endpoints                   │
│                                             │
│        http://localhost:8000                │
└─────────────────────────────────────────────┘
```

### Tech Stack

**Backend:**
- Python 3.11+
- FastAPI 0.104+
- Uvicorn (ASGI server)
- Pydantic (validation)
- pytest (testing)

**Frontend:**
- React 18
- Vite 5
- Vitest (testing)
- ESLint (linting)

**DevOps:**
- Docker & Docker Compose
- GitHub Actions
- Nginx (production)

**Security:**
- Bandit (Python security)
- Safety (dependency check)
- npm audit (Node security)
- Trivy (container scanning)
- ESLint security plugin

## 💻 Development

### Local Development (Without Docker)

**Backend:**

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload

# Access API at http://localhost:8000
# API docs at http://localhost:8000/docs
```

**Frontend:**

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Access app at http://localhost:3000
```

### Development with Docker Compose

```bash
# Start development environment with hot reload
docker-compose -f docker-compose.dev.yml up

# Backend will auto-reload on code changes
# Frontend will auto-reload on code changes
```

## 🧪 Testing

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# View coverage report
open htmlcov/index.html  # On Windows: start htmlcov/index.html
```

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Watch mode
npm run test:watch
```

### Test Coverage Requirements

- Backend: Minimum 80% coverage
- Frontend: Minimum 80% coverage
- All tests must pass before merging

## 🔒 Security

### Security Scanning

**Backend:**
```bash
cd backend

# Security vulnerability scan
bandit -r app/

# Dependency vulnerability check
safety check
```

**Frontend:**
```bash
cd frontend

# Dependency audit
npm audit

# Fix vulnerabilities
npm audit fix
```

**Docker Images:**
```bash
# Scan backend image
trivy image hello-world-backend:latest

# Scan frontend image
trivy image hello-world-frontend:latest
```

### Security Features

- ✅ Non-root Docker containers
- ✅ Security headers (Nginx)
- ✅ CORS configuration
- ✅ Input validation (Pydantic)
- ✅ Dependency scanning
- ✅ Container vulnerability scanning
- ✅ No hardcoded secrets

## 🚀 Deployment

### Production Docker Compose

```bash
# Build and start production containers
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

**Backend:**
- `PYTHONUNBUFFERED=1` - Enable Python logging

**Frontend:**
- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)

### Health Checks

Both services include health check endpoints:

- Backend: `GET /health`
- Frontend: `GET /health`

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend health
curl http://localhost:3000/health
```

## 📚 API Documentation

### Endpoints

**Root Endpoint**
```
GET /
```
Returns API information and available endpoints.

**Hello World**
```
GET /hello
```
Returns greeting message with timestamp.

**Response:**
```json
{
  "message": "Hello, World!",
  "timestamp": "2024-01-01T12:00:00Z",
  "version": "1.0.0"
}
```

**Health Check**
```
GET /health
```
Returns service health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "hello-world-api",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

**Backend CI/CD** (`.github/workflows/ci-backend.yml`)
- ✅ Test on Python 3.11 & 3.12
- ✅ Code coverage reporting
- ✅ Security scanning (Bandit, Safety)
- ✅ Code quality (flake8, pylint, black)
- ✅ Docker image build & scan (Trivy)

**Frontend CI/CD** (`.github/workflows/ci-frontend.yml`)
- ✅ Test on Node 18 & 20
- ✅ Code coverage reporting
- ✅ Linting (ESLint with security plugin)
- ✅ Dependency audit (npm audit)
- ✅ Build optimization
- ✅ Docker image build & scan (Trivy)

### Pipeline Status

View pipeline status in GitHub Actions tab or check badges above.

## 📂 Project Structure

```
hello-world-app/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── __init__.py
│   │   └── tests/          # Backend tests
│   ├── Dockerfile          # Backend container
│   ├── requirements.txt    # Python dependencies
│   ├── pytest.ini          # pytest configuration
│   ├── .bandit            # Security config
│   └── .flake8            # Linting config
├── frontend/               # React frontend
│   ├── src/
│   │   ├── App.jsx        # Main component
│   │   ├── App.test.jsx   # Component tests
│   │   ├── main.jsx       # Entry point
│   │   └── *.css          # Styles
│   ├── public/            # Static assets
│   ├── Dockerfile         # Frontend container
│   ├── nginx.conf         # Nginx configuration
│   ├── package.json       # Node dependencies
│   ├── vite.config.js     # Vite configuration
│   └── .eslintrc.cjs      # ESLint config
├── .github/
│   └── workflows/         # CI/CD pipelines
│       ├── ci-backend.yml
│       └── ci-frontend.yml
├── docker-compose.yml     # Production orchestration
├── docker-compose.dev.yml # Development orchestration
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest` and `npm test`)
5. Run security scans
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Quality Standards

- All tests must pass
- Code coverage must be ≥80%
- Security scans must pass
- Follow existing code style
- Add tests for new features

## 🐛 Troubleshooting

### Backend Issues

**Port 8000 already in use:**
```bash
# Stop the process using port 8000
# On Windows: netstat -ano | findstr :8000
# On Linux/Mac: lsof -i :8000
```

**Import errors:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
```bash
# Change port in vite.config.js or use different port
npm run dev -- --port 3001
```

**Build errors:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Docker Issues

**Containers not starting:**
```bash
# Check logs
docker-compose logs

# Rebuild containers
docker-compose up --build --force-recreate
```

**Network issues:**
```bash
# Reset Docker networks
docker-compose down
docker network prune
docker-compose up
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the amazing Python framework
- React team for the frontend library
- Vite for the blazing-fast build tool
- Docker for containerization
- GitHub Actions for CI/CD

## 📞 Support

For issues and questions:
- 🐛 [Report Bug](https://github.com/yourusername/hello-world-app/issues)
- 💡 [Request Feature](https://github.com/yourusername/hello-world-app/issues)
- 📧 Email: your.email@example.com

---

**Made with ❤️ by Your Name**

⭐ Star this repo if you find it helpful!
