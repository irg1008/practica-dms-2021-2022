![pylint score](https://github.com/irg1008/practica-dms-2021-2022/workflows/pylint%20score/badge.svg)
![mypy typechecking](https://github.com/irg1008/practica-dms-2021-2022/workflows/mypy%20typechecking/badge.svg) 

# DMS course project codebase, academic year 2021-2022

<img src="https://github.com/irg1008/practica-dms-2021-2022/blob/main/components/dms2122frontend/dms2122frontend/static/svg/logo.svg" width="200" />

The goal of this project is to implement a basic online evaluation appliance deployed across several interconnected services.

### Demo
![GIF](https://i.imgur.com/fNtsuQD.gif)

# Table of Contents
- [DMS course project codebase, academic year 2021-2022](#dms-course-project-codebase-academic-year-2021-2022)
  - [Documentation](#documentation)
    - [Spanish](#spanish)
  - [Changelog](#changelog)
    - [E3:](#e3)
  - [Developers:](#developers)
  - [Components](#components)
    - [Services](#services)
      - [`dms2122auth`](#dms2122auth)
      - [`dms2122backend`](#dms2122backend)
      - [`dms2122frontend`](#dms2122frontend)
    - [Libraries](#libraries)
      - [`dms2122core`](#dms2122core)
  - [Docker](#docker)
  - [Helper scripts](#helper-scripts)
  - [GitHub workflows and badges](#github-workflows-and-badges)



## Documentation
### Spanish
- [Deployment](docs/ES_es/Deployment.md)
- [Manual](docs/ES_es/Manual.md)
- Frontend
    * [Design](docs/ES_es/frontend/Design.md)
    * [Diagrams](docs/ES_es/frontend/Diagrams.md)
    * [Error Handling](docs/ES_es/frontend/Error_Handling.md)
- Backend
    * [Data](docs/ES_es/backend/data.md)
    * [Endpoints](docs/ES_es/backend/endpoints.md)
    * [Auth Process](docs/ES_es/backend/auth.md)
    * [Design](docs/ES_es/backend/Design.md)

## Changelog
### E3: 
- Updated Manuals
- Updated Frontend Design Readmes
- Added a new endpoint to fetch all the user stats
- Updated User Stats
- Teacher Role users can see the current stats of any student.

## Developers:
- [Jorge Ruiz Gómez](https://github.com/JorgeRuizDev)
- [Iván Ruiz Gázquez](https://github.com/irg1008)
- [Pablo Simón Sainz](https://github.com/ChocoAlmendrado)
- [Jesús Alonso Abad](https://github.com/Kencho)
## Components

The source code of the components is available under the `components` directory.

### Services

The services comprising the appliance are:

#### `dms2122auth`

This is the authentication service. It provides the user credentials, sessions and rights functionalities of the application.

See the `README.md` file for further details on the service.

#### `dms2122backend`

This service provides the evaluation logic (definition of questions, grading, etc.)

See the `README.md` file for further details on the service.

#### `dms2122frontend`

A frontend web service that allows to interact with the other services through a web browser.

See the `README.md` file for further details on the application.

### Libraries

These are auxiliar components shared by several services.

#### `dms2122core`

The shared core functionalities.

See the `README.md` file for further details on the component.

## Docker

The application comes with a pre-configured Docker setup to help with the development and testing (though it can be used as a base for more complex deployments).

To run the application using Docker Compose:

```bash
docker-compose -f docker/config/dev.yml up -d
```

When run for the first time, the required Docker images will be built. Should images be rebuilt, do it with:

```bash
docker-compose -f docker/config/dev.yml build
```

To stop and remove the containers:

```bash
docker-compose -f docker/config/dev.yml rm -sfv
```

By default data will not be persisted across executions. The configuration file `docker/config/dev.yml` can be edited to mount persistent volumes and use them for the persistent data.

To see the output of a container:

```bash
docker logs CONTAINER_NAME
# To keep printing the output as its streamed until interrupted with Ctrl+C:
# docker logs CONTAINER_NAME -f
```

To enter a running service as another subprocess to operate inside through a terminal:

```bash
docker exec -it CONTAINER_NAME /bin/bash
```

To see the status of the different containers:

```bash
docker container ps -a
```

## Helper scripts

The directory `scripts` contain several helper scripts.

- `verify-style.sh`: Runs linting (using pylint) on the components' code. This is used to verify a basic code quality. On GitHub, this CI pass will fail if the overall score falls below 7.00.
- `verify-type-correctness.sh`: Runs mypy to assess the type correctness in the components' code. It is used by GitHub to verify that no typing rules are broken in a commit.
- `verify-commit.sh`: Runs some validations before committing a changeset. Right now enforces type correctness (using `verify-type-correctness.sh`). Can be used as a Git hook to avoid committing a breaking change:
  Append at the end of `.git/hooks/pre-commit`:

  ```bash
  scripts/verify-commit.sh
  ```

## GitHub workflows and badges

This project includes some workflows configured in `.github/workflows`. They will generate the badges seen at the top of this document, so do not forget to update the URLs in this README file if the project is forked!
