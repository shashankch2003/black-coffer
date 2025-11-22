from neo4j import GraphDatabase
import random

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "myneo4jpass123"))

def create_large_graph(tx, node_count):
    # Create 50 Person nodes
    for i in range(node_count):
        tx.run("MERGE (:Person {name:$name})", name=f"Person_{i}")

    # Create random "FRIENDS" and "ENEMY" relationships
    relations = ["FRIEND", "ENEMY"]
    for _ in range(node_count * 3):  # 150 relationships, approx 3 per node
        a = random.randint(0, node_count-1)
        b = random.randint(0, node_count-1)
        if a != b:
            rel = random.choice(relations)
            tx.run(
                f"MATCH (a:Person {{name:$nameA}}), (b:Person {{name:$nameB}}) "
                f"MERGE (a)-[:{rel}]->(b)",
                nameA=f"Person_{a}", nameB=f"Person_{b}"
            ) 

with driver.session() as session:
    session.execute_write(create_large_graph, 50)

driver.close()
