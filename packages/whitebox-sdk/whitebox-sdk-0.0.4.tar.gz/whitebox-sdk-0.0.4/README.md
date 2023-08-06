6UgCjUTJzUiT;D$

# Whitebox - E2E machine learning monitoring

<p align="center">
  <a href="https://squaredev-io.github.io/whitebox">
    <img src="https://squaredev-io.github.io/whitebox/img/logo.svg" alt="Whitebox" width="50%">
  </a>
</p>
<p align="center">
    <em>Whitebox is an open source E2E ML monitoring platform with edge capabilities that plays nicely with kubernetes
</em>
</p>

---

**Documentation**: <a href="https://squaredev-io.github.io/whitebox/" target="_blank">https://squaredev-io.github.io/whitebox</a>

**Source Code**: <a href="https://github.com/squaredev-io/whitebox" target="_blank">https://github.com/squaredev-io/whitebox</a>

**Roadmap**: <a href="https://github.com/squaredev-io/whitebox/milestone/2" target="_blank">https://github.com/squaredev-io/whitebox/milestone/2</a>

---

Whitebox is an open source E2E ML monitoring platform with edge capabilities that plays nicely with kubernetes.

The key features are:

- **Classification models metrics**
- **Regression models metrics**
- **Data / model drift monitoring**
- **Alerts**

Design guidelines:

- **Easy**: Very easy to set up and get started with.
- **Intuitive**: Designed to be intuitive and easy to use.
- **Pythonic SDK**: Pythonic SDK for building your own monitoring infrastructure.
- **Robust**: Get production-ready MLOps system.
- **Kubernetes**: Get production-ready code. With automatic interactive documentation.

# How to use

## Run the server

The project is still in rapid development so to run the server clone the repo and run:

```bash
python -m venv .venv
pip install -r requirements.txt
ENV=dev uvicorn src.main:app --reload
```

In the near future you will be able to `pip install whitebox` and run `whitebox serve` to run whitebox.

## High level diagram of model set up

All you have to do is register a model and send inference data through the SDK.

```mermaid
sequenceDiagram
    actor user
    participant whitebox

    user->>user: Import sdk

    note over user, whitebox: Configure model and monitors
    user->>whitebox: Register model and training set via SDK
    whitebox-->>user: Model ID
    user->>whitebox: Log model inferences and actuals

    note over user, whitebox: You can now start monitoring metrics and get alerts
    user->>whitebox: Setup monitors to get specific alert
    whitebox-->>user: Get alerted when an anomaly occurs
```

# Set up locally for development

### Install packages:

```bash
python -m venv .venv
pip install -r requirements.txt
pre-commit install
```

### Run the server:

```bash
ENV=dev uvicorn src.main:app --reload
```

### Tests:

- Run: `ENV=test pytest -s`
- Watch: `ENV=test ptw`
- Run test coverage `ENV=test coverage run -m pytest`
- Look at coverage report: `coverage report` or `coverage html` to generate an html. To view it in your browser open the `htmlcov/index.html` file.

### Docs

**Documentation is hosted bby GitHub here**: <a href="https://squaredev-io.github.io/whitebox/" target="_blank">https://squaredev-io.github.io/whitebox</a>

```
mkdocs serve -f docs/mkdocs/mkdocs.yml -a localhost:8001
```

# Helm chart

You can install whitebox and all of its dependencies in your k8s cluster using helm

```bash
helm repo add squaredev https://chartmuseum.squaredev.io/
helm repo update
helm install whitebox squaredev/whitebox
```

# Contributing

We happily welcome contributions to Whitebox. You can start by opening a new issue!
