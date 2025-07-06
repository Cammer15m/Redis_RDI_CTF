# Redis RDI CTF 🚀

Welcome to the **Redis Data Integration (RDI) Capture The Flag** challenge! This hands-on learning environment teaches real-time data integration patterns using Redis and PostgreSQL.

## 🎯 What You'll Learn

- **Data Integration Patterns**: Snapshot vs Change Data Capture (CDC)
- **Real-time Data Replication**: PostgreSQL → Redis synchronization
- **Redis Data Structures**: Hashes, Streams, and JSON
- **Advanced RDI Features**: Transformations and multi-table replication

## 📋 Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows with WSL2
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Disk Space**: ~3GB free space
- **Docker**: Will be installed automatically if not present
- **Python 3.7+**: With pip package manager
- **Internet Connection**: For downloading packages and Docker images

### Software Dependencies (Auto-installed)
**Python Packages:**
- `redis>=4.0.0` - Redis client library
- `psycopg2-binary>=2.9.0` - PostgreSQL adapter
- `flask>=2.0.0` - Web framework for monitoring UI
- `pandas>=1.3.0` - Data manipulation library
- `sqlalchemy>=1.4.0` - Database toolkit
- `python-dotenv>=0.19.0` - Environment variable management
- `requests>=2.28.0` - HTTP library

**Docker Images (~2.5GB total):**
- `postgres:15` (~350MB) - PostgreSQL database
- `redis:7-alpine` (~30MB) - Redis server
- `redis/redisinsight:latest` (~200MB) - Redis management UI
- `sqlpad/sqlpad:6` (~150MB) - PostgreSQL query interface
- `redis/rdi:latest` (~800MB) - Redis Data Integration platform

### Knowledge Prerequisites
- **Basic knowledge** of databases and data integration
- **Terminal/Command line** familiarity
- **Redis Cloud** account (free tier available) - Optional for advanced features

## 🚀 Quick Start

### 1. Complete Local Setup
### **🚀 Automated Setup (Recommended)**
```bash
# Clone the repository
git clone https://github.com/Cammer15m/Redis_RDI_CTF
cd Redis_RDI_CTF

# One-command setup (installs everything automatically)
./scripts/install_all.sh
```

**This automatically installs:**
- ✅ PostgreSQL with music database (15 tracks, 8 albums)
- ✅ Redis RDI via Docker (http://localhost:8080)
- ✅ Python dependencies for data generation
- ✅ Sample music data from 3,494+ real tracks

### **⚙️ Manual Configuration**
1. **Get Redis Cloud connection**: Sign up at https://redis.com/try-free/
2. **Edit .env file**: Add your Redis Cloud connection string
3. **Open RDI Web UI**: http://localhost:8080

### 2. Verify Your Environment
```bash
# Test all connections
source .env
redis-cli -u "$REDIS_URL" ping
psql -U rdi_user -d rdi_db -h localhost -c "SELECT version();"
```

### 3. Start the Labs
```bash
# Begin with Lab 1
cd labs/01_postgres_to_redis
cat README.md
```

### 4. Monitor Your Progress
- **RedisInsight**: Explore your Redis Cloud data visually
- **Flag Checker**: `cd scripts && source ../.env && python3 check_flags.py`

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PostgreSQL    │───▶│   Redis RDI     │───▶│   Redis Cloud   │
│    (Local)      │    │   (Platform)    │    │   (Your DB)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                               │                        ▲
                               │                        │
                               ▼                        │
                   ┌─────────────────┐                  │
                   │  RedisInsight   │──────────────────┘
                   │     (Local)     │
                   └─────────────────┘
```

**Components:**
- **🏠 Local**: PostgreSQL, RedisInsight (you install)
- **☁️ Cloud**: Redis database + RDI platform (Redis Cloud)
- **🔗 Integration**: RDI handles real-time data synchronization

## 📚 Lab Overview

| Lab | Topic | Difficulty | Estimated Time |
|-----|-------|------------|----------------|
| **01** | PostgreSQL → Redis (Snapshot) | 🟢 Beginner | 15 minutes |
| **02** | Snapshot vs CDC | 🟡 Intermediate | 25 minutes |
| **03** | Advanced RDI Features | 🟠 Advanced | 20 minutes |

## 🎮 CTF Flags

Each lab contains a hidden flag. Collect all flags to complete the challenge:

```bash
# Check your progress
cd scripts
python3 check_flags.py
```

**Expected Flags:**
- `flag:01` → `RDI{pg_to_redis_success}`
- `flag:02` → `RDI{snapshot_vs_cdc_detected}`
- `flag:03` → `RDI{advanced_features_mastered}`

## 🛠️ Services & Ports

| Service | Port | Purpose |
|---------|------|---------|
| Redis | 6379 | Primary data store |
| RedisInsight | 8001 | Redis web UI |
| PostgreSQL | 5432 | Source database |
| Redis RDI | 8080 | RDI web interface |

## 📁 Directory Structure

```
Redis_RDI_CTF/
├── 📖 README.md                 # This file
├── 🐳 docker-compose.yml        # Service orchestration
├── ⚙️  .env.example             # Environment template
├── 🧪 labs/                     # Hands-on exercises
│   ├── 01_postgres_to_redis/    # Lab 1: Basic integration
│   ├── 02_snapshot_vs_cdc/      # Lab 2: Replication modes
│   └── 03_advanced_rdi/         # Lab 3: Advanced features
├── 🏴 flags/                    # CTF flag management
│   ├── flag_injector.lua        # Flag injection script
│   └── redis_flag_map.json      # Flag definitions
├── 🔧 scripts/                  # Utility scripts
│   ├── check_flags.py           # Progress checker
│   ├── setup_rdi_connectors.sh  # Connector setup
│   └── test_all_labs.sh         # Environment tester
└── 🌱 seed/                     # Sample data
    ├── postgres.sql             # Database schema & data
    └── track.csv                # Sample music data
```

## 🔧 Troubleshooting

### Services Won't Start
```bash
# Check Docker is running
docker --version

# View service logs
docker-compose logs <service-name>

# Restart all services
docker-compose down && docker-compose up -d
```

### Can't Connect to Services
```bash
# Check if ports are available
netstat -an | grep -E "(6379|5432|8001|8080)"

# Verify containers are running
docker ps
```

### Reset Environment
```bash
# Clean slate restart
docker-compose down -v
docker-compose up -d
```

## 🎓 Learning Resources

- [Redis Data Integration Documentation](https://redis.io/docs/data-integration/)
- [Redis Streams Guide](https://redis.io/docs/data-types/streams/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [RedisInsight Documentation](https://redis.com/redis-enterprise/redis-insight/)

## 🤝 Contributing

Found an issue or want to improve the labs? Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Learning! 🎉**

*Ready to become a Redis Data Integration expert? Start with Lab 1 and work your way through the challenges!*
