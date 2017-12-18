# Starts the adventure

# Adventuring requires python3
PYTHON=$(which python3)

rc=$?
if [ ! $rc -eq 0 ]; then
    echo "error: python3 is needed for adventuring!"
    exit -1
fi

cd resources

# Adventures must be performed in a clean environment
env -i bash --noprofile --init-file <(echo "PYTHON=${PYTHON}; source ./present.cfg")
