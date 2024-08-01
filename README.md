# Chatbot API
================
## Features

- **User Registration and Authentication**: Register new users and authenticate existing users.
- **Token-Based Authentication**: Secure API access using JWT tokens.
- **Chat Functionality**: Send messages to the chatbot and receive responses.
- **Token Management**: Check and manage user tokens.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Pip package manager

### Clone the Repository

```bash
git clone https://github.com/Damithedev/AIchatbot.git
cd AIchatbot
```
### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate

```

### Run the Server

```bash
python manage.py runserver
```

#### The server will start on `http://localhost:8000



## Endpoints
### 1. Register User
#### URL: `/users/register/`
#### Method: `POST`
#### Description: Creates a new user account.
#### Request Body:
```json
{
  "username": "string",
  "password": "string"
}
```

### 2. List Users
#### URL: `/users/`
#### Method: `GET`
#### Description: Retrieves a list of all registered users.



### 3. Login User
#### URL: `/users/login/`
#### Method: `POST`
#### Description: Authenticates a user and returns a JSON Web Token (JWT).
#### Request Body:
```json
{
  "username": "string",
  "password": "string"
}
```
#### Response
```
{
  "token": "string"
}
```

### 4. Send Message
#### URL: `/send/`
#### Method: `POST`
#### Description: Sends a message to the chatbot and returns a response.
#### Request Body:
```json
{
  "message": "string"
}
```
#### Response
```
{
  "response": "string"
}
```

### 5. Check Token
#### URL: `/token/`
#### Method: `GET`
#### Description: Checks the authenticated user's token and returns the remaining tokens.
#### Response:
```json
{
  "tokens": "integer"
}
```

## Models
### User
Represents a user account with a username and password.
### Chat
Represents a chat message with a message, user, and response.

## Serializers
### UserSerializer
Serializes and deserializes user data.
### ChatSerializer
Serializes and deserializes chat message data.

## Authentication
### JSON Web Token (JWT) Authentication
* JSON Web Token (JWT) authentication is used to authenticate users.
* Tokens are valid for 60 minutes.

## Chatbot Response
* The chatbot response is handled asynchronously using the `dummy_chatbot_response` function.
