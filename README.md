# Campaign Notification Service Clone

A simplified clone of an enterprise Campaign Notification Service built using FastAPI and MongoDB.

The goal of this project is to understand and recreate the architecture and workflows used in production-grade communication systems responsible for email notifications, SMS notifications, communication tracking, and template-based messaging.

---

# Project Overview

This service allows users to:

- Create notification templates
- Send OTP notifications
- Send campaign notifications
- Send order notifications
- Send reminder notifications
- Track notification history
- Track communication status
- Simulate email and SMS delivery

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
    +-------- Communication Tracking APIs
    |
    +-------- Mock Email Service
    |
    +-------- Mock SMS Service
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
Select Template
        |
        v
Render Notification
        |
        v
Send Email / SMS
        |
        v
Create Communication Log
        |
        v
Track Delivery Status
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
│       └── utility.py
│
├── services/
│   ├── email_service.py
│   └── sms_service.py
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
- Docker
- Docker Compose
- Pytest

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
  "template_name": "otp_notification",
  "status": "completed"
}
```

---

## communication_logs

Tracks notification delivery attempts.

Example:

```json
{
  "notification_id": "123",
  "channel": "email",
  "status": "success"
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

Swagger:

```text
http://localhost:8000/docs
```

---

# Health Check

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
Authorization: Basic <base64-credentials>
```

Example credentials:

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
  "recipient": "john@example.com",
  "channel": "email",
  "otp": "123456"
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
  "recipient": "john@example.com",
  "channel": "email",
  "campaign_name": "Summer Rewards"
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
  "recipient": "john@example.com",
  "channel": "email",
  "order_id": "ORDER1001"
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
  "recipient": "john@example.com",
  "channel": "email",
  "days_left": 5
}
```

---

# Communication Tracking APIs

## Get Communication Logs

```http
GET /communication-logs
```

---

## Get Communication Log

```http
GET /communication-logs/{log_id}
```

---

# Mock Communication Services

To keep the project simple and self-contained, notifications are simulated.

## Email Service

Example:

```text
EMAIL SENT
```

---

## SMS Service

Example:

```text
SMS SENT
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
Background Processing
        |
        v
Mock Email / SMS Sent
        |
        v
Communication Log Created
        |
        v
Status Updated
```

---

# Docker Support

## Build

```bash
docker compose build
```

---

## Run

```bash
docker compose up
```

---

## Stop

```bash
docker compose down
```

---

# Testing

Implemented using:

```text
Pytest
FastAPI TestClient
```

---

## Run Tests

```bash
python -m pytest
```

Example:

```text
======================
5 passed
======================
```

---

# Completed Phases

```text
✅ Phase 1 - Foundation Setup

⬜ Phase 2 - Template Management Module

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

✅ Project Structure

✅ Swagger Documentation

---

# Planned Enhancements

## Phase 2

Template Management

- Create Template
- List Templates
- Get Template

---

## Phase 3

Notification Module

- OTP Notifications
- Campaign Notifications
- Order Notifications
- Reminder Notifications

---

## Phase 4

Communication Tracking

- Delivery Logs
- Status Tracking
- Communication History

---

## Phase 5

Mock Notification Providers

- Mock Email Delivery
- Mock SMS Delivery

---

## Phase 6

Docker Support

- Dockerfile
- Docker Compose

---

## Phase 7

Automated Testing

- Health Tests
- Template Tests
- Notification Tests
- Authentication Tests

---

# Learning Outcomes

This project demonstrates:

- FastAPI Development
- REST API Design
- MongoDB CRUD Operations
- Background Task Processing
- Basic Authentication
- Notification Workflows
- Communication Tracking
- Service-Oriented Architecture
- Docker Fundamentals
- API Testing using Pytest

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
Template Rendering
       |
       v
Email / SMS Delivery
       |
       v
Communication Tracking
       |
       v
Delivery History
```

This project demonstrates how enterprise notification systems manage templates, notifications, communication channels, and delivery tracking while keeping the implementation lightweight and easy to understand.