<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Workcell
</h1>

<p align="center">
    <strong>Instantly turn your Python function into production-ready microservice.</strong>
</p>

<p align="center">
    <a href="https://pypi.org/project/workcell/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/workcell?color=green&style=flat"></a>
    <a href="https://pypi.org/project/workcell/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>
    <a href="https://github.com/weanalyze/workcell/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache2.0-blue.svg"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#license">License</a> •
  <a href="https://github.com/weanalyze/workcell/releases">Changelog</a>
</p>

Instantly turn your Python function into production-ready microservice, with lightweight UI to interact with. Use / Share / Publish / Collaborate with your team. 

<sup>Pre-alpha Version: Not feature-complete and only suggested for experimental usage.</sup>

<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>

---

## Highlights

- 🪄&nbsp; Turn functions into production-ready services within seconds.
- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.
- 📦&nbsp; Deploy microservice into weanalye FaaS cloud.
- 🧩&nbsp; Reuse pre-defined templates & combine with existing components.
- 📈&nbsp; Instantly deploy and scale for production usage.

## Getting Started

### Installation

> _Requirements: Python 3.8+._

```bash
pip install workcell
```

### Usage

1. A simple workcell-compatible function could look like this:

    ```python
    from pydantic import BaseModel

    class Input(BaseModel):
        message: str

    class Output(BaseModel):
        message: str

    def hello_workcell(input: Input) -> Output:
        """Returns the `message` of the input data."""
        return Output(message=input.message)
    ```

    _💡 A workcell-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._

2. Copy this code to a file named `app.py`, put into a folder, e.g. `hello_workcell`

3. Run the HTTP API server from command-line:

    ```bash
    cd hello_workcell
    workcell serve app:hello_workcell
    ```
    _In the output, there's a line that shows where your API is being served, on your local machine._

4. Run the Streamlit based UI server from command-line:

    ```bash
    workcell serve-ui app:hello_workcell
    ```
    _In the output, there's a line that shows where your UI is being served, on your local machine._

5. Deploy the service into weanalyze cloud from command-line:

    ### requirements

    - [Docker](https://docker.com/) installed
    - [Dockerhub](https://hub.docker.com/) account
    - [Weanalyze](https://weanalyze.co) account

    You need both [dockerhub](https://hub.docker.com/) and [weanalyze](https://weanalyze.co) account to deploy your function.

    Set environment variable `DOCKERHUB_USERNAME` as your dockerhub username:

    ```bash
    export DOCKERHUB_USERNAME={YOUR_DOCKERHUB_USERNAME}
    ```

    or save it into `.env` under your project folder. Your project dir may seems like this:

    ```bash
    hello_workcell
    ├── .env
    ├── app.py
    └── requirements.txt    
    ```

    ### usage

    Let's deploy your function on weanalyze cloud! 

    First, login on weanalyze cloud:
    
    ```bash
    # login on weanalyze cloud
    workcell login -u {WEANALYZE_USERNAME}    
    ```

    In your project folder:

    ```bash
    # 1-click deploy!
    workcell up app:hello_workcell
    ```
    _In the output, there's a line that shows where your serverless funtion is being served, on weanalyze cloud._

    If you want to deploy function in multiple steps:
    
    ```bash
    workcell build app:hello_workcell
    workcell push
    ```
    _Build workcell into docker image, then push to dockerhub._

    ```bash
    workcell deploy
    ```
    _Deploy builded docker image on weanalyze cloud._


5. Find out more usage information and get inspired by our [examples](https://github.com/weanalyze/workcell/tree/main/examples).

## License

Apache-2.0 License.
