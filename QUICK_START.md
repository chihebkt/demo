# 🚀 Quick Start Guide

Get the Hello World app running in 2 minutes!

## ⚡ Super Quick Start (Docker)

```bash
# 1. Start the application
docker-compose up -d

# 2. Open your browser
# Frontend: http://localhost:3000
# Backend API Docs: http://localhost:8000/docs

# 3. Stop when done
docker-compose down
```

That's it! 🎉

---

## 📋 Step-by-Step Guide

### Prerequisites Check

```bash
# Check Docker is installed
docker --version
docker-compose --version

# Should show version numbers
```

### Step 1: Start Services

```bash
# Navigate to project directory
cd demo

# Start all services in detached mode
docker-compose up -d

# Expected output:
# ✓ Network hello-world-network created
# ✓ Container hello-world-backend started
# ✓ Container hello-world-frontend started
```

### Step 2: Verify Services

```bash
# Check containers are running
docker-compose ps

# Should show:
# NAME                    STATUS
# hello-world-backend     Up (healthy)
# hello-world-frontend    Up (healthy)
```

### Step 3: Access the Application

**Frontend (React App):**
- URL: http://localhost:3000
- Should display: "🌍 Hello World App" with greeting message

**Backend API:**
- URL: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

### Step 4: Test the API

```bash
# Test hello endpoint
curl http://localhost:8000/hello

# Response:
# {
#   "message": "Hello, World!",
#   "timestamp": "2024-01-01T12:00:00Z",
#   "version": "1.0.0"
# }

# Test health endpoint
curl http://localhost:8000/health

# Response:
# {
#   "status": "healthy",
#   "service": "hello-world-api",
#   "timestamp": "2024-01-01T12:00:00Z"
# }
```

### Step 5: View Logs (Optional)

```bash
# View all logs
docker-compose logs

# View backend logs
docker-compose logs backend

# View frontend logs
docker-compose logs frontend

# Follow logs in real-time
docker-compose logs -f
```

### Step 6: Stop the Application

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

---

## 🛠️ Development Mode

For local development with hot reload:

```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up

# Backend auto-reloads on code changes
# Frontend auto-reloads on code changes
```

---

## 🧪 Run Tests

### Backend Tests

```bash
# Option 1: Inside Docker container
docker-compose exec backend pytest

# Option 2: Local (requires Python 3.11+)
cd backend
pip install -r requirements.txt
pytest
```

### Frontend Tests

```bash
# Option 1: Inside Docker container (dev mode)
docker-compose -f docker-compose.dev.yml exec frontend npm test

# Option 2: Local (requires Node 20+)
cd frontend
npm install
npm test
```

---

## 🔍 Troubleshooting

### Issue: Containers won't start

```bash
# Check what's using the ports
netstat -ano | findstr :3000
netstat -ano | findstr :8000

# Or change ports in docker-compose.yml
```

### Issue: "Network error" in frontend

```bash
# Check backend is running
curl http://localhost:8000/health

# Check logs
docker-compose logs backend
```

### Issue: Need to rebuild

```bash
# Rebuild and restart
docker-compose up -d --build --force-recreate
```

### Issue: Port already in use

```bash
# Stop all containers
docker-compose down

# Kill processes on ports (Windows)
# Find PID: netstat -ano | findstr :3000
# Kill: taskkill /PID <pid> /F
```

---

## 📊 Health Check

```bash
# Check container health
docker-compose ps

# Manual health checks
curl http://localhost:8000/health  # Backend
curl http://localhost:3000/health  # Frontend (Nginx)

# View detailed stats
docker stats hello-world-backend hello-world-frontend
```

---

## 🎯 Next Steps

1. ✅ **Explore the API**: Visit http://localhost:8000/docs
2. ✅ **Modify the code**: Try changing the greeting message
3. ✅ **Run the tests**: Ensure everything still works
4. ✅ **Check CI/CD**: Review `.github/workflows/`
5. ✅ **Read README**: Full documentation in `README.md`

---

## 💡 Pro Tips

### Use Docker Compose Shortcuts

```bash
# Start services
docker-compose up -d

# View logs for specific service
docker-compose logs -f backend

# Restart a service
docker-compose restart backend

# Execute command in container
docker-compose exec backend python --version

# Remove everything (clean slate)
docker-compose down -v --rmi all
```

### Quick Environment Setup

```bash
# Copy environment template
cp .env.example .env

# Edit as needed
notepad .env  # Windows
nano .env     # Linux/Mac
```

### Monitor in Real-Time

```bash
# Terminal 1: Backend logs
docker-compose logs -f backend

# Terminal 2: Frontend logs
docker-compose logs -f frontend

# Terminal 3: Stats
docker stats
```

---

## ✅ Success Checklist

- [ ] Docker and Docker Compose installed
- [ ] Ran `docker-compose up -d`
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend accessible at http://localhost:8000
- [ ] API docs available at http://localhost:8000/docs
- [ ] Health checks passing
- [ ] Can see "Hello, World!" message
- [ ] Tested with `curl http://localhost:8000/hello`

---

**🎉 Congratulations! Your Hello World app is running!**

For more details, see [README.md](README.md)
