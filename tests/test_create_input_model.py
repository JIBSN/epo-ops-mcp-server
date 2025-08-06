"""
Test cases for input model creation in EPO OPS MCP Server
"""
import unittest
from epo_ops.models import Docdb, Epodoc, Original
from epo_ops_mcp_server.models import DocdbInput, EpodocInput, OriginalInput

class TestInputModels(unittest.TestCase):
    
    def test_create_docdb_model(self):
        """Test creating Docdb model from input data"""
        input_data = DocdbInput(
            country_code="WO",
            number="2025160170",
            kind_code="A1"
        )
        self.assertIsInstance(input_data, DocdbInput)
        self.assertEqual(input_data.country_code, "WO")
        self.assertEqual(input_data.number, "2025160170")
        self.assertEqual(input_data.kind_code, "A1")
    
    def test_create_epodoc_model_with_kind(self):
        """Test creating Epodoc model with kind_code"""
        input_data = EpodocInput(
            number="WO2025160170",
            kind_code="A1"
        )
        self.assertIsInstance(input_data, EpodocInput)
        self.assertEqual(input_data.number, "WO2025160170")
        self.assertEqual(input_data.kind_code, "A1")
    
    def test_create_epodoc_model_without_kind(self):
        """Test creating Epodoc model without kind_code"""
        input_data = EpodocInput(
            number="WO2025160170"
        )
        self.assertIsInstance(input_data, EpodocInput)
        self.assertEqual(input_data.number, "WO2025160170")
        self.assertIsNone(input_data.kind_code)
    
    def test_create_original_model(self):
        """Test creating Original model"""
        input_data = OriginalInput(
            number="WO2025160170",
            country_code=None,
            kind_code=None
        )
        self.assertIsInstance(input_data, OriginalInput)
        self.assertEqual(input_data.number, "WO2025160170")
        self.assertIsNone(input_data.country_code)
        self.assertIsNone(input_data.kind_code)

if __name__ == '__main__':
    unittest.main()