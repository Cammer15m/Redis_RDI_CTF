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

# Generate continuous track data
cd from-repo/scripts
python3 generate_load.py
```
*This continuously generates realistic track data using 3,495 real track names and composers.*

### **3. Access Tools**
- **Redis Insight**: http://localhost:5540 - *Connect to your Redis database*
- **Database Browser**: http://localhost:3001 - *View PostgreSQL data (SQLPad)*
- **Monitoring**: http://localhost:3000 - *Grafana dashboards*
- **PostgreSQL**: localhost:5432 - *Direct database access (postgres/postgres)*

## 🔄 Data Loading Details

The data generator uses a CSV file with **3,495 real track records** including:
- **Real track names**: "Stairway to Heaven", "Bohemian Rhapsody", "Hotel California", etc.
- **Real composers**: "Angus Young, Malcolm Young, Brian Johnson", "Steven Tyler, Joe Perry", etc.
- **Automatic TrackId management**: Finds the highest existing ID and increments from there
- **Random realistic data**: Milliseconds (100-300k), Bytes (100-500k), Genres (1-5)
- **Continuous generation**: Adds tracks every 100-500ms for realistic CDC testing

## 🔧 Basic RDI Setup

### **Connect to Your Redis Database**
1. Open **Redis Insight**: http://localhost:5540
2. Add your Redis database connection
3. Configure RDI pipeline using the web interface

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
