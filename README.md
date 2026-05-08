# Hotel Booking App

A Django REST API for hotel room booking management.

## Project Overview

This is a simple hotel booking application built with Django and Django REST Framework. It allows users to manage hotel rooms and bookings with validation to prevent double bookings.

## Features

- **Room Management**: Create, read, update, and delete hotel rooms
- **Booking Management**: Create, read, update, and delete room bookings
- **Booking Validation**: Prevents overlapping bookings for the same room
- **REST API**: Full RESTful API endpoints for all operations

## Technology Stack

- **Backend**: Django 5.2.7
- **API Framework**: Django REST Framework
- **Database**: SQLite

## Project Structure

```
hotelbookapp/ 
├── manage.py            # Django management script 
├── db.sqlite3           # SQLite database
├── hotelbookapp/        # Main Django project 
│ ├── init.py 
│ ├── settings.py        # Django settings 
│ ├── urls.py            # Main URL configuration 
│ ├── asgi.py 
│ └── wsgi.py 
└── bookroom/            # Booking app 
├── init.py 
├── admin.py             # Django admin configuration 
├── apps.py              # App configuration 
├── models.py            # Database models 
├── serializers.py       # DRF serializers 
├── views.py             # API views 
├── urls.py              # App URL configuration 
└── migrations/          # Database migrations
```

## Models

### Room
- `room_number`: Unique integer identifier for each room

### Booking
- `room`: Foreign key to Room model (room_number)
- `start_date`: Booking start date
- `end_date`: Booking end date

## API Endpoints

The application provides the following REST API endpoints:

- `/api/rooms/` - Room CRUD operations
- `/api/bookings/` - Booking CRUD operations

## API Testing
Test the API using tools like Postman, curl, or the Django REST Framework browsable API at http://localhost:8000/api/.

## Validation Features

- Date Validation: Ensures start date is before end date
- Outdated Validation: Ensures cannot book rooms for past dates.
- Overlap Prevention: Prevents double bookings for the same room
- Error Messages: Provides clear error messages for validation failures