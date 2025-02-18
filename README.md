Here is a responsive `README.md` template for your Django API Implementation Test:

```markdown
# Django API Implementation Test

![Django Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png)

## Objective:
The goal of this task is to evaluate the candidate’s ability to implement authentication, API documentation, and security measures using Django, Django REST Framework (DRF), and Swagger.

## Project Requirements:
Develop a Django-based authentication system with cookie-based authentication. The system should include user registration, login, and a protected endpoint to retrieve the logged-in user’s details.

---

## Task Breakdown

### 1. Project Setup & Configuration
- Create a new Django project and an app named `authentication`.
- Install and configure:
  - Django REST Framework (DRF) for API development.
  - Install the Swagger package.
- Ensure that Swagger (`/swagger/`) automatically generates a CSRF token when accessed.

---

### 2. User Registration API (POST `/api/register/`)
- Accepts `email`, `password`.
- Sends a one-time password to the email for verification.
- Returns a success response upon successful registration.

---

### 3. User Registration API (POST `/api/register/verify`)
- Verifies the registration using the API.

---

### 4. User Login API (POST `/api/login/`)
- Accepts `email` and `password`.
- Validates credentials and authenticates the user.
- On successful authentication:
  - Sets an authentication token (`auth_token`) in an HTTP-only cookie.
  - API access should only work after login.

---

### 5. User Details API (GET `/api/me/`)
- Returns details of the logged-in user.
- Should only be accessible if the user is authenticated using the `auth_token` from cookies.

---

### 6. Logout API (POST `/api/logout/`)
- Clears the `auth_token` cookie from the client.
- Prevents further API access until the user logs in again.

---

### 7. Security Considerations
- **CSRF Protection**:
  - The `csrftoken` should be automatically generated when Swagger is opened.
  - All requests should require a CSRF token for validation.
- **Cookie-based Authentication** only (No token headers).
- **Secure Cookies**:
  - Use `HttpOnly` and `Secure` flags to prevent client-side access.

---

## Bonus (Optional but Preferred)
- Implement a simple frontend (HTML + JavaScript) to test authentication flow. If not, Swagger docs will be used to test the authentication flow.

---

## Installation and Setup

### Clone the repository:
```bash
git clone https://github.com/vishalraj9102/aie.git
cd aie
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Run Migrations:
```bash
python manage.py migrate
```

### Run the Development Server:
```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/` and the Swagger documentation at `http://127.0.0.1:8000/swagger/`.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to check out the project on GitHub: [Django API Implementation Test](https://github.com/vishalraj9102/aie.git)
```

