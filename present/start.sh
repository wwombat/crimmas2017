# Starts the adventure

# Adventuring requires python3
PYTHON=$(which python3)

# Adventures must be performed in a clean environment
env -i bash --noprofile --init-file <(echo "PYTHON=${PYTHON}; source ./present.cfg")
