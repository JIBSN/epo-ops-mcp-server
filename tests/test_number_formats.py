"""
Test cases for number format handling in EPO OPS MCP Server
"""
import unittest
from epo_ops.models import Docdb, Epodoc, Original
from epo_ops_mcp_server.models import DocdbInput, EpodocInput, OriginalInput

# Mock classes to simulate the InputObj used in _create_input_model
class MockInputObj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class TestNumberFormats(unittest.TestCase):
    
    def test_docdb_input_model(self):
        """Test DocdbInput model validation"""
        # Valid Docdb format
        data = {
            "country_code": "WO",
            "number": "2025160170",
            "kind_code": "A1"
        }
        docdb_input = DocdbInput(**data)
        self.assertEqual(docdb_input.country_code, "WO")
        self.assertEqual(docdb_input.number, "2025160170")
        self.assertEqual(docdb_input.kind_code, "A1")
    
    def test_epodoc_input_model(self):
        """Test EpodocInput model validation"""
        # Valid Epodoc format with kind_code
        data = {
            "number": "WO2025160170",
            "kind_code": "A1"
        }
        epodoc_input = EpodocInput(**data)
        self.assertEqual(epodoc_input.number, "WO2025160170")
        self.assertEqual(epodoc_input.kind_code, "A1")
        
        # Valid Epodoc format without kind_code
        data = {
            "number": "WO2025160170"
        }
        epodoc_input = EpodocInput(**data)
        self.assertEqual(epodoc_input.number, "WO2025160170")
        self.assertIsNone(epodoc_input.kind_code)
    
    def test_original_input_model(self):
        """Test OriginalInput model validation"""
        # Valid Original format with all fields
        data = {
            "number": "WO2025160170",
            "country_code": "WO",
            "kind_code": "A1"
        }
        original_input = OriginalInput(**data)
        self.assertEqual(original_input.number, "WO2025160170")
        self.assertEqual(original_input.country_code, "WO")
        self.assertEqual(original_input.kind_code, "A1")
        
        # Valid Original format with only number
        data = {
            "number": "WO2025160170"
        }
        original_input = OriginalInput(**data)
        self.assertEqual(original_input.number, "WO2025160170")
        self.assertIsNone(original_input.country_code)
        self.assertIsNone(original_input.kind_code)

if __name__ == '__main__':
    unittest.main()