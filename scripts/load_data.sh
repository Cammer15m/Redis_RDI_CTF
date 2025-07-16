#!/bin/bash
# Simple Data Loader - One command to populate PostgreSQL
# Usage: ./load_data.sh

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🎵 Loading sample data for RDI testing...${NC}"

# Database config
DB_HOST=${DB_HOST:-localhost}
DB_PORT=${DB_PORT:-5432}
DB_NAME=${DB_NAME:-chinook}
DB_USER=${DB_USER:-postgres}
DB_PASSWORD=${DB_PASSWORD:-postgres}

# Check if PostgreSQL is running
if ! PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d postgres -c "SELECT 1;" > /dev/null 2>&1; then
    echo "❌ PostgreSQL not accessible. Starting it..."
    docker-compose up -d postgres
    sleep 5
fi

# Create database
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d postgres -c "CREATE DATABASE $DB_NAME;" 2>/dev/null || true

# Create tables
echo "📋 Creating tables..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f ../create_track_table.sql > /dev/null

# Load data using Python script
echo "📊 Loading sample data..."
python3 auto_load_data.py <<EOF


EOF

echo -e "${GREEN}✅ Data loading complete!${NC}"
echo ""
echo "🎯 Next steps:"
echo "  1. Start RDI to sync data to Redis"
echo "  2. Check data: psql -h localhost -U postgres -d chinook -c 'SELECT COUNT(*) FROM Track;'"
echo "  3. Generate more data: python3 auto_load_data.py"
