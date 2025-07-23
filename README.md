# FastAPI File Upload Project

This is a simple FastAPI project that demonstrates how to upload files using FastAPI's `UploadFile`.

## 🛠 Requirements

- Python 3.8 or higher  
- FastAPI  
- Uvicorn  

## 📦 Installation

1. Clone this repo or open your project folder.  
2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the dependencies:

    ```bash
    pip install fastapi uvicorn python-multipart
    ```

## 🚀 Running the App

Start the server with:

```bash
uvicorn main:app --reload
```

It will be available at:

```
http://127.0.0.1:8000
```

## 📄 Swagger UI

You can test the API through the interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

### ➕ Upload File Endpoint

- **Method:** `POST`  
- **Endpoint:** `/upload/`  
- Click **Try it out**  
- Choose a file (e.g., `test_upload.txt`)  
- Click **Execute**  
- You’ll receive a response showing the file name and content type  

## 📁 .gitignore Setup

Create a `.gitignore` file and add:

```
venv/
__pycache__/
*.pyc
.env
*.log
```

This helps keep your repo clean by ignoring unnecessary or sensitive files.

## 🧪 Test File

Make a simple test file named `test_upload.txt`:

```
This is a sample file used for testing FastAPI file upload.
```

Use this when testing the `/upload/` endpoint.

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
