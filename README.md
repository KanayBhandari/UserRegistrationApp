# UserRegistrationApp
A simple FastAPI user registration application.

**Steps to setup Development Environment:**

1. Clone the project and cd into the clone project dir
```
git clone git@github.com:KanayBhandari/UserRegistrationApp.git
```
```
cd UserRegistrationApp
```
2. Create virtual environment
```
python -m venv venv (For Windows)
```
```
python3 -m venv venv (For Linux)
```
3. Activate virtual environment(Windows)
```
source venv/Scripts/activate
```
Activate virtual environment(Linux)
```
source venv/bin/activate
```
4. Install the requirements in the virtual environment
```
pip install -r requirements.txt
```
5. Create a `.env` file and store the creds for postgres DB with below fields.

```
DB_USER
DB_PASSWORD
DB_NAME
DB_HOST
DB_PORT
SCHEMA_NAME
```
6. Create a Postges DB and update the creds in `.env` file

7. Run the application in development server
```
uvicorn app.main:app --reload
```
