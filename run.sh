#!/bin/bash

# PrivacyBot - Setup and Run Script
# This script sets up the environment and runs both the Flask backend and React frontend

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}PrivacyBot - Setup and Run${NC}"
echo -e "${GREEN}========================================${NC}\n"

# Check for Python
echo -e "${YELLOW}Checking for Python 3...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed. Please install Python 3.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✓ Found: $PYTHON_VERSION${NC}\n"

# Check for Node.js
echo -e "${YELLOW}Checking for Node.js...${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${RED}Node.js is not installed. Please install Node.js.${NC}"
    exit 1
fi
NODE_VERSION=$(node --version)
NPM_VERSION=$(npm --version)
echo -e "${GREEN}✓ Found Node.js: $NODE_VERSION${NC}"
echo -e "${GREEN}✓ Found npm: $NPM_VERSION${NC}\n"

# Setup Python Virtual Environment
echo -e "${YELLOW}Setting up Python virtual environment...${NC}"
if [ ! -d "PB_venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv PB_venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
source PB_venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}\n"

# Install Python dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
pip install -q --upgrade pip
pip install -q -r app/requirements.txt
echo -e "${GREEN}✓ Python dependencies installed${NC}\n"

# Install Node dependencies
echo -e "${YELLOW}Installing Node dependencies...${NC}"
cd PB_UI
npm install -q
echo -e "${GREEN}✓ Node dependencies installed${NC}\n"
cd ..

# Display startup information
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Starting PrivacyBot Services${NC}"
echo -e "${GREEN}========================================${NC}\n"
echo -e "${YELLOW}Services will start in the following seconds...${NC}"
echo -e "  ${GREEN}Flask Backend:${NC} http://localhost:5000"
echo -e "  ${GREEN}React Frontend:${NC} http://localhost:3000"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}\n"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${YELLOW}Shutting down services...${NC}"
    jobs -p | xargs -r kill 2>/dev/null || true
    echo -e "${GREEN}✓ Services stopped${NC}"
    exit 0
}

# Set trap to call cleanup function on script exit
trap cleanup EXIT INT TERM

# Start Flask backend
echo -e "${YELLOW}Starting Flask backend...${NC}"
cd app
source ../PB_venv/bin/activate
flask run --port 5000 &
FLASK_PID=$!
echo -e "${GREEN}✓ Flask started (PID: $FLASK_PID)${NC}"
sleep 2
cd ..

# Start React frontend
echo -e "${YELLOW}Starting React frontend...${NC}"
cd PB_UI
NODE_OPTIONS=--openssl-legacy-provider npm start &
REACT_PID=$!
echo -e "${GREEN}✓ React started (PID: $REACT_PID)${NC}"
cd ..

echo -e "\n${GREEN}✓ All services are running!${NC}\n"

# Wait for background processes
wait
