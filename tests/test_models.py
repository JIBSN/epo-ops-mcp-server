"""
Test cases for number format handling in EPO OPS MCP Server
"""
import unittest
from epo_ops.models import Docdb, Epodoc
from epo_ops_mcp_server.models import DocdbInput, EpodocInput
from main import get_published_data, get_family, get_legal, convert_number, get_register

class TestNumberFormats(unittest.TestCase):
    
    def test_epodoc_input_model(self):
        """Test EpodocInput model validation"""
        # Valid Epodoc format
        data = {
            "number": "WO2025160170",
            "kind_code": "A1"
        }
        epodoc_input = EpodocInput(**data)
        self.assertEqual(epodoc_input.number, "WO2025160170")
        self.assertEqual(epodoc_input.kind_code, "A1")
    
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

if __name__ == '__main__':
    unittest.main()