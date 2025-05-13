#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Personal Website...${NC}"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Virtual environment created.${NC}"
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install requirements if needed
echo -e "${GREEN}Checking dependencies...${NC}"
pip install flask flask-babel

# Start the application
echo -e "${GREEN}Starting server...${NC}"
python app.py &
APP_PID=$!

echo -e "${YELLOW}Waiting for the server to start...${NC}"
sleep 2

# Check if server started successfully
if ps -p $APP_PID > /dev/null; then
    echo -e "${GREEN}Server started successfully.${NC}"
    echo -e "${GREEN}Opening browser...${NC}"
    open http://127.0.0.1:5004/
    echo -e "${YELLOW}Website running on http://127.0.0.1:5004/${NC}"
    echo -e "${YELLOW}Press Ctrl+C to stop.${NC}"
    
    # Handle the Ctrl+C signal
    trap "echo -e '${RED}Stopping server...${NC}'; kill $APP_PID; echo -e '${GREEN}Server stopped.${NC}'; exit" INT
    
    wait $APP_PID
else
    echo -e "${RED}Failed to start server.${NC}"
    exit 1
fi 