command required to run thi project
Here are all the commands needed to run your AI Chatbot project:

1. Backend Setup Commands
Clone the repository (if not already done)
bash
git clone https://github.com/saurav9746/chatbot2.0.git
cd chatbot2.0/backend
Create and activate virtual environment
bash
# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies
bash
pip install -r requirements.txt
If requirements.txt doesn't exist, install manually:
bash
pip install django==4.2.7
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install groq==0.4.2
pip install python-dotenv==1.0.0
pip install pillow==10.1.0
Create .env file with your API keys
bash
# Create .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
echo "DEBUG=True" >> .env
echo "SECRET_KEY=your-secret-key-here" >> .env
Run migrations
bash
python manage.py makemigrations bot
python manage.py migrate
Create superuser (optional - for admin access)
bash
python manage.py createsuperuser
# Follow prompts to create admin user
Start backend server
bash
python manage.py runserver
Backend will run at: http://localhost:8000

2. Frontend Setup Commands
Open new terminal and navigate to frontend
bash
cd ../frontend
# Or if you're in backend folder: cd frontend
Install dependencies
bash
npm install
If you don't have package.json, create one:
bash
npm init -y
npm install react react-dom react-markdown
npm install -D vite @vitejs/plugin-react
Start frontend development server
bash
npm run dev
Frontend will run at: http://localhost:5173

3. Quick Start Script (One Command)
Create a file start.bat in your project root:

batch
@echo off
echo Starting AI Chatbot...
echo.

echo Starting Backend Server...
start cmd /k "cd backend && venv\Scripts\activate && python manage.py runserver"

timeout /t 3

echo Starting Frontend Server...
start cmd /k "cd frontend && npm run dev"

echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
pause
Run it:

bash
start.bat
4. For Mac/Linux - Create start.sh
bash
#!/bin/bash
echo "Starting AI Chatbot..."

# Start backend
cd backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!

cd ..

# Start frontend
cd frontend
npm run dev &
FRONTEND_PID=$!

echo "Backend running on http://localhost:8000"
echo "Frontend running on http://localhost:5173"
echo "Press Ctrl+C to stop"

wait $BACKEND_PID $FRONTEND_PID
Make it executable:

bash
chmod +x start.sh
./start.sh
5. Environment Setup Commands
Check Python version
bash
python --version
# Should be Python 3.8 or higher
Check Node version
bash
node --version
# Should be Node 16 or higher
Check npm version
bash
npm --version
Install pip if not available
bash
python -m ensurepip --upgrade
6. Troubleshooting Commands
If migrations fail:
bash
# Reset migrations
python manage.py migrate bot zero
python manage.py makemigrations bot
python manage.py migrate bot
If database issues:
bash
# Delete database and recreate
rm db.sqlite3
python manage.py migrate
If port already in use:
bash
# Use different port for backend
python manage.py runserver 8001

# Use different port for frontend
npm run dev -- --port 5174
If dependencies conflict:
bash
# Create fresh virtual environment
rm -rf venv
python -m venv venv
source venv/Scripts/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
7. Complete Setup Script
Create setup.bat for Windows:

batch
@echo off
echo ========================================
echo AI Chatbot Setup Script
echo ========================================
echo.

echo 1. Creating virtual environment...
cd backend
python -m venv venv

echo 2. Activating virtual environment...
call venv\Scripts\activate

echo 3. Installing dependencies...
pip install -r requirements.txt

echo 4. Creating .env file...
if not exist .env (
    echo GROQ_API_KEY=your_groq_api_key_here > .env
    echo DEBUG=True >> .env
    echo SECRET_KEY=your-secret-key-here >> .env
)

echo 5. Running migrations...
python manage.py makemigrations bot
python manage.py migrate

echo 6. Creating superuser (optional)...
python manage.py createsuperuser

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the servers:
echo 1. Backend: cd backend && python manage.py runserver
echo 2. Frontend: cd frontend && npm run dev
echo.
pause
Run it:

bash
setup.bat
8. Docker Setup (Optional)
Create Dockerfile:

dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
Build and run:

bash
docker build -t ai-chatbot .
docker run -p 8000:8000 ai-chatbot
9. Testing Commands
Test backend API:
bash
# Test hello endpoint
curl http://localhost:8000/api/hello/

# Test create session
curl -X POST http://localhost:8000/api/sessions/ \
  -H "Content-Type: application/json" \
  -d '{}'
Test frontend is working:
bash
# In browser, open:
http://localhost:5173
10. Complete Production Build
Build frontend for production:
bash
cd frontend
npm run build
Collect static files:
bash
cd ../backend
python manage.py collectstatic
Run with production server (gunicorn):
bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
Quick Reference Card:
bash
# Start everything from scratch
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# In new terminal
cd frontend
npm install
npm run dev

# Open browser
http://localhost:5173
That's it! Your AI Chatbot should now be running locally. 🚀

