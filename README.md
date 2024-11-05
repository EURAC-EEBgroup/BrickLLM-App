<p align="center">
  <img src="BrickApp/assets/brickllm_banner.png" alt="BrickLLM" style="width: 100%;">
</p>

# 🧱 BrickLLM App

BrickLLM is a web app for generating RDF files following the BrickSchema ontology using Large Language Models (LLMs). It is based on the python library BrickLLM - [pypi](https://pypi.org/project/brickllm/) and [github](https://github.com/EURAC-EEBgroup/brick-llm)

## Citation
Please cite us if you use the library

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14039358.svg)](https://zenodo.org/doi/10.5281/zenodo.14039358)



# Brief description
The open-source python web app has been developed using [Dash plotly](https://dash.plotly.com/) and the [dash mantine components](https://www.dash-mantine-components.com/). The tool can be used:

  - directly through the website hosted by [Eurac Reserch](https://https://www.eurac.edu/en/institutes-centers/institute-for-renewable-energy/research-group/energy-efficient-buildings/) at the following link
  - on-premises.

## On-premises
It is recommended to use a virtual environment such as Pipenv or Pyenv. For example: 

``` bash
    pipenv shell --python 3.12.6
    pipenv install
    source $(pipenv --venv)/bin/activate
```

The tool is currently tested with Python 3.12.6. After installing the required libraries using the command 

``` bash
pip install -r requirements.txt
```

the application can start 
1) locally: running the command inside the folder BrickApp

``` bash
python app.py
```
the actual port set up is: 8091

or create and use a docker container:

1. build dev docker image: 
``` bash 
    docker build --platform=linux/amd64 -t brick:dev .   
```

2. run docker compose: 
``` bash 
    docker compose up
```

# Example

### Possible issue running in Mac:

If there are these allerts
``` bash 
objc[9558]: +[NSString initialize] may have been in progress in another thread when fork() was called.
objc[9558]: +[NSString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
```

run in terminal:
``` bash
    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```




