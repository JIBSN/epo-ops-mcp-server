"""
Example client for the EPO OPS MCP Server
"""
import json
from fastmcp import Client

# Connect to the MCP server
client = Client("http://localhost:8000")

def test_get_published_data_epodoc():
    """Test the get_published_data tool with Epodoc format."""
    # Example request for patent WO2025160170 using Epodoc format
    result = client.call_tool(
        "get_published_data",
        reference_type="publication",
        input_data={
            "number": "WO2025160170",
            "kind_code": "A1"
        },
        endpoint="biblio"
    )
    
    print(f"Published data result (Epodoc): {json.dumps(result, indent=2)}")

def test_get_published_data_docdb():
    """Test the get_published_data tool with Docdb format."""
    # Example request for patent WO2025160170 using Docdb format
    result = client.call_tool(
        "get_published_data",
        reference_type="publication",
        input_data={
            "country_code": "WO",
            "number": "2025160170",
            "kind_code": "A1"
        },
        endpoint="biblio"
    )
    
    print(f"Published data result (Docdb): {json.dumps(result, indent=2)}")

def test_search_published_data():
    """Test the search_published_data tool."""
    # Example search for patents with "artificial intelligence" in the title
    result = client.call_tool(
        "search_published_data",
        cql='title:"artificial intelligence"',
        range_begin=1,
        range_end=5
    )
    
    print(f"Search result: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    print("Testing EPO OPS MCP Server client")
    
    # Note: The following tests require the server to be running with valid EPO credentials
    # test_get_published_data_epodoc()
    # test_get_published_data_docdb()
    # test_search_published_data()
    
    print("Client example completed")