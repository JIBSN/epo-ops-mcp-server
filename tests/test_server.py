"""
Unit tests for EPO OPS MCP Server
"""
import pytest
from epo_ops_mcp_server.main import mcp

def test_mcp_server_initialization():
    """Test that the MCP server is initialized correctly."""
    assert mcp is not None
    assert mcp.name == "EPO OPS MCP Server"

def test_tools_registered():
    """Test that all tools are registered."""
    tool_names = [tool.name for tool in mcp.tools]
    
    expected_tools = [
        "get_published_data",
        "search_published_data",
        "get_family",
        "get_legal",
        "convert_number",
        "get_register",
        "search_register",
        "get_image"
    ]
    
    for tool_name in expected_tools:
        assert tool_name in tool_names