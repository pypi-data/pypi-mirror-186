# Python Agent

### Usage
Python traceable agent requires Python >= 3.6

Additionally, to use the traceable filter, you must be on a supported OS. 
- Ubuntu 18.04+
- Centos 7+
- Debian 10+
- Amazon Linux 2+

### Instrumentation methods
There are two ways to instrument your application, auto-instrumentation and code based instrumentation.

#### Autoinstrumentation
Simply prepend `traceableai-instrument` to your applications startup command.

ex: `traceableai-instrument flask run`


#### Code based instrumentation
Add the following snippet to your python apps entrypoint file:
```python
from traceableai.agent import Agent

app = Flask(__name__)

agent = Agent()
agent.instrument(app) # This will instrument the flask app + any other modules that are supported
agent.add_traceable_filter() # add the traceable filter to enable blocking
```

### Developing
```bash
# Create a virtual env & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r dev-requirements 
```

_Note: if you run into an error installing grpc:_
> File "/Users/user/.pyenv/versions/3.9.4/lib/python3.9/distutils/unixccompiler.py", line 120, in _compile
> raise CompileError(msg)
> distutils.errors.CompileError: command '/usr/bin/clang' failed with exit code 1

_prepend this env var to the above pip install command:_ 
`GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true`

### Building
```bash
pip install -r requirements.txt
python3 -m build
```

### Instrumenting
```bash
traceableai-instrument your_startup_command
# ex: traceableai-instrument flask run -p 5000 
```

### Updating Libtraceable
1. Update the `libtraceable.h` header file if it has changed.
1. Edit `./src/download.py` and update the constant `LIBTRACEABLE_VERSION`.  
1. Verify using a test application in `docker/test_apps`. It will fail to build if libtraceable cannot be downloaded.
### Updating the Proto
```bash
git submodule update --init --recursive
./scripts/build_proto.sh
```
### Testing
- Unit tests
    1. Build the *.whl files. `build_artifacts.sh` builds all the whl files. Intentionally use the `CIBW_SKIP` environment variable to skip versions to save time. The example below only tests on 3.6.
        ```
        CIBW_SKIP="*37* *38* *39* *310*" ./build_artifacts.sh
        ```
    1. Build and run test in docker.
        ```
        docker build --build-arg ARTIFACTORY_USER --build-arg ARTIFACTORY_TOKEN -f docker/test_apps/unittest.Dockerfile -t pythonunittest .
        docker run --rm pythonunittest
        ```
- Test applications
    1. Refer to `docker/test_apps/`.
