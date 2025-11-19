
### **1. Solution/Architecture**

**Workflow Diagram:**

```
User input (name)
    ↓
Format Question: "Who is {name}?"
    ↓
OpenAI LLM via LangChain
    ↓
Display Answer
```

- Python script using LangChain + OpenAI API to chain prompt creation and answer generation.

***

### **2. Prerequisites**

- **Python 3.x** installed
- **OpenAI API key** (get from https://platform.openai.com/account/api-keys)
- Internet connection

***

### **3. Installation \& Setup**

Install required packages:

```bash
pip install langchain langchain-openai openai
```

Set your API key (PowerShell):

```powershell
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

*(Replace with your real API key)*

For Windows CMD:

```cmd
set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

For macOS/Linux:

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```


***

### **4. Running the App**

1. Save app source as `langgraph_demo.py`.
2. In your terminal, navigate to your project folder.
3. Set your API key as above.
4. Run the script:

```bash
python langgraph_demo.py
```


***

### **5. How to Use**

- When prompted, enter any name (e.g., `Ada Lovelace`, `Alan Turing`).
- The app will format “Who is {name}?” and send to the LLM.
- View the AI-generated answer.
- Type `exit` to quit.

***

### **6. Sample Input/Output**

```
Enter a name (or type 'exit'): Ada Lovelace

Question: Who is Ada Lovelace?
Answer: Ada Lovelace was a pioneering mathematician...

Enter a name (or type 'exit'): exit
```


***

### **7. Troubleshooting**

- **Missing modules error:**
Run: `pip install langchain langchain-openai openai`
- **API error / quota exceeded (`RateLimitError: 429`):**
Check your OpenAI usage/quota at https://platform.openai.com/account/usage
Upgrade account or use a key with available quota.
- **Authentication error:**
Confirm you’ve set the `OPENAI_API_KEY` environment variable.

***

### **8. requirements.txt**

Include this file for reproducible installation:

```
langchain
langchain-openai
openai
```


***

### **9. Deliverables**

- `langgraph_demo.py` (Python app)
- `README.md` (this file)
- `requirements.txt`
- Demo video (showing setup and running the app)

***

**Note:**
If you face an "insufficient_quota" error, code and workflow are correct—requires an OpenAI key with active quota to see live results.
