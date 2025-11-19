from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "myneo4jpass123"))

def create_graph(tx):
    # Creates nodes and relationships
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
