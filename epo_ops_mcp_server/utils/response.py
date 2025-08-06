"""
Response utilities for EPO OPS MCP Server
"""
from typing import Any, Dict
import xml.etree.ElementTree as ET
import json


def format_response(content: str, content_type: str) -> Dict[str, Any]:
    """
    Format the response content based on its type.
    
    Args:
        content: The raw response content
        content_type: The content type header
        
    Returns:
        Formatted response dictionary
    """
    # Default response
    response = {
        "raw": content
    }
    
    # Try to parse as JSON
    if "application/json" in content_type:
        try:
            response["json"] = json.loads(content)
        except json.JSONDecodeError:
            pass
    
    # Try to parse as XML
    elif "application/xml" in content_type or "text/xml" in content_type:
        try:
            root = ET.fromstring(content)
            response["xml"] = {
                "tag": root.tag,
                "attributes": root.attrib,
                # Note: We're not including full element text to keep response size manageable
            }
        except ET.ParseError:
            pass
    
    return response