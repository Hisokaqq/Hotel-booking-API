# Hotel Booking System

This project is a Django-based REST API for managing hotel bookings, rooms, and users. It includes models for hotels, rooms, bookings, payments, and user profiles, and provides CRUD operations through Django REST framework viewsets.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Models](#models)
  - [UserProfile](#userprofile)
  - [Hotel](#hotel)
  - [Room](#room)
  - [Booking](#booking)
  - [Payment](#payment)
- [Views](#views)
  - [HotelViewSet](#hotelviewset)
  - [RoomViewSet](#roomviewset)
  - [BookingViewSet](#bookingviewset)
- [API Endpoints](#api-endpoints)
- [Settings](#settings)
- [Additional Notes](#additional-notes)
- [Running Tests](#running-tests)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hotel_booking_system.git
    cd hotel_booking_system
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Requirements

- Django==5.1
- djangorestframework==3.14.0

## Models

### UserProfile

Represents a profile for each user, extending the default Django `User` model with additional fields.

- **Fields**:
  - `user`: One-to-one relationship with the Django `User` model.
  - `phone_number`: User's phone number.
  - `address`: User's address.
  - `type`: User type (Guest, Staff, Admin).

### Hotel

Represents a hotel with basic information.

- **Fields**:
  - `name`: Name of the hotel.
  - `address`: Address of the hotel.
  - `city`: City where the hotel is located.
  - `description`: Description of the hotel.

### Room

Represents a room in a hotel.

- **Fields**:
  - `hotel`: Foreign key to the `Hotel` model.
  - `number`: Room number.
  - `type`: Room type (Single, Double).
  - `price`: Price per night.
  - `available`: Availability status.

### Booking

Represents a booking made by a user for a room.

- **Fields**:
  - `user`: Foreign key to the `User` model.
  - `room`: Foreign key to the `Room` model.
  - `check_in`: Check-in date.
  - `check_out`: Check-out date.
  - `status`: Booking status (Pending, Confirmed, Cancelled).

### Payment

Represents a payment made for a booking.

- **Fields**:
  - `booking`: One-to-one relationship with the `Booking` model.
  - `amount`: Payment amount.
  - `date`: Payment date.
  - `method`: Payment method (Cash, Card, Transfer).

## Views

### HotelViewSet

Provides CRUD operations for `Hotel` model and supports filtering and pagination.

- **Filtering**: Can filter by `name`, `address`, `city`, and availability of rooms.
- **Pagination**: Supports custom pagination.

### RoomViewSet

Provides CRUD operations for `Room` model and supports filtering, sorting, and pagination.

- **Filtering**: Can filter by `type`, `price`, and availability.
- **Sorting**: Can sort by `price` and `type`.
- **Pagination**: Supports custom pagination.

### BookingViewSet

Provides CRUD operations for `Booking` model and supports filtering and pagination. Uses different serializers for list and detail views.

- **Filtering**: Can filter by `status`.
- **Pagination**: Supports custom pagination.

## API Endpoints

### Hotels

- `GET /api/hotels/`: List all hotels (supports filtering and pagination).
- `POST /api/hotels/`: Create a new hotel.
- `GET /api/hotels/{id}/`: Retrieve a hotel by ID.
- `PUT /api/hotels/{id}/`: Update a hotel by ID.
- `DELETE /api/hotels/{id}/`: Delete a hotel by ID.

### Rooms

- `GET /api/rooms/`: List all rooms (supports filtering, sorting, and pagination).
- `POST /api/rooms/`: Create a new room.
- `GET /api/rooms/{id}/`: Retrieve a room by ID.
- `PUT /api/rooms/{id}/`: Update a room by ID.
- `DELETE /api/rooms/{id}/`: Delete a room by ID.

### Bookings

- `GET /api/bookings/`: List all bookings (supports filtering and pagination).
- `POST /api/bookings/`: Create a new booking.
- `GET /api/bookings/{id}/`: Retrieve a booking by ID.
- `PUT /api/bookings/{id}/`: Update a booking by ID.
- `DELETE /api/bookings/{id}/`: Delete a booking by ID.

## Settings

The project settings are configured in `settings.py`:

- **Database**: Uses SQLite by default. Can be changed to other databases.
- **Installed Apps**: Includes `rest_framework`, `hotels`, `bookings`, and `users`.
- **Middleware**: Default middleware provided by Django.
- **Templates**: Configured to use Django templates.
- **Static Files**: Default settings for static files.

## Additional Notes

- Ensure that the `users` app is properly configured and the `UserProfile` model is set up to create and delete profiles as users are created and deleted.
- The project uses Django REST framework for API development and provides a pagination system to manage large datasets.
- To add more functionality or customize existing features, refer to the Django and Django REST framework documentation.
- Contribution guidelines and common troubleshooting steps can be added for better collaboration.

## Running Tests

To run tests, use the following command:
```sh
python manage.py test
