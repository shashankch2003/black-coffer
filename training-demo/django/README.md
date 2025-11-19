
### **1. Solution/Architecture**

**Workflow Diagram:**

```
Client request (browser/Postman)
      ↓
Django server (Python, localhost)
      ↓
URL route matches endpoint
      ↓
View returns response
```

- Django project and app with one URL endpoint returning a message.

***

### **2. Prerequisites**

- **Python 3.x** installed
- `pip` package manager
- Internet connection (for installing Django)

***

### **3. Installation \& Setup**

Install Django:

```bash
pip install django
```


***

### **4. Running the App**

1. Create a new Django project:

```bash
django-admin startproject demo_project
cd demo_project
```

2. (Optional) Create a Django app:

```bash
python manage.py startapp demo_app
```

3. Edit `demo_project/urls.py` and add:

```python
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello from Django demo!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
]
```

4. Run the development server:

```bash
python manage.py runserver
```


***

### **5. How to Use**

- Open your browser or Postman.
- URL: `http://127.0.0.1:8000/hello/`
- Method: **GET**
- Response:

```
{
  "message": "Hello from Django demo!"
}
```


***

### **6. Sample Input/Output**

**Request:** GET to `http://127.0.0.1:8000/hello/`
**Response:**

```
{
  "message": "Hello from Django demo!"
}
```


***

### **7. Troubleshooting**

- **ModuleNotFoundError: django**
Run: `pip install django`
- **Server error or port in use:**
Try `python manage.py runserver 8080`
- **App not created or not added to INSTALLED_APPS (for extended demo):**
Check `settings.py` and add your app if needed.

***

### **8. requirements.txt**

```
django
```


***

### **9. Deliverables**

- `demo_project/` (Django project folder)
- `README.md` (this file)
- `requirements.txt`
- Demo video (setup, running, endpoint demo in browser/Postman)

