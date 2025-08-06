"""
Simple test script to verify the implementation
"""
from epo_ops_mcp_server.models import DocdbInput, EpodocInput, OriginalInput

def test_models():
    print("Testing DocdbInput model...")
    try:
        # Valid Docdb format
        data = {
            "country_code": "WO",
            "number": "2025160170",
            "kind_code": "A1"
        }
        docdb_input = DocdbInput(**data)
        print(f"DocdbInput validation successful: {docdb_input}")
    except Exception as e:
        print(f"DocdbInput validation failed: {e}")
    
    print("\nTesting EpodocInput model...")
    try:
        # Valid Epodoc format with kind_code
        data = {
            "number": "WO2025160170",
            "kind_code": "A1"
        }
        epodoc_input = EpodocInput(**data)
        print(f"EpodocInput validation successful: {epodoc_input}")
    except Exception as e:
        print(f"EpodocInput validation failed: {e}")
    
    try:
        # Valid Epodoc format without kind_code
        data = {
            "number": "WO2025160170"
        }
        epodoc_input = EpodocInput(**data)
        print(f"EpodocInput validation (without kind_code) successful: {epodoc_input}")
    except Exception as e:
        print(f"EpodocInput validation (without kind_code) failed: {e}")
    
    print("\nTesting OriginalInput model...")
    try:
        # Valid Original format with all fields
        data = {
            "number": "WO2025160170",
            "country_code": "WO",
            "kind_code": "A1"
        }
        original_input = OriginalInput(**data)
        print(f"OriginalInput validation successful: {original_input}")
    except Exception as e:
        print(f"OriginalInput validation failed: {e}")

if __name__ == "__main__":
    test_models()