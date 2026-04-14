# MonitorAgent

MonitorAgent is a web application for managing and monitoring software agents. It provides a backend API built with FastAPI for agent registration, status updates, and health monitoring, along with a user-friendly web interface built with Gradio. The system uses AI-powered health summaries to analyze agent status logs and provide insights.

## Features

- **Agent Management**: Register new agents with name and type
- **Status Tracking**: Update and track agent statuses with detailed logs
- **Health Monitoring**: AI-generated health summaries for each agent based on status history
- **Web Interface**: Simple UI for managing agents without API knowledge
- **Secure Authentication**: Token-based authentication for API access
- **Database Integration**: PostgreSQL database for persistent storage
- **Container Support**: Docker containerization for easy deployment

## Tech Stack

### Backend

- **FastAPI**: Modern Python web framework for building APIs
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Relational database (using Neon for serverless hosting)
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server for running FastAPI

### Frontend

- **Gradio**: Python library for creating web interfaces

### AI Integration

- **Groq API**: For generating health summaries using the compound-mini model

### Security

- **PyJWT**: JSON Web Token handling (prepared for future JWT authentication)
- **HTTP Bearer**: Token-based authentication

### Other

- **httpx**: Async HTTP client for API calls
- **python-dotenv**: Environment variable management
- **Docker**: Containerization

## Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL database (or Neon account for cloud database)
- Groq API key

### Quick Setup (Windows)

1. Clone the repository:

   ```
   git clone <repository-url>
   cd MonitorAgent
   ```

2. Run the setup script:

   ```
   setup.bat
   ```

   This will:
   - Check Python installation
   - Create a virtual environment
   - Install dependencies
   - Create a `.env` file template

3. Configure environment variables in `.env`:
   ```
   DATABASE_URL=postgresql://user:password@host:port/database
   API_TOKEN=your_secure_api_token
   GROQ_API_KEY=your_groq_api_key
   ```

### Manual Setup

1. Create a virtual environment:

   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (see above)

## Usage

### Running the Application

1. Start the FastAPI server:

   ```
   python -m uvicorn src.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

2. In a separate terminal, start the Gradio UI:
   ```
   python src/app.py
   ```
   The web interface will be available at `http://localhost:7860`

### Using the Web Interface

- **Create Agent**: Enter agent name and type
- **Update Status**: Provide agent ID and new status
- **List Agents**: View all agents with their health summaries

### API Endpoints

All API endpoints require authentication via Bearer token in the Authorization header.

- `POST /agents` - Register a new agent
  - Body: `{"name": "string", "type": "string"}`

- `PATCH /agents/{agent_id}` - Update agent status
  - Body: `{"status": "string"}`

- `GET /agents` - List all agents with health summaries

## Architecture

The application follows a modular architecture:

- `src/main.py`: FastAPI application with API endpoints
- `src/models.py`: Database models using SQLAlchemy
- `src/database.py`: Database connection and session management
- `src/auth.py`: Authentication middleware
- `src/jwt_auth.py`: JWT token utilities (for future enhancement)
- `src/llm.py`: AI integration for health summaries
- `src/app.py`: Gradio web interface

The system uses PostgreSQL for data persistence, with tables created automatically on startup. Authentication is currently implemented as simple token verification, with JWT support prepared for more advanced scenarios.

## Docker Deployment

Build and run with Docker:

```
docker build -t monitoragent .
docker run -p 8000:8000 monitoragent
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

See LICENSE file for details.
