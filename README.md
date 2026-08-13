# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

This project is designed to replicate the core architecture and workflows of a production notification service used to manage communication events, notification templates, delivery tracking, and notification auditing.

---

# Project Overview

The service currently supports:

- Notification Template Management
- Notification Creation
- Communication Tracking
- Notification Status Updates
- HTTP Basic Authentication
- MongoDB Persistence

Future phases will introduce:

- Background Processing
- Mock Email Delivery
- Mock SMS Delivery
- Docker Support
- Automated Testing

---

# Architecture

```text
Client
    |
    v
FastAPI
    |
    +-------- Template Module
    |
    +-------- Notification Module
    |
    +-------- Communication Tracking Module
    |
    +-------- Authentication Module
    |
    v
MongoDB
```

---

# Business Flow

```text
Notification Request
        |
        v
Create Notification
        |
        v
Store Notification
        |
        v
Create Communication Log
        |
        v
Track Status
```

---

# Project Structure

```text
campaign-notification-service-clone/

├── main.py
│
├── db/
│   ├── config.py
│   └── connection.py
│
├── security/
│   └── auth.py
│
├── api/
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
├── tests/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
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

---

# MongoDB Collections

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
  "notification_id": "689cf12345",
  "channel": "email",
  "notification_type": "otp",
  "status": "pending"
}
```

---

# Environment Variables

Create a `.env` file:

```env
MONGO_URL=mongodb://localhost:27017

DATABASE_NAME=campaign_notification_service

BASIC_AUTH_USERNAME=admin

BASIC_AUTH_PASSWORD=admin123
```

---

# Installation

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

## Activate Virtual Environment

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

# Run Application

```bash
uvicorn main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Authentication

The service uses HTTP Basic Authentication similar to the production notification service.

Example:

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

Response

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

Request:

```json
{
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "otp",
  "payload": {
    "otp": "123456"
  }
}
```

---

## Send Campaign Notification

```http
POST /notifications/campaign
```

Request:

```json
{
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "campaign",
  "payload": {
    "campaign_name": "Summer Rewards"
  }
}
```

---

## Send Order Notification

```http
POST /notifications/order
```

Request:

```json
{
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "order",
  "payload": {
    "order_id": "ORDER1001"
  }
}
```

---

## Send Reminder Notification

```http
POST /notifications/reminder
```

Request:

```json
{
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "reminder",
  "payload": {
    "days_left": 5
  }
}
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

Response Example:

```json
[
  {
    "_id": "689cf123456",
    "notification_id": "689cf123455",
    "channel": "email",
    "notification_type": "otp",
    "status": "pending"
  }
]
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

Allowed Status Values:

```text
pending
processing
completed
failed
```

Response:

```json
{
  "success": true,
  "message": "Status updated"
}
```

---

# Communication Lifecycle

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
Status Updated
        |
        v
Audit Trail Maintained
```

---

# MongoDB Verification

## notification_templates

```json
{
  "_id": "...",
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

## notifications

```json
{
  "_id": "...",
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "otp",
  "status": "pending"
}
```

---

## communication_logs

```json
{
  "_id": "...",
  "notification_id": "...",
  "channel": "email",
  "notification_type": "otp",
  "status": "completed"
}
```

---

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Template Management Module

✅ Phase 3 - Notification Module

✅ Phase 4 - Communication Tracking Module

⬜ Phase 5 - Background Processing & Mock Delivery

⬜ Phase 6 - Dockerization

⬜ Phase 7 - Automated Testing
```

---

# Features Implemented

✅ FastAPI Application

✅ MongoDB Integration

✅ Environment Configuration

✅ HTTP Basic Authentication

✅ Health Check Endpoint

✅ Notification Template Management

✅ Notification Creation APIs

✅ Notification Retrieval APIs

✅ Communication Log Creation

✅ Communication Audit Tracking

✅ Communication Status Updates

✅ Swagger Documentation

---

# Upcoming Enhancements

## Phase 5

Background Processing & Mock Delivery

- Background Tasks
- Mock Email Delivery
- Mock SMS Delivery
- Automatic Status Updates

---

## Phase 6

Docker Support

- Dockerfile
- Docker Compose
- Containerized Deployment

---

## Phase 7

Testing

- Health API Tests
- Template API Tests
- Notification API Tests
- Communication Log Tests

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- REST API Design
- MongoDB CRUD Operations
- Event-Driven Architecture
- Communication Tracking
- Audit Logging
- Authentication
- Service-Oriented Design

---

# Final Outcome

The Campaign Notification Service Clone models the communication layer of a rewards ecosystem.

```text
Campaign Event
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
Status Management
        |
        v
Audit Trail
```

The project now provides a complete foundation for notification management and communication tracking, closely mirroring the core architecture of an enterprise notification service.