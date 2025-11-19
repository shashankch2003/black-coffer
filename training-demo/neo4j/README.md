
## Task 2: Neo4j Graph Demo – Step-by-Step Guide


***

### **Prerequisites**

- Docker installed
- Python 3.x installed
- Python Neo4j driver installed:

```
pip install neo4j
```


***

### **Folder Structure**

Your directory should have:

```
neo4j/
|-- connect.py
|-- README.md
```


***

### **Step-by-Step Instructions**

#### 1. **(Optional) Remove Old Neo4j Container**

Open PowerShell or terminal and run:

```bash
docker rm -f neo4j
```


***

#### 2. **Start Neo4j Docker Container**

Choose a password of at least 8 characters (example: `myneo4jpass123`).

Run:

```power shell
docker run -d --name neo4j -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/myneo4jpass123 neo4j:5

```


***

#### 3. **Open Neo4j Browser and Log In**

- In your browser, go to:
[http://localhost:7474](http://localhost:7474)
- Username: `neo4j`
- Password: `myneo4jpass123`

***

#### 4. **Edit `connect.py` If Needed for Password**

Make sure your Python file has:

```python
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "myneo4jpass123"))

def create_graph(tx):
    tx.run("""
        MERGE (a:Person {name:'Alice'})
        MERGE (b:Person {name:'Bob'})
        MERGE (c:Person {name:'Eve'})
        MERGE (a)-[:FRIEND]->(b)
        MERGE (a)-[:FRIEND]->(c)
        MERGE (c)-[:ENEMY]->(b)
    """)

def show_friends(tx, name):
    for record in tx.run("MATCH (a:Person {name:$name})-[:FRIEND]->(f) RETURN f.name", name=name):
        print(f"{name} is friends with {record['f.name']}")

with driver.session() as session:
    session.execute_write(create_graph)
    session.execute_read(show_friends, "Alice")

driver.close()
```

- Replace `myneo4jpass123` in both the Docker command and `connect.py` above if using something else!

***

#### 5. **Run Your Python Script**

Navigate to your project directory in PowerShell:

```bash
cd path\to\neo4j\folder
python connect.py
```


***

#### 6. **View the Result in Neo4j Browser**

- In the Neo4j browser, run:

```
MATCH (a:Person)-[r]->(b) RETURN a, r, b
```

- You’ll see the graph visualization for Alice, Bob, and Eve.

***

#### 7. **To Stop \& Remove Neo4j Docker Container**

```bash
docker rm -f neo4j
```
