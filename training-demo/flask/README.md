
## Project Name: Flask Demo App


***

### **Objective**

Build and demo a simple Flask API to illustrate core server/app workflow.

***

### **1. Solution/Architecture**

**Workflow Diagram:**

```
Client POST (browser/Postman)
      ↓
Flask server (Python, localhost)
      ↓
API endpoint processes request
      ↓
Returns JSON response
```

- Minimal Python Flask server with a test/demo endpoint.

***

### **2. Prerequisites**

- **Python 3.x** installed
- `pip` package manager
- Internet connection (for installing Flask)

***

### **3. Installation \& Setup**

Install Flask:

```bash
pip install flask
```


***

### **4. Running the App**

1. Save this code as `flask_demo.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask demo!"})

if __name__ == '__main__':
    app.run(debug=True)
```

2. In terminal, navigate to the project folder.
3. Start your server:

```bash
python flask_demo.py
```


***

### **5. How to Use**

- Open your browser or Postman.
- Enter URL: `http://127.0.0.1:5000/hello`
- Method: **GET**
- Response:

```
{
  "message": "Hello from Flask demo!"
}
```


***

### **6. Sample Input/Output**

**Example using browser or Postman:**

- **Request**: GET to `http://127.0.0.1:5000/hello`
- **Response**:

```
{
  "message": "Hello from Flask demo!"
}
```


***

### **7. Troubleshooting**

- **ModuleNotFoundError: flask**
Run: `pip install flask`
- **Server not starting**
Ensure you’re running Python 3+ and in the right directory.
- **Port already in use**
Change `app.run(debug=True)` to `app.run(debug=True, port=5050)` or similar.

***

### **8. requirements.txt**

```
flask
```


***

### **9. Deliverables**

- `flask_demo.py` (Python app)
- `README.md` (this file)
- `requirements.txt`
- Demo video (showing setup and results in browser/Postman)
