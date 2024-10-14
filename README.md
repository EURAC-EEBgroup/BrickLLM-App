# Brick ontology tool
Application to create brick ontology starting from user prompt

## Requires
- python 3.12

## Development:
```
    pipenv shell --python 3.12.6
```
## Install dependencies 
```
    pipenv install
```
# Activate 
source $(pipenv --venv)/bin/activate

# As soon as the brick library it is not in pip 
install locally
```
    pip install dist_brick_local/brickllm-0.0.2.tar.gz
```

## issue running in Mac:
if there are these allerts
```
objc[9558]: +[NSString initialize] may have been in progress in another thread when fork() was called.
objc[9558]: +[NSString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
```

run in terminal:

    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES