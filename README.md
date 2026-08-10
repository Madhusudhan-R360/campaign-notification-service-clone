# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

The goal of this project is to understand and recreate the architecture and workflows used in production-grade communication systems responsible for notification template management, communication tracking, email/SMS delivery, and event-driven messaging.

---

# Project Overview

This service allows administrators to:

- Create notification templates
- Manage notification templates
- Retrieve notification templates
- Configure notification content
- Build reusable communication workflows

Future phases will introduce notification delivery, communication logs, background processing, Docker support, and automated testing.

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
    +-------- Authentication
    |
    v
MongoDB
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
│   └── templates/
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

# Health Check API

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

# Authentication

The service uses HTTP Basic Authentication similar to the production notification service.

Example:

```http
Authorization: Basic <credentials>
```

Example:

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

# Current Database Flow

```text
Create Template
       |
       v
Validate Request
       |
       v
Insert Into MongoDB
       |
       v
Store Template
       |
       v
Retrieve Template When Required
```

---

# MongoDB Verification

Collection:

```text
notification_templates
```

Example Document:

```json
{
  "_id": "687f123abc456",
  "template_name": "otp_notification",
  "subject": "OTP Verification",
  "content": "Hello {{name}}, your OTP is {{otp}}."
}
```

---

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

✅ Phase 2 - Template Management Module

⬜ Phase 3 - Notification Module

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

✅ Create Template API

✅ Get Templates API

✅ Get Template API

✅ Swagger Documentation

---

# Planned Enhancements

## Phase 3

Notification Module

- OTP Notifications
- Campaign Notifications
- Order Notifications
- Reminder Notifications

---

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
- Async Notification Handling

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
- Authentication Tests
- Notification Tests

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- REST API Design
- MongoDB CRUD Operations
- HTTP Basic Authentication
- Layered Architecture
- Service-Oriented Design
- Notification Template Management

---

# Final Outcome

The Campaign Notification Service Clone aims to recreate the communication layer used in campaign-based platforms.

```text
Notification Event
        |
        v
Template Selection
        |
        v
Template Rendering
        |
        v
Notification Delivery
        |
        v
Communication Tracking
```

Currently, the project supports notification template management and establishes the foundation for future notification delivery and tracking workflows.