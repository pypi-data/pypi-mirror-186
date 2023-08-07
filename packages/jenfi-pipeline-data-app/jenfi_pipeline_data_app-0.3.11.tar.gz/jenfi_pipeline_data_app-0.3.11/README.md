# Jenfi Pipeline Data App

Designed to allow teams to access Jenfi's data sources in a Jupyter Notebook.

## Docs

[View public API doc](https://jenfi-eng.github.io/pipeline-data) for using in Jupyter notebook.

## Basic Usage

```python
from jenfi_pipeline_data_app import PipelineDataApp as Jenfi

Jenfi.ROOT_DIR # => /Your/app/root/dir
```

Setup a `.env` file in the folder of `Jenfi.ROOT_DIR`

## Maintaining this repo

- Build pdoc - `pdoc --html --force --output-dir ./docs jenfi_pipeline_data_app`
