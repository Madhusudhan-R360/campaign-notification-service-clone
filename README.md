# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

This project recreates the core architecture of a production notification platform responsible for managing communication templates, notification requests, delivery processing, and communication tracking.

The implementation focuses on learning modern backend concepts such as:

- FastAPI
- MongoDB
- Background Tasks
- Notification Workflows
- Communication Tracking
- Service-Oriented Architecture
- Audit Logging

---

# Project Overview

The service currently supports:

- Notification Template Management
- Notification Creation
- Notification Retrieval
- Communication Tracking
- Communication Status Updates
- Background Processing
- Mock Email Delivery
- Mock SMS Delivery
- HTTP Basic Authentication
- MongoDB Persistence

---

# Architecture

```text
                        Client
                           |
                           v
                      FastAPI API
                           |
       ------------------------------------------------
       |                    |                        |
       v                    v                        v

Notification        Communication         Background Task
Templates              Logs                 Processor
       |                    |                        |
       ------------------------------------------------
                           |
                           v
                      MongoDB
                           |
                           v
               Mock Email / SMS Services
```

---

# Notification Lifecycle

```text
Notification Request
        |
        v
Create Notification
        |
        v
Create Communication Log
        |
        v
Background Task Started
        |
        +------ Email Service
        |
        +------ SMS Service
        |
        v
Update Communication Status
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

---

# Database Collections

## notification_templates

Stores reusable communication templates.

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

Stores communication tracking records.

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

Allowed values:

```text
pending
processing
completed
failed
```

---

# Background Processing

Phase 5 introduces asynchronous notification processing using FastAPI BackgroundTasks.

Whenever a notification is created:

```text
Notification Created
        |
        v
Communication Log Created
        |
        v
Background Task Triggered
        |
        +------ Email Delivery
        |
        +------ SMS Delivery
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

Output:

```text
EMAIL SENT TO: john@gmail.com
```

---

# Mock SMS Service

File:

```text
services/sms_service.py
```

Output:

```text
SMS SENT TO: 9876543210
```

---

# Communication Status Lifecycle

### Initial Status

```text
pending
```

### During Processing

```text
processing
```

### Successful Delivery

```text
completed
```

### Failed Delivery

```text
failed
```

---

# Example Workflow

```text
POST /notifications/send-otp
            |
            v
Notification Created
            |
            v
Communication Log Created
            |
            v
Background Task Runs
            |
            v
EMAIL SENT TO: john@gmail.com
            |
            v
Status Updated To Completed
```

---

# MongoDB Sample Documents

## Notification

```json
{
  "_id": "...",
  "recipient": "john@gmail.com",
  "channel": "email",
  "notification_type": "otp",
  "payload": {
    "otp": "123456"
  },
  "status": "pending"
}
```

---

## Communication Log

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

# Features Implemented

✅ FastAPI Application

✅ MongoDB Integration

✅ Environment Configuration

✅ HTTP Basic Authentication

✅ Health Check Endpoint

✅ Notification Template Management

✅ Notification Creation APIs

✅ Notification Retrieval APIs

✅ Communication Tracking

✅ Communication Log Retrieval

✅ Communication Status Updates

✅ Background Processing

✅ Mock Email Delivery

✅ Mock SMS Delivery

✅ Notification Processor

✅ Swagger Documentation

---

# Project Progress

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Template Management Module

✅ Phase 3 - Notification Module

✅ Phase 4 - Communication Tracking Module

✅ Phase 5 - Background Processing & Mock Delivery Service

⬜ Phase 6 - Dockerization

⬜ Phase 7 - Automated Testing
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
- Service Layer Design

---

# Final Outcome

The Campaign Notification Service Clone simulates a real-world notification platform.

```text
Business Event
        |
        v
Notification Request
        |
        v
Template Selection
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
        +------ Email
        |
        +------ SMS
        |
        v
Status Update
        |
        v
Audit Trail
```

The project now closely mirrors the workflow of