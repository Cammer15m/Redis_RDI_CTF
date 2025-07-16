# Redis RDI Training Environment 🚀

Professional Redis Data Integration (RDI) training environment with PostgreSQL, Redis, and monitoring tools.

## 🚀 Quick Start

### **1. Clone and Start Services**
```bash
git clone https://github.com/Cammer15m/Redis_RDI_CTF
cd Redis_RDI_CTF
./start.sh
```

### **2. Load Sample Data**
```bash
# Install dependencies
pip3 install pandas psycopg2-binary SQLAlchemy==1.4.46

# Generate continuous track data (runs forever - press Ctrl+C to stop)
cd from-repo/scripts
python3 generate_load.py
```
*This continuously generates realistic track data using 3,495 real track names and composers. Perfect for testing RDI in real-time!*

### **3. Access Tools**
- **Redis Insight**: http://localhost:5540 - *Connect to your Redis database*
- **Database Browser**: http://localhost:3001 - *View PostgreSQL data (SQLPad)*
- **Monitoring**: http://localhost:3000 - *Grafana dashboards*
- **PostgreSQL**: localhost:5432 - *Direct database access (postgres/postgres)*

## 🎵 Data Generator Features

The `generate_load.py` script provides realistic continuous data for RDI testing:

### **Real Music Data**
- **3,495 authentic track records** from the Chinook database
- **Real track names**: "Stairway to Heaven", "Bohemian Rhapsody", "Hotel California", etc.
- **Real composers**: "Angus Young, Malcolm Young, Brian Johnson", "Steven Tyler, Joe Perry", etc.
- **Proper data types**: Realistic milliseconds, bytes, genres, and pricing

### **Smart Data Management**
- **Automatic TrackId handling**: Finds MAX(TrackId) and increments safely
- **No primary key conflicts**: Solves the duplicate key constraint issue
- **Continuous generation**: Adds tracks every 100-500ms for realistic CDC testing
- **Random selection**: Picks different tracks each time for variety

### **Perfect for RDI Testing**
- **Change Data Capture (CDC)**: Watch real-time sync to Redis
- **Performance testing**: Sustained data flow for load testing
- **Demo scenarios**: Realistic data for presentations

## 🔧 Complete RDI Setup

### **Step 1: Create RDI Configuration**
Create the main RDI config file:
```bash
# Create config directory
mkdir -p rdi_config

# Create config.yaml
cat > rdi_config/config.yaml << 'EOF'
connections:
  # Redis target DB connection details
  target:
    type: redis
    host: your-redis-host.redns.redis-cloud.com  # Replace with your Redis Cloud host
    port: 12345                                   # Replace with your Redis Cloud port
    password: your-redis-password                 # Replace with your Redis Cloud password
    # For Redis Cloud, uncomment these if using TLS:
    # tls: true
    # tls_skip_verify: false
EOF
```

### **Step 2: Create Ingest Configuration**
```bash
# Create ingest-config.yaml
cat > rdi_config/ingest-config.yaml << 'EOF'
connections:
  # Redis target DB connection details
  target:
    host: your-redis-host.redns.redis-cloud.com  # Replace with your Redis Cloud host
    port: 12345                                   # Replace with your Redis Cloud port
    password: your-redis-password                 # Replace with your Redis Cloud password
    # For Redis Cloud with TLS:
    # tls: true
    # tls_skip_verify: false

applier:
  # Error handling strategy: ignore - skip, dlq - store rejected messages in a dead letter queue
  error_handling: dlq
  # Dead letter queue max messages per stream
  dlq_max_messages: 100
  # Target data type: hash/json - RedisJSON module must be in use in the target DB
  target_data_type: hash
EOF
```

### **Step 3: Create Job Configuration**
```bash
# Create jobs directory and track job
mkdir -p rdi_config/jobs

# Create track.yaml job
cat > rdi_config/jobs/track.yaml << 'EOF'
source:
    table: Track
transform:
  - uses: add_field
    with:
      field: NameUpper
      expression: upper("Name")
      language: sql
  - uses: filter
    with:
      expression: GenreId=2  # Only sync Metal tracks (GenreId=2)
      language: sql
EOF
```

### **Step 4: Deploy and Start RDI**
```bash
# Access RDI container
docker exec -it rdi bash

# Deploy configuration
redis-di deploy --config /path/to/rdi_config

# Start the pipeline
redis-di start

# Check status
redis-di status
```

### **Monitor Data Sync**
- **PostgreSQL data**: http://localhost:3001 (SQLPad)
- **Redis data**: http://localhost:5540 (Redis Insight)
- **System metrics**: http://localhost:3000 (Grafana)

## 🛑 Stop Environment

```bash
# Stop all services
./stop.sh

# Or manually
docker-compose down
```

## 🏗️ What's Included

### **Services**
- **PostgreSQL** - Source database with music data
- **Redis Insight** - Redis database management interface
- **Grafana** - Monitoring dashboards
- **SQLPad** - PostgreSQL query interface
- **Prometheus** - Metrics collection

### **Sample Data**
- **12 Artists** - The Beatles, Led Zeppelin, Pink Floyd, etc.
- **12 Albums** - Abbey Road, Dark Side of the Moon, etc.
- **28+ Tracks** - Come Together, Stairway to Heaven, etc.

### **What You Need**
- **Docker** - Will be installed automatically if missing
- **Redis Database** - Use Redis Cloud (free) or your own Redis instance

## 🔧 Troubleshooting

### **Services Won't Start**
```bash
# Check if Docker is running
docker ps

# Restart services
./stop.sh
./start.sh

# Check logs
docker-compose logs
```

### **Can't Load Data**
```bash
# Make sure PostgreSQL is running
docker ps | grep postgres

# Try loading data again
cd scripts
./load_data.sh
```

### **Port Conflicts**
If you get port errors, check what's using the ports:
```bash
# Check ports 5432, 5540, 3000, 3001
lsof -i :5432
lsof -i :5540
```

## 📚 Learning Resources

- [Redis Data Integration Documentation](https://redis.io/docs/data-integration/)
- [Redis Cloud Free Account](https://redis.com/try-free/)
- [Redis Insight Download](https://redis.io/downloads/#redis-insight)

## 🤝 Contributing

Found an issue? Contributions welcome!
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Ready to learn Redis Data Integration? Start with the Quick Start above! 🚀**
