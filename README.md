# ML Model Deployment API with FastAPI & Docker

A production-ready machine learning model serving API built using **FastAPI** and containerized with **Docker**. This project demonstrates how to deploy a trained machine learning model behind a REST API, enabling easy integration with web applications, mobile apps, and other services.

---

## Overview

This project wraps a trained machine learning model inside a RESTful API and packages the entire application using Docker for consistent deployment across environments.

### Key Features

* Fast and lightweight API built with FastAPI
* Machine learning model inference endpoint
* Automatic API documentation with Swagger UI
* Dockerized deployment
* Easy local setup and testing
* Clean project structure
* Production-ready foundation

---

## Project Structure

```text
ml-api-docker/
│
├── app/
│   ├── main.py              # FastAPI application
│   ├── predict.py           # Prediction logic
│   ├── model.pkl            # Trained ML model
│
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── sample_request.json      # Example request payload
├── README.md                # Project documentation
└── .gitignore
```

---

## Architecture

```text
Client
   │
   ▼
FastAPI Application
   │
   ▼
Model Loader
   │
   ▼
Trained ML Model (.pkl)
   │
   ▼
Prediction Result
   │
   ▼
JSON Response
```

### Workflow

1. Client sends a request to the prediction endpoint.
2. FastAPI validates incoming data.
3. Features are passed to the trained model.
4. Model generates predictions.
5. API returns the prediction as a JSON response.

---

## Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| FastAPI      | REST API framework        |
| Scikit-Learn | Machine learning model    |
| Uvicorn      | ASGI server               |
| Docker       | Containerization          |
| Pydantic     | Request validation        |

---

## API Endpoints

### Health Check

**Endpoint**

```http
GET /
```

**Response**

```json
{
  "message": "Model API Running"
}
```

---

### Model Prediction

**Endpoint**

```http
POST /predict
```

**Request Body**

```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

**Success Response**

```json
{
  "prediction": [0]
}
```

---

## Running Locally

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ml-api-docker.git
cd ml-api-docker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / MacOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Application

```bash
uvicorn app.main:app --reload
```

### 6. Access API

Application:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t ml-api .
```

### Verify Image

```bash
docker images
```

### Run Container

```bash
docker run -p 8000:8000 ml-api
```

### Access Application

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Testing the API

### Using cURL

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"feature1\":5.1,\"feature2\":3.5,\"feature3\":1.4,\"feature4\":0.2}"
```

### Sample Output

```json
{
  "prediction": [0]
}
```

---

## Example Request File

Create a file named:

```text
sample_request.json
```

Contents:

```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

Execute:

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d @sample_request.json
```

---

## Docker Commands Reference

### Build Image

```bash
docker build -t ml-api .
```

### Run Container

```bash
docker run -p 8000:8000 ml-api
```

### View Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container_id>
```

### Remove Container

```bash
docker rm <container_id>
```

### Remove Image

```bash
docker rmi ml-api
```

---

## Validation and Error Handling

FastAPI automatically validates incoming requests.

Example invalid request:

```json
{
  "feature1": "invalid"
}
```

Response:

```json
{
  "detail": [
    {
      "type": "float_parsing",
      "msg": "Input should be a valid number"
    }
  ]
}
```

---

## Future Enhancements

* Model versioning
* Authentication and authorization
* Logging and monitoring
* CI/CD pipeline integration
* Kubernetes deployment
* Batch inference endpoints
* Database integration
* Cloud deployment (AWS, Azure, GCP)

---

## Screenshots

### Swagger UI

Add a screenshot after running:

```text
http://localhost:8000/docs
```

Example:

```text
docs/swagger-ui.png
```

---

## Deliverables

This repository contains:

* FastAPI application code
* Trained machine learning model
* Dockerfile
* Requirements file
* Sample request payload
* API documentation
* Docker deployment instructions
* Example API requests and responses

---

## Learning Outcomes

By completing this project, you will gain hands-on experience with:

* Machine Learning Model Deployment
* REST API Development
* FastAPI Framework
* Docker Containerization
* Request Validation
* API Documentation
* Production Deployment Concepts

---

## Author

**Adarsh Chaudhary**

Machine Learning • AI • Backend Development • Product-Focused Engineering

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and professional purposes.

.
.
.

