# Medical Chatbot API

An AI-powered REST API chatbot for healthcare assistance and information retrieval, built with FastAPI.

## Features

- **Intent Detection**: Automatically identifies user intent from medical queries
- **FAQ Search**: Matches user questions against a knowledge base using similarity matching
- **Confidence Scoring**: Returns confidence levels for matched answers
- **RESTful API**: Easy-to-use HTTP endpoints for integration
- **Docker Support**: Ready-to-deploy with Docker and Docker Compose
- **Fast Performance**: Built on FastAPI for high-speed responses

## Architecture

```
app/
├── main.py                 # FastAPI application setup
├── api/
│   └── routes/
│       └── chatbot.py      # Chatbot API endpoints
├── core/
│   └── config.py           # Application configuration
├── services/
│   ├── chatbot_service.py  # Main chatbot logic
│   ├── intent_detector.py  # Intent detection service
│   └── search_engine.py    # FAQ search functionality
├── schemas/
│   └── chat_schema.py      # Request/Response models
└── data/
    ├── faq_dataset.json    # FAQ knowledge base
    └── synonyms.json       # Synonym mappings
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Docker (optional)

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd RestAPI-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Docker Setup

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

Or build the Docker image manually:
```bash
docker build -t medical-chatbot .
docker run -p 8000:8000 medical-chatbot
```

## Usage

### API Endpoints

#### Root Endpoint
```http
GET /
```
Returns API status and available endpoints.

#### Chat Endpoint
```http
POST /chatbot/chat
Content-Type: application/json

{
  "message": "What are the symptoms of flu?"
}
```

**Response:**
```json
{
  "intent": "symptoms_inquiry",
  "confidence": 0.95,
  "matched_question": "What are the symptoms of the flu?",
  "answer": "Common flu symptoms include fever, cough, fatigue..."
}
```

### Interactive Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Configuration

Edit `.env` file for configuration:
```env
APP_NAME=Medical Chatbot
APP_VERSION=1.0.0
```

## Technologies Used

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI web server
- **Scikit-learn**: Machine learning library
- **RapidFuzz**: Fuzzy string matching
- **Pydantic**: Data validation

## Project Structure

```
RestAPI-bot/
├── Dockerfile              # Docker container configuration
├── docker-compose.yml      # Docker Compose setup
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .gitignore
└── app/                    # Application source code
```

## Development

### Adding New FAQs

Edit `app/data/faq_dataset.json` to add new Q&A pairs:
```json
{
  "faqs": [
    {
      "question": "Your question here",
      "answer": "Your answer here",
      "keywords": ["keyword1", "keyword2"]
    }
  ]
}
```

### Adding Synonyms

Edit `app/data/synonyms.json` for better intent matching:
```json
{
  "symptoms": ["signs", "manifestations", "indicators"],
  "fever": ["high temperature", "body heat"]
}
```

## API Response Format

All endpoints return responses in the following format:

```json
{
  "intent": "detected_intent",
  "confidence": 0.95,
  "matched_question": "matched_question_from_faq",
  "answer": "detailed_answer"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful request
- `400 Bad Request`: Invalid input
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Deployment

### Using Docker

```bash
docker-compose up -d
```

