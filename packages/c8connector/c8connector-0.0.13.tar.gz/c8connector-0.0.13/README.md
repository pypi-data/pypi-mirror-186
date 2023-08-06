# Implementing C8 Connectors.

Users can extend `C8Connector` interface and develop 3 types of connectors.

1. Source Connectors (Connectors that ingest data)
2. Target Connectors (Connectors that export data)
3. Integration Connectors (Generic integrations for other services)

When developing these connectors, developers must adhere to a few guidelines mentioned below.

## Naming the Connector

- Package name of the connector must be in the `c8-{type}-{connector}` format (i.e `c8-source-postgres`).
- Module name of the connector must be in the `c8_{type}_{connector}` format (i.e `c8_source_postgres`).

## Project structure (package names and structure)

- Project source code must follow the below structure.
```text
.
├── LICENSE
├── README.md
├── c8_{type}_{connector}
│        ├── __init__.py
│        └── main.py
│        └── {other source files or modules}
├── pyproject.toml
└── setup.cfg
```
- Within the `/c8_{type}_{connector}/__init__.py` there must be a class which implements `C8Connector` interface.

## Dependencies/Libraries and their versions to use.

- Connectors must only use following dependencies/libraries and mentioned versions' when developing.
```text
python = ">=3.7"
c8connector = "latest"
pipelinewise-singer-python = "1.2.0"
```
- Developers must not use `singer-sdk` or any other singer sdk variants other than `pipelinewise-singer-python`.

## Samples
- Postgres Source Connector: [Git Repository](https://github.com/Macrometacorp/c8-source-postgres)
- Oracle Source Connector: [Git Repository](https://github.com/Macrometacorp/c8-source-oracle)
- C8 Collections target Connector: [Git Repository](https://github.com/Macrometacorp/c8-target-c8collection)
