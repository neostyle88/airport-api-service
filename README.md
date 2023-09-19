# SkyTrack

SkyTrack provides endpoints to manage and query data related to
flights, crew members, airplanes, orders, and more. It is built using Django
and Django REST Framework. For creating tasks was used Celery library.

## Endpoints

Below is a list of available endpoints and their functionalities:

### Crews

- `GET /api/crews/`: Retrieve a list of all crew members.
- `POST /api/crews/`: Create a new crew member.
- `GET /api/crews/?first_name=<first_name>&last_name=<last_name>&position=<position>`:
  Filter crew members by first name, last name, and position.

### Countries

- `GET /api/countries/`: Retrieve a list of all countries.
- `POST /api/countries/`: Create a new country.
- `GET /api/countries/?name=<name>`: Filter countries by name.

### Cities

- `GET /api/cities/`: Retrieve a list of all cities.
- `POST /api/cities/`: Create a new city.
- `GET /api/cities/?name=<name>&country=<country_id>`: Filter cities by name
  and country.

### Facilities

- `GET /api/facilities/`: Retrieve a list of all facilities.
- `POST /api/facilities/`: Create a new facility.
- `GET /api/facilities/?name=<name>`: Filter facilities by name.

### Airports

- `GET /api/airports/`: Retrieve a list of all airports.
- `POST /api/airports/`: Create a new airport.
- `GET /api/airports/?name=<name>&facilities=<facility_ids>&closest_big_city=<city_name>`:
  Filter airports by name, facilities, and closest big city.
- `GET /api/airports/<airport_id>/`: Retrieve details of a specific airport.
- `POST /api/airports/<airport_id>/upload-image/`: Upload an image for a
  specific airport (Admins only).

### Routes

- `GET /api/routes/`: Retrieve a list of all flight routes.
- `POST /api/routes/`: Create a new flight route.
- `GET /api/routes/?source=<source_city>&destination=<destination_city>`:
  Filter routes by source and destination cities.

### Airplane Types

- `GET /api/airplane-types/`: Retrieve a list of all airplane types.
- `POST /api/airplane-types/`: Create a new airplane type.
- `GET /api/airplane-types/?name=<name>`: Filter airplane types by name.

### Airplanes

- `GET /api/airplanes/`: Retrieve a list of all airplanes.
- `POST /api/airplanes/`: Create a new airplane.
- `GET /api/airplanes/?name=<name>&facilities=<facility_ids>&airplane_type=<airplane_type>`:
  Filter airplanes by name, facilities, and airplane type.
- `GET /api/airplanes/<airplane_id>/`: Retrieve details of a specific airplane.
- `POST /api/airplanes/<airplane_id>/upload-image/`: Upload an image for a
  specific airplane (Admins only).

### Flights

- `GET /api/flights/`: Retrieve a list of all flights.
- `POST /api/flights/`: Create a new flight.
- `GET /api/flights/?departure_time=<departure_date>&arrival_time=<arrival_date>`:
  Filter flights by departure and arrival times.
- `GET /api/flights/<flight_id>/`: Retrieve details of a specific flight.

### Orders

- `GET /api/orders/`: Retrieve a list of all orders (authenticated users only).
- `POST /api/orders/`: Create a new order (authenticated users only).
- `GET /api/orders/?date=<date>`: Filter orders by creation date (authenticated
  users only).
- `GET /api/orders/<order_id>/`: Retrieve details of a specific order (
  authenticated users only).

## Local deployment instruction

To deploy the Airport API Service locally, please follow the steps below:

1. Clone the repository to your local machine:
   ```git clone https://github.com/neostyle88/airport-api-service.git```

2. Navigate to the project directory:
   ```cd airport_api_service```

3. Start docker container using the following command:
   `docker-compose up --build`

4. Open your web browser and access the Airport API Service application
   at http://localhost:8000/.

5. Create schedule if you want to get email when flight departs tomorrow

You can use test admin user made during migration:

- Email ```test@admin.com```
- Password ```testpass123```

---

## Environment Variables

> The following environment variables should be set in the `.env` file:

- `DJANGO_SECRET_KEY`: DJANGO_SECRET_KEY
- `POSTGRES_DB`: POSTGRES_DB
- `POSTGRES_USER`: POSTGRES_USER
- `POSTGRES_PASSWORD`: POSTGRES_PASSWORD
- `POSTGRES_HOST`: POSTGRES_HOST
- `POSTGRES_PORT`: POSTGRES_PORT
- `CELERY_BROKER_URL`: CELERY_BROKER_URL
- `CELERY_RESULT_BACKEND`: CELERY_RESULT_BACKEND
- `EMAIL_HOST`: EMAIL_HOST
- `EMAIL_PORT`: EMAIL_PORT
- `EMAIL_HOST_USER`: EMAIL_HOST_USER
- `EMAIL_HOST_PASSWORD`: EMAIL_HOST_PASSWORD
- `DEFAULT_FROM_EMAIL`: DEFAULT_FROM_EMAIL

**Note:** Before starting the project, make a copy of the `.env_sample` file
and rename it to `.env`. Replace the sample values with your actual environment
variable values.
