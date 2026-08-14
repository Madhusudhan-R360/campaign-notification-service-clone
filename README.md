# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

This project recreates the core architecture of a production notification platform responsible for managing notification templates, notification requests, communication tracking, background processing, and delivery orchestration.

The application demonstrates modern backend engineering concepts including:

- FastAPI
- MongoDB
- Background Tasks
- REST APIs
- Communication Tracking
- Event-Driven Processing
- Docker
- Containerized Deployment
- Service-Oriented Architecture

---

# Project Overview

The service currently supports:

- Notification Template Management
- Notification Creation
- Communication Tracking
- Communication Status Updates
- Background Processing
- Mock Email Delivery
- Mock SMS Delivery
- HTTP Basic Authentication
- Dockerized Deployment
- MongoDB Persistence

---

# System Architecture

```text
                           Client
                              |
                              v
                        FastAPI API
                              |
      --------------------------------------------------
      |                    |                           |
      v                    v                           v

 Notification       Communication Logs      Background Processor
   Templates
      |                    |                           |
      --------------------------------------------------
                              |
                              v
                           MongoDB
                              |
                ----------------------------
                |                          |
                v                          v
        Mock Email Service        Mock SMS Service
```

---

# Notification Lifecycle

```text
Notification Request
        |
        v
Notification Created
        |
        v
Communication Log Created
        |
        v
Background Task Triggered
        |
        +------ Email Service
        |
        +------ SMS Service
        |
        v
Communication Status Updated
        |
        v
Completed / Failed
```

---

# Project Structure

```text
campaign-notification-service-clone/

├── api/
│   │
│   ├── templates/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   ├── notifications/
│   │   ├── app.py
│   │   ├── schema.py
│   │   └── utility.py
│   │
│   └── communication_logs/
│       ├── app.py
│       ├── schema.py
│       └── utility.py
│
├── db/
│   ├── config.py
│   └── connection.py
│
├── security/
│   └── auth.py
│
├── services/
│   ├── email_service.py
│   ├── sms_service.py
│   └── notification_processor.py
│
├── tests/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
└── README.md
```

---

# Technologies Used

- FastAPI
- MongoDB
- Motor
- Pydantic
- Uvicorn
- HTTP Basic Authentication
- FastAPI Background Tasks
- Docker
- Docker Compose

---

# Database Collections

## notification_templates

Stores reusable notification templates.

Example:

```json
{
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

## notifications

Stores notification requests.

Example:

```json
{
  "recipient": "john@example.com",
  "channel": "email",
  "notification_type": "otp",
  "payload": {
    "otp": "123456"
  },
  "status": "pending"
}
```

---

## communication_logs

Stores communication audit records.

Example:

```json
{
  "notification_id": "689cf123",
  "channel": "email",
  "notification_type": "otp",
  "status": "completed"
}
```

---

# Environment Variables

Create a `.env` file:

```env
MONGO_URL=mongodb://mongo:27017

DATABASE_NAME=campaign_notification_service

BASIC_AUTH_USERNAME=admin

BASIC_AUTH_PASSWORD=admin123
```

---

# Installation (Local Development)

## Clone Repository

```bash
git clone <repository-url>

cd campaign-notification-service-clone
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Activate Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn main:app --reload
```

---

# Swagger Documentation

```text
http://localhost:8000/docs
```

---

# Authentication

The service uses HTTP Basic Authentication.

Example Credentials:

```text
Username: admin

Password: admin123
```

---

# Health API

## Endpoint

```http
GET /health
```

Response:

```json
{
  "success": true
}
```

---

# Template Management APIs

## Create Template

```http
POST /templates
```

Request:

```json
{
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

## Get All Templates

```http
GET /templates
```

---

## Get Template By ID

```http
GET /templates/{template_id}
```

---

# Notification APIs

## Send OTP Notification

```http
POST /notifications/send-otp
```

---

## Send Campaign Notification

```http
POST /notifications/campaign
```

---

## Send Order Notification

```http
POST /notifications/order
```

---

## Send Reminder Notification

```http
POST /notifications/reminder
```

---

## Get All Notifications

```http
GET /notifications
```

---

## Get Notification By ID

```http
GET /notifications/{notification_id}
```

---

# Communication Tracking APIs

## Get All Communication Logs

```http
GET /communication-logs
```

---

## Get Communication Log By ID

```http
GET /communication-logs/{log_id}
```

---

## Update Communication Status

```http
PATCH /communication-logs/{log_id}/status
```

Request:

```json
{
  "status": "completed"
}
```

Valid Statuses:

```text
pending
processing
completed
failed
```

---

# Background Processing

Whenever a notification is created:

```text
Notification Created
        |
        v
Communication Log Created
        |
        v
Background Task Started
        |
        +------ Email Service
        |
        +------ SMS Service
        |
        v
Communication Status Updated
```

---

# Mock Email Service

File:

```text
services/email_service.py
```

Console Output:

```text
EMAIL SENT TO: john@gmail.com
```

---

# Mock SMS Service

File:

```text
services/sms_service.py
```

Console Output:

```text
SMS SENT TO: 9876543210
```

---

# Communication Status Lifecycle

```text
pending
    |
    v
processing
    |
    +----------------+
    |                |
    v                v

completed         failed
```

---

# Docker Setup

## Dockerfile

The application is fully containerized and can run independently inside Docker.

---

## Build Containers

```bash
docker compose build
```

---

## Start Application

```bash
docker compose up
```

Background Mode:

```bash
docker compose up -d
```

---

## Stop Application

```bash
docker compose down
```

---

# Docker Compose Services

```text
FastAPI Application
MongoDB Database
Persistent Docker Volume
```

---

# MongoDB Compass Configuration

MongoDB runs inside Docker.

Expose MongoDB using:

```yaml
mongo:
  image: mongo:7

  ports:
    - "27018:27017"
```

Restart containers:

```bash
docker compose down

docker compose up -d
```

Then connect using Mongo Compass:

```text
mongodb://localhost:27018
```

Database:

```text
campaign_notification_service
```

Collections:

```text
notification_templates

notifications

communication_logs
```

---

# Persistent Storage

MongoDB data persists using Docker volumes:

```yaml
volumes:
  - mongo_data:/data/db
```

This ensures data remains available even after:

```bash
docker compose down
```

and container restarts.

---

# Sample Workflow

```text
POST /notifications/send-otp
            |
            v
Notification Stored
            |
            v
Communication Log Created
            |
            v
Background Task Executed
            |
            v
EMAIL SENT TO: john@gmail.com
            |
            v
Status Updated To Completed
```

---

# Features Implemented

✅ FastAPI Application

✅ MongoDB Integration

✅ Environment Configuration

✅ HTTP Basic Authentication

✅ Template Management

✅ Notification Management

✅ Communication Tracking

✅ Communication Status Updates

✅ Background Processing

✅ Mock Email Delivery

✅ Mock SMS Delivery

✅ Notification Processor

✅ Dockerization

✅ Docker Compose

✅ MongoDB Container

✅ Persistent Database Storage

✅ Swagger Documentation

---

# Project Progress

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Template Management Module

✅ Phase 3 - Notification Module

✅ Phase 4 - Communication Tracking Module

✅ Phase 5 - Background Processing & Mock Delivery

✅ Phase 6 - Dockerization

```

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- MongoDB CRUD Operations
- REST API Design
- HTTP Basic Authentication
- Background Task Processing
- Event-Driven Architecture
- Notification Workflows
- Communication Tracking
- Audit Logging
- Docker Fundamentals
- Containerized Deployment
- Service Layer Design

---

# Final Outcome

The Campaign Notification Service Clone simulates a real-world enterprise communication platform.

```text
Business Event
        |
        v
Notification Request
        |
        v
Notification Creation
        |
        v
Communication Tracking
        |
        v
Background Processing
        |
        +------ Email Delivery
        |
        +------ SMS Delivery
        |
        v
Status Management
        |
        v
Audit Trail
```

The application now closely mirrors the architecture and workflow of a production notification service while remaining lightweight, educational, and easy to extend.