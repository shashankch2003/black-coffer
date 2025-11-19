
## Task 1: ELK Stack Demo — Step-by-Step Execution Guide


***

### **Prerequisites**

- Docker and Docker Compose installed
- Files in your project folder:
    - `docker-compose.yml`
    - `logstash.conf`
    - `ecommerce_data.csv` (your sample data)

***

### **Folder Structure**

```
elk/
|-- docker-compose.yml
|-- logstash.conf
|-- ecommerce_data.csv
|-- README.md
```


***

### **Instructions to Execute the Demo**

#### 1. **Check and Edit Config Files**

- **docker-compose.yml**

```yaml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.2
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    networks:
      - elk
  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.2
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
    networks:
      - elk
  logstash:
    image: docker.elastic.co/logstash/logstash:8.11.2
    ports:
      - "5044:5044"
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
      - ./ecommerce_data.csv:/usr/share/logstash/pipeline/ecommerce_data.csv
    depends_on:
      - elasticsearch
    networks:
      - elk
networks:
  elk:
    driver: bridge
```

- **logstash.conf**

```conf
input {
  file {
    path => "/usr/share/logstash/pipeline/ecommerce_data.csv"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}
filter {
  csv {
    separator => ","
    columns => ["order_date","category","currency","customer_first_name",
                "customer_last_name","customer_gender","customer_phone",
                "manufacturer","price","product_name","total_quantity"]
  }
  mutate {
    convert => { "price" => "float" "total_quantity" => "integer" }
  }
}
output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    index => "ecommerce_orders"
  }
  stdout { codec => rubydebug }
}
```

    - **Change the column headers** if your CSV is different!

***

#### 2. **Start the ELK Stack**

- Open PowerShell or terminal in the `elk` folder.
- Run:

```bash
docker-compose down -v
docker-compose up
```

- Wait for all services to finish starting.

***

#### 3. **Access Kibana**

- Open your browser and go to:
[http://localhost:5601](http://localhost:5601)

***

#### 4. **Configure Index Pattern in Kibana**

- Go to **Stack Management → Data Views**.
- Click **Create data view**.
- Index pattern:

```
ecommerce_orders
```

- Choose the timestamp field (`order_date`) if available.
- Click **Create data view**.

***

#### 5. **View and Explore Imported Data**

- In Kibana, select **Discover** from the left menu.
- Pick your new data view (`ecommerce_orders`).
- Browse, search, and analyze the data you ingested from CSV.

***

#### 6. **Shutdown**

- To stop and remove all services and data:

```bash
docker-compose down -v
```

