# EPO OPS MCP Server

A server that exposes the European Patent Office's Open Patent Services API as an MCP (Model Context Protocol) server using the fastMCP library.

## Features

- MCP-compatible server for accessing EPO OPS services
- Built-in authentication, throttling, and caching
- Automatic API documentation
- Docker support for easy deployment
- Dependency management with `uv` for fast installation
- Proper validation using Pydantic models

## Prerequisites

- Python 3.8+
- EPO OPS API credentials (key and secret)
- `uv` package manager (optional but recommended)

## Installation

### Option 1: Using `uv` (Recommended)

1. Clone the repository:
   ```
   git clone <repository-url>
   cd epo-ops-mcp-server
   ```

2. Install `uv` if you haven't already:
   ```
   pip install uv
   ```
   
   Or follow the [official installation guide](https://docs.astral.sh/uv/)

3. Install dependencies with `uv`:
   ```
   uv sync
   ```



## Usage

1. Set up environment variables:
   Create a `.env` file with your EPO OPS credentials:
   ```
   # EPO OPS API credentials (required)
   EPO_OPS_KEY=key
   EPO_OPS_SECRET=secret

   Server settings (optional)
   SERVER_HOST=0.0.0.0
   SERVER_PORT=8000

   # Cache settings (optional)
   CACHE_ENABLED=True
   CACHE_PATH=/var/tmp/epo-ops-server/cache.dbm
   ```

2. Start the server:
   ```
   python main.py
   ```

   Or with `uv`:
   ```
   uv run python main.py
   ```

## MCP client configuration

```
"mcpServers": {
    "epo-ops-mcp-server": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "main.py"
      ],
      "cwd": "path to epo-ops-mcp-server",
      "env": {
        "MCP_TRANSPORT_TYPE": "stdio",
        "MCP_LOG_LEVEL": "debug"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
```

## MCP Tools

The server exposes the following tools that can be used by MCP clients:

- `get_published_data` - Retrieve published patent data
- `search_published_data` - Search published patent data
- `get_family` - Retrieve patent family data
- `get_legal` - Retrieve legal status information
- `convert_number` - Convert patent number formats
- `get_register` - Retrieve European Patent Register data
- `search_register` - Search European Patent Register
- `get_image` - Retrieve patent images


### Number Formats

The EPO OPS API supports different patent number formats:

1. **Epodoc Format**: A single string that combines country, number, and kind code (e.g., "WO2025160170" or "US5444451A")
2. **Docdb Format**: Separate fields for country code, number, and kind code (e.g., "WO", "2025160170", "A1")

When using the tools, you can provide patent numbers in either format:

```python
# Epodoc format
{
  "number": "WO2025160170",
  "kind_code": "A1"
}

# Docdb format
{
  "country_code": "WO",
  "number": "2025160170",
  "kind_code": "A1"
}
```

The server now uses Pydantic models to validate the input data, ensuring that the correct format is used for each type of request. This provides better type safety and clearer error messages when invalid data is provided.

## Configuration

The server can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `EPO_OPS_KEY` | EPO OPS API key | *Required* |
| `EPO_OPS_SECRET` | EPO OPS API secret | *Required* |
| `SERVER_HOST` | Server host | `0.0.0.0` |
| `SERVER_PORT` | Server port | `8000` |
| `CACHE_ENABLED` | Enable caching | `True` |
| `CACHE_PATH` | Cache file path | `/var/tmp/epo-ops-server/cache.dbm` |

## Development

For development, you can install the dev dependencies:

With `uv`:
```
uv sync --extra=dev
```

With pip:
```
pip install -e .[dev]
```