# Serving List of Pokemons

## Description

This project is a RESTful API built with FastAPI that serves a list of Pokémon data. It fetches data from the [PokeAPI](https://pokeapi.co/), stores it in a PostgreSQL database, and provides endpoints to retrieve Pokémon information, filter by name and type, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the Repository:**
   ```shell
   git clone <repository-url>
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   Configure your PostgreSQL database connection by editing the `config.py` file. Ensure that the database connection details are correctly set in the configuration.

4. **Initialize the Database:**
   Run the following command to create the necessary database table:

   ```shell
   python main.py
   ```

## Usage

- **Start the FastAPI Server:**
  Start the FastAPI server by running:

  ```shell
  uvicorn main:app --host localhost --port 8000
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

## Configuration

Ensure that you configure your PostgreSQL database connection and other settings in the `config.py` file. Avoid hardcoding sensitive information and instead use configuration files or environment variables.

## Contributing

Contributions to this project are welcome. Please follow the standard GitHub fork and pull request workflow.

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

- [Your Name]

## Acknowledgments

- [PokeAPI](https://pokeapi.co/): The API used to fetch Pokémon data.
- [FastAPI](https://fastapi.tiangolo.com/): The Python framework used to create the RESTful API.

---

Replace `[Your Name]` in the Authors section with your name or the names of the project contributors. Additionally, make sure to replace `<repository-url>` with the URL of your Git repository where this project is hosted.