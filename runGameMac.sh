#!/bin/bash
if hash python3 2>/dev/null; then
    ./halite/haliteMac -d "30 30" "python3 TofuBot/TofuBot.py" "python3 RandomBot/RandomBot.py" "python3 RandomBot/RandomBot.py" "python3 RandomBot/RandomBot.py"
else
    ./halite/haliteMac -d "30 30" "python TofuBot/TofuBot.py" "python RandomBot/RandomBot.py" "python RandomBot/RandomBot.py" "python RandomBot/RandomBot.py"
fi
