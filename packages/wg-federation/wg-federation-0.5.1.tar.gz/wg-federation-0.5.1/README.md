# wg-federation

A WireGuard federation server and client.

## Development

Python `virtualenv` must be installed on your system.

```bash
# Setup
python -m venv venv
source ./venv/bin/activate
pip install -e ".[dev]"
pip install -e ".[build]" # optional: if you want to build locally
wg-federation # To run wg-federation

# Deactivate
deactivate
```

### Run Unit Tests
```bash
pytest -v --spec
pytest -v --cov # To see coverage
```

### Run Functional Tests

```bash
behave tests/features
behave tests/features -w # To see all outputs of all features tagged @wip
```

### Run SAST Tests

```bash
bandit -c pyproject.toml -r -q .
```

### Setup IDE and Debugger
To avoid having to install the dependencies on your operating system, setup your IDE to use a python virtual environment “SDK”.
E.g. the `venv` directory you may have created above.
[Intellij/PyCharm provides this feature](https://www.jetbrains.com/help/idea/creating-virtual-environment.html).
This will allow the IDE to find the libraries in the virtual environment, run and debug the application.

To debug the application, run `src/wg_federation/__init__.py`

### Deploy Manually

#### Build
```bash
python -m build
```

#### Publish to Test PyPI
_Use `__token__` as a username to publish using a token_
```bash
twine upload --repository testpypi dist/*
```

#### Publish in Production (PyPI)
_Use `__token__` as a username to publish using a token_
```bash
twine upload dist/*VERSION_HERE
```

### Generate the Documentation

```bash
sphinx-apidoc -o doc/ src/wg_federation # Generate API documentation directly from the code
pyreverse -o png -d doc/img --colorized --ignore container.py,federation.py,wireguard_interface.py,hq_state.py,controller_events.py,hq_event.py,wireguard_peer.py,constants.py,main.py,status.py,raw_options.py,log_level.py,is_argument_data_class.py,is_data_class.py,interface_status.py,configuration_saver_interface.py,configuration_loader_interface.py,can_save_configuration_interface.py,can_load_configuration_interface.py,user_input.py,command_line_argument.py,configuration_backend.py,argparse_action.py,command_line_option.py src/wg_federation # Generate UML diagram
make -C doc html # Generate HTML documentation fr²om .rst source code
```
