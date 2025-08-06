"""
Main fastMCP server implementation for EPO OPS
"""
import fastmcp
from epo_ops.models import Docdb, Epodoc, Original
from epo_ops_mcp_server.services.epo_client import get_epo_client
from epo_ops_mcp_server.utils.response import format_response

# Create FastMCP server instance
mcp = fastmcp.FastMCP("EPO OPS MCP Server")

def validate_pat_number(input_data):
    
    '''
        Convert dict to appropriate input model using Pydantic models for validation
        Determine if this is Docdb or Epodoc format based on presence of country_code
    '''

    if 'country_code' in input_data and input_data["country_code"] is not None:
        # Docdb format
        from epo_ops_mcp_server.models import DocdbInput
        validated_input = DocdbInput(**input_data)
        input_model = Docdb(
            number=validated_input.number,
            country_code=validated_input.country_code,
            kind_code=validated_input.kind_code,
            date=validated_input.date
        )
    else:
        # Epodoc format
        from epo_ops_mcp_server.models import EpodocInput
        validated_input = EpodocInput(**input_data)
        input_model = Epodoc(
            number=validated_input.number,
            kind_code=validated_input.kind_code,
            date=validated_input.date
        )
    
    return input_model

@mcp.tool()
def get_published_data(
    reference_type: str,
    input_data: dict,
    endpoint: str = "biblio"
):

    """
        Retrieve published patent information from the EPO OPS service.

        This function queries EPO's Open Patent Services (OPS) API using a given patent number
        and returns structured patent information such as bibliographic data, abstract, description,
        claims, or full text. The input patent number must be provided in either **docdb** or **epodoc**
        format.

        Args:
            input_data: Dictionary containing patent number information.
                        The format **must** be one of the following two options:

                        1. **DocDB format** (structured, recommended for precision):
                        Requires all three fields:
                        ```json
                        {
                            "country_code": "WO",
                            "number": "2025158691",
                            "kind_code": "A1"
                        }
                        ```

                        2. **EpoDoc format** (compact, legacy-style):
                        Requires a single `number` field:
                        ```json
                        {
                            "number": "WO2025158691"
                        }
                        ```

                        ⚠️ Important:
                        - You must use **either** docdb **or** epodoc format, not both.
                        - In **docdb**, all three fields are mandatory.
                        - In **epodoc**, the `number` must be a complete string including country code, number, and kind (e.g., "WO2025158691").

            reference_type: Type of reference used in the request.
                            Must be one of: `"publication"`, `"application"`, or `"priority"`.

            endpoint: The specific data section to retrieve from EPO OPS.
                    Common values include:
                    `"biblio"`, `"abstract"`, `"claims"`, `"description"`, `"fulltext"`, `"images"`.

        Returns:
            A formatted response from the EPO OPS API containing the requested section of the patent document.
    """

    client = get_epo_client()
    
    input_model = validate_pat_number(input_data)
    
    response = client.published_data(
        reference_type=reference_type,
        input=input_model,
        endpoint=endpoint,
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def search_published_data(
    cql: str,
    range_begin: int = 1,
    range_end: int = 25,
    constituents: list = None
):
    """
    
    Search for published patent documents using any keywords against European Patent Office(EPO) using its Open Patent Services(OPS) API.
    Accepts a CQL (Contextual Query Language) expression to specify the search criteria.
    
    Args:
        cql: CQL search query
        range_begin: Start of result range
        range_end: End of result range, maxminum is 1000.
        constituents: List of data constituents to retrieve. Must be one of "full-cycle", "abstract".
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    response = client.published_data_search(
        cql=cql,
        range_begin=range_begin,
        range_end=range_end,
        constituents=constituents
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def get_family(
    reference_type: str,
    input_data: dict,
    endpoint=None
):
    """
    Retrieve patent family data.
    
    Args:
        reference_type: "publication", "application", or "priority"
        input_data: Dictionary containing patent number information.
                        The format **must** be one of the following two options:

                        1. **DocDB format** (structured, recommended for precision):
                        Requires all three fields:
                        ```json
                        {
                            "country_code": "WO",
                            "number": "2025158691",
                            "kind_code": "A1"
                        }
                        ```

                        2. **EpoDoc format** (compact, legacy-style):
                        Requires a single `number` field:
                        ```json
                        {
                            "number": "WO2025158691"
                        }
                        ```

                        ⚠️ Important:
                        - You must use **either** docdb **or** epodoc format, not both.
                        - In **docdb**, all three fields are mandatory.
                        - In **epodoc**, the `number` must be a complete string including country code, number, and kind (e.g., "WO2025158691").
        constituents: List of data constituents to retrieve
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    input_model = validate_pat_number(input_data)
    
    response = client.family(
        reference_type=reference_type,
        input=input_model,
        endpoint=endpoint
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def get_legal(
    reference_type: str,
    input_data: dict
):
    """
    Retrieve legal status information.
    
    Args:
        reference_type: "publication", "application", or "priority"
        input_data: Dictionary containing patent number information.
                        The format **must** be one of the following two options:

                        1. **DocDB format** (structured, recommended for precision):
                        Requires all three fields:
                        ```json
                        {
                            "country_code": "WO",
                            "number": "2025158691",
                            "kind_code": "A1"
                        }
                        ```

                        2. **EpoDoc format** (compact, legacy-style):
                        Requires a single `number` field:
                        ```json
                        {
                            "number": "WO2025158691"
                        }
                        ```

                        ⚠️ Important:
                        - You must use **either** docdb **or** epodoc format, not both.
                        - In **docdb**, all three fields are mandatory.
                        - In **epodoc**, the `number` must be a complete string including country code, number, and kind (e.g., "WO2025158691").
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    input_model = validate_pat_number(input_data)
    
    response = client.legal(
        reference_type=reference_type,
        input=input_model
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def get_register(
    reference_type: str,
    input_data: dict,
    constituents: list = None
):
    """
    Retrieve European Patent Register data.
    
    Args:
        reference_type: "publication", "application", or "priority"
        input_data: Dictionary with patent number information (Epodoc format only)
        constituents: List of data constituents to retrieve
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    # Register only accepts Epodoc format
    from epo_ops_mcp_server.models import EpodocInput
    validated_input = EpodocInput(**input_data)
    input_model = Epodoc(
        number=validated_input.number,
        kind_code=validated_input.kind_code,
        date=validated_input.date
    )
    
    response = client.register(
        reference_type=reference_type,
        input=input_model,
        constituents=constituents
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def search_register(
    cql: str,
    range_begin: int = 1,
    range_end: int = 25
):
    """
    Search European Patent Register.
    
    Args:
        cql: CQL search query
        range_begin: Start of result range
        range_end: End of result range
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    response = client.register_search(
        cql=cql,
        range_begin=range_begin,
        range_end=range_end
    )
    
    return format_response(response.text, response.headers.get('content-type', ''))

@mcp.tool()
def get_image(
    path: str,
    range_val: int = 1,
    document_format: str = "application/tiff"
):
    """
    Retrieve patent images.
    
    Args:
        path: Image path
        range_val: Range parameter
        document_format: Document format
        
    Returns:
        Formatted response from EPO OPS API
    """
    client = get_epo_client()
    
    response = client.image(
        path=path,
        range=range_val,
        document_format=document_format
    )
    
    # For images, we might want to return the content differently
    return format_response(response.text, response.headers.get('content-type', ''))

if __name__ == "__main__":
    # Run the server
    mcp.run()