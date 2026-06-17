#!/bin/bash

# Launch backend and frontend servers in separate processes

set -e

echo "Starting DIP servers..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Launch backend server
echo "Starting backend server (fastapi dev)..."
cd "$SCRIPT_DIR/backend"
fastapi dev src/main.py &
BACKEND_PID=$!
echo "Backend server started with PID: $BACKEND_PID"

# Launch frontend server
echo "Starting frontend server (npm run dev)..."
cd "$SCRIPT_DIR/frontend"
npm run dev &
FRONTEND_PID=$!
echo "Frontend server started with PID: $FRONTEND_PID"

echo "Both servers are running:"
echo "  Backend PID: $BACKEND_PID"
echo "  Frontend PID: $FRONTEND_PID"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
