<p align="center">
  <img src="BrickApp/assets/brickllm_banner.png" alt="BrickLLM" style="width: 100%;">
</p>

# 🧱 BrickLLM

BrickLLM is a web app for generating RDF files following the BrickSchema ontology using Large Language Models (LLMs). It is based on the python library BrickLLM

Citation
----------
Please cite us if you use the library

.. image:: https://zenodo.org/badge/761715706.svg
  :target: https://zenodo.org/doi/10.5281/zenodo.10887919


# Brief description
The open-source python web app has been developed using [Dash plotly](https://dash.plotly.com/) and the [dash mantine components](https://www.dash-mantine-components.com/). The tool can be used:
- [] directly through the website hosted by [Eurac Reserch](https://https://www.eurac.edu/en/institutes-centers/institute-for-renewable-energy/research-group/energy-efficient-buildings/) at the following link
- [] or on-premises.

# On-premises deployment
It is recommended to use a virtual environment such as Pipenv or Pyenv. The tool is currently tested with Python 3.12.6. After installing the required libraries using the command 

````
    pip install -r requirements.txt
```    

the application will start running the command inside the folder BrickApp

```
python app.py

```

# Example



# License

to run the ca
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


# Deployment: 

1. build dev docker image: 
```
    docker build --platform=linux/amd64 -t brick:dev .   
```

2. run docker compose: 
```
    docker compose up
```


