# Serving List of Pokemons

## Description

This project is a RESTful API built with FastAPI that serves a list of Pokémon data. It fetches data from the [PokeAPI](https://pokeapi.co/), stores it in a PostgreSQL database, and provides endpoints to retrieve Pokémon information, filter by name and type, and more.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/balibabu/pokemon
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Configure your PostgreSQL database connection by adding the `config.py` file. Ensure that the database connection details are correctly set in the configuration.
```shell
config = {
    "database": {
        "host": "localhost",
        "port": port_no,
        "database": "your_db_name",
        "user": "your_db_user",
        "password": "your_db_password",
    }
}
```

## Usage

- **Start the FastAPI Server:**
  Start the FastAPI server by running:

  ```shell
  python main.py
  ```

- **API Endpoints:**

  - **Get List of Pokemons:**
    - Endpoint: `/api/v1/pokemons`
    - Description: Retrieve a list of all Pokemons with their names, images, and types.

  - **Filter Pokemons:**
    - Endpoint: `/api/v1/pokemons/name={name}/type={_type}`
    - Description: Filter Pokemons by name and/or type. Replace `{name}` and `{_type}` with the desired filter criteria. Use "none" to specify no filter for a particular parameter.

- **Example Requests:**
  - Get all Pokemons: `http://localhost:8000/api/v1/pokemons`
  - Filter Pokemons by name: `http://localhost:8000/api/v1/pokemons/name=Charizard/type=none`
  - Filter Pokemons by type: `http://localhost:8000/api/v1/pokemons/name=none/type=Fire`


## Authors

- Bali Babu Chauhan

## Acknowledgments

- [PokeAPI](https://pokeapi.co/): The API used to fetch Pokémon data.
- [FastAPI](https://fastapi.tiangolo.com/): The Python framework used to create the RESTful API.
