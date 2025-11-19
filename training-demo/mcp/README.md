
## MCP Flask Demo — Step-by-Step Guide


***

### **Prerequisites**

- Python 3.x installed
- `pip` package manager installed (comes with recent Python)

***

### **Folder Structure**

```
mcp_demo/
|-- app.py            # <-- your MCP Flask code
|-- README.md         # <-- this file
```


***

### **Step 1: Install Requirements**

In your command prompt or terminal:

```bash
pip install flask
```


***

### **Step 2: Code for MCP Demo (`mcp_demo.py`)**

Paste this code in `mcp_demo.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/model-context', methods=['POST'])
def context():
    content = request.json
    # Dummy response for demo
    response = {
        "received_context": content,
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```


***

### **Step 3: Run the Flask App**

Navigate (in terminal) to your project folder and run:

```bash
python mcp_demo.py
```

This starts the server on `http://127.0.0.1:5000`.

***

### **Step 4: Test the API with Postman**

- **Method:** POST
- **URL:** `http://127.0.0.1:5000/model-context`
- **Headers:**
    - `Content-Type`: `application/json`
- **Body:** raw, JSON:

```json
{
  "model": "GPT",
  "input": "Hello from MCP"
}
```

- **Click Send**

**Expected Response:**

```json
{
  "received_context": {
    "model": "GPT",
    "input": "Hello from MCP"
  },
  "status": "success"
}
```


***

### **Troubleshooting**

- **404 Not Found:**
    - Double-check the route: `/model-context`
    - Make sure Flask server is running
    - Method should be POST
    - Server port should be `5000`
- **ModuleNotFoundError:**
    - Run `pip install flask`
- **Invalid JSON format:**
    - Check that request body is proper JSON and set header to application/json
- **Cannot connect:**
    - Make sure server is running and port matches your request URL

***

### **To Stop the Server**

Press `Ctrl + C` in the terminal.

