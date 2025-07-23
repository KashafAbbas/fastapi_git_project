# FastAPI File Upload Project

This is a simple FastAPI project demonstrating file uploads using FastAPI's `UploadFile`.

## 🛠 Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## 📦 Installation

1. Clone this repository or navigate to your project folder.
2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate  # For Windows
```

3. Install the required packages:

```bash
pip install fastapi uvicorn python-multipart
```

## 🚀 Running the App

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

This will start the server at:

```
http://127.0.0.1:8000
```

## 📄 Swagger UI

You can test the API using Swagger UI here:

```
http://127.0.0.1:8000/docs
```

### ➕ Upload File Endpoint

- Endpoint: `POST /upload/`
- Click "Try it out"
- Choose a file (e.g., `test_upload.txt`)
- Click "Execute"
- You’ll see a response with file name and content type

## 📁 .gitignore

Create a `.gitignore` file and add the following:

```
venv/
__pycache__/
*.pyc
.env
*.log
```

This will prevent unnecessary or sensitive files from being committed to Git.

## 🧪 Test File

Create a simple test file called `test_upload.txt`:

```text
This is a sample file used for testing FastAPI file upload.
```

Use this file to test the `/upload/` endpoint via Swagger UI.

## 💻 Git Commands to Initialize and Push

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```

Happy coding! 🚀
