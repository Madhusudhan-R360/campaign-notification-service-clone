# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

The goal of this project is to understand and recreate the architecture and workflows used in production-grade communication systems responsible for notification templates, notification delivery, communication tracking, and event-driven messaging.

---

# Project Overview

This service allows administrators to:

- Create notification templates
- Manage notification templates
- Create notification requests
- Send OTP notifications
- Send campaign notifications
- Send order notifications
- Send reminder notifications
- Track notification requests
- Build reusable communication workflows

Future phases will introduce communication logs, background processing, Docker support, and automated testing.

---

# Architecture

```text
Client
    |
    v
FastAPI
    |
    +-------- Template APIs
    |
    +-------- Notification APIs
    |
    +-------- Authentication
    |
    v
MongoDB
```

---

# Business Flow

```text
Notification Event
        |
        v
Select Notification Type
        |
        v
Create Notification
        |
        v
Store In MongoDB
        |
        v
Notification Status
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
│   └── notifications/
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

Linux / Mac

```bash
source venv/bin/activate
```

Windows

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

# Health Check API

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

# Authentication

The service uses HTTP Basic Authentication similar to the production notification service.

Example:

```http
Authorization: Basic <credentials>
```

Example Credentials:

```text
Username: admin
Password: admin123
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

Response:

```json
{
  "success": true,
  "template_id": "687f123abc456"
}
```

---

## Get Templates

```http
GET /templates
```

---

## Get Template

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
    "order_id": "ORD1001"
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

## Get Notifications

```http
GET /notifications
```

---

## Get Notification

```http
GET /notifications/{notification_id}
```

---

# Sample Templates

## OTP Notification

```json
{
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

## Campaign Notification

```json
{
  "template_name": "campaign_notification",
  "subject": "New Campaign Available",
  "content": "Hello {{name}}, welcome to {{campaign_name}}."
}
```

---

## Order Notification

```json
{
  "template_name": "order_notification",
  "subject": "Order Confirmation",
  "content": "Hello {{name}}, your order {{order_id}} has been placed."
}
```

---

## Reminder Notification

```json
{
  "template_name": "reminder_notification",
  "subject": "Reward Expiry Reminder",
  "content": "Hello {{name}}, your reward expires in {{days_left}} days."
}
```

---

# Current Notification Flow

```text
Notification API Request
          |
          v
Validate Payload
          |
          v
Create Notification
          |
          v
Store In MongoDB
          |
          v
Status = Pending
```

---

# MongoDB Verification

## notification_templates

```json
{
  "_id": "687f123abc456",
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

## notifications

```json
{
  "_id": "687f456abc789",
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

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Template Management Module

✅ Phase 3 - Notification Module

⬜ Phase 4 - Communication Tracking Module

⬜ Phase 5 - Background Processing

⬜ Phase 6 - Dockerization

⬜ Phase 7 - Pytest Testing Suite
```

---

# What Has Been Implemented

✅ FastAPI Application

✅ MongoDB Integration

✅ Environment Configuration

✅ HTTP Basic Authentication

✅ Health Check API

✅ Notification Template Collection

✅ Notification Creation

✅ OTP Notifications

✅ Campaign Notifications

✅ Order Notifications

✅ Reminder Notifications

✅ Notification Retrieval APIs

✅ Swagger Documentation

---

# Planned Enhancements

## Phase 4

Communication Tracking

- Communication Logs
- Notification Status Tracking
- Delivery History

---

## Phase 5

Background Processing

- Mock Email Service
- Mock SMS Service
- Async Notification Processing

---

## Phase 6

Docker Support

- Dockerfile
- Docker Compose

---

## Phase 7

Automated Testing

- Health API Tests
- Template API Tests
- Notification API Tests
- Authentication Tests

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- REST API Design
- MongoDB CRUD Operations
- HTTP Basic Authentication
- Event-Driven Architecture
- Notification Management
- Service-Oriented Design
- Notification Workflow Modeling

---

# Final Outcome

The Campaign Notification Service Clone simulates the communication layer of a campaign ecosystem.

```text
Campaign Event
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
Status Tracking
        |
        v
Future Delivery