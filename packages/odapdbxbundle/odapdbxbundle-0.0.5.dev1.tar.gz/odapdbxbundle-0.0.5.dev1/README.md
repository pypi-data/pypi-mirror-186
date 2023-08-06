# ODAP Databricks Bundle

## Overview

ODAP Databricks Bundle is a bundle containing connectors to various data sources to make importing and exporting of data easier.

ODAP Databricks Bundle supports metadata driven ingestion and exports of tables and files

It's build on top of the Databricks platform.

## Documentation
TODO 

### DBR & Python
DBR 10.4+ with python 3.8+ are supported

### Dependency management
Use `poetry` as main dependency management tool

### Linting & Formatting
- pylint
- pyre-check
- black

### Code style
- functions-only python (no dependency injection)
- try to avoid classes as much as possible
- data classes are OK
- no `__init__.py` files
- keep the `src` directory in root
- project config is raw YAML
- use type hinting as much as possible
