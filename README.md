# AI API Server

A FastAPI-based API server with WebSocket support, authentication, and task queue capabilities.

## Features

- WebSocket connections for real-time communication
- ELL-AI integration for AI capabilities
- Authentication via Google OAuth and Magic Links
- API key authentication for frontend
- PostgreSQL database integration
- Celery task queue for long-running operations
- Chat, Action, and Submind creation endpoints

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
alembic upgrade head
```

5. Start the services:
```bash
# Start Redis (required for Celery)
redis-server

# Start Celery worker
celery -A app.tasks.celery_app worker --loglevel=info

# Start the API server
uvicorn app.main:app --reload
```

## Frontend Integration

1. API Key Authentication:
   - Add the API key to your frontend requests:
   ```javascript
   const headers = {
     'X-API-Key': 'your-api-key'
   };
   ```

2. WebSocket Connection:
   ```javascript
   const ws = new WebSocket('ws://localhost:8000/chat/ws');
   ws.onmessage = (event) => {
     const response = JSON.parse(event.data);
     console.log(response);
   };
   ```

3. Authentication Flow:
   - Google OAuth:
   ```javascript
   // After getting Google token
   const response = await fetch('/auth/google', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({ token: googleToken })
   });
   ```
   
   - Magic Link:
   ```javascript
   // Request magic link
   await fetch('/auth/magic-link', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({ email: userEmail })
   });

   // Verify magic link token
   const response = await fetch('/auth/verify-magic-link', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({ token: magicLinkToken })
   });
   ```

## API Endpoints

- Authentication:
  - POST `/auth/google` - Google OAuth login
  - POST `/auth/magic-link` - Request magic link
  - POST `/auth/verify-magic-link` - Verify magic link token

- Chat:
  - WebSocket `/chat/ws` - Real-time chat connection
  - POST `/chat/message` - Send message

- Actions:
  - POST `/actions/execute` - Execute action
  - GET `/actions/status/{task_id}` - Get action status

- Subminds:
  - POST `/subminds/create` - Create new submind
  - GET `/subminds/list` - List all subminds