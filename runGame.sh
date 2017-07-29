#!/bin/bash
if hash python3 2>/dev/null; then
    ./halite/halite -d "30 30" "python3 MyBot/MyBot.py" "python3 RandomBot/RandomBot.py" "python3 RandomBot/RandomBot.py" "python3 RandomBot/RandomBot.py"
else
    ./halite/halite -d "30 30" "python MyBot/MyBot.py" "python RandomBot/RandomBot.py" "python RandomBot/RandomBot.py" "python RandomBot/RandomBot.py"
fi
