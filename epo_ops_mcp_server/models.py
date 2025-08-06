"""
Data models for EPO OPS MCP Server
"""
from typing import List, Optional, Union
from pydantic import BaseModel


class DocdbInput(BaseModel):
    '''
        **DocDB format** (structured, recommended for precision):
                Requires all three fields:
                ```json
                {
                    "country_code": "WO",
                    "number": "2025158691",
                    "kind_code": "A1"
                }
                ```
    ''' 
    number: str # 2025158691
    country_code: str # WO, EP, CN, US
    kind_code: str # A1, A2, B1, B2
    date: Optional[str] = None


class EpodocInput(BaseModel):
    ''' 
    **EpoDoc format** (compact, legacy-style):
            Requires a single `number` field:
            ```json
            {
                "number": "WO2025158691"
            }
            ```
'''
    number: str # WO2025158691
    kind_code: Optional[str] = None
    date: Optional[str] = None


class OriginalInput(BaseModel):
    number: str
    country_code: Optional[str] = None
    kind_code: Optional[str] = None
    date: Optional[str] = None


class PublishedDataRequest(BaseModel):
    
    """
    Request object for retrieving published patent data from EPO OPS.
    
    Supported reference_type include "publication", "application", or "priority"
    Supported endpoing include  "biblio", "equivalents", "abstract", "claims", "description", "fulltext", "images"
    Supported formats for `input`:
    - DocDB format: requires `country_code`, `number`, and `kind_code`
    - EpoDoc format: requires full `number` like "WO2025158268"

    Example (DocDB):
        {
            "reference_type": "publication",
            "input": {
                "country_code": "WO",
                "number": "2025158268",
                "kind_code": "A1"
            },
            "endpoint": "abstract"
        }

    Example (EpoDoc):
        {
            "reference_type": "publication",
            "input": {
                "number": "WO2025158268"
            },
            "endpoint": "biblio"
        }
    """
    
    reference_type: str  # "publication", "application", or "priority"
    input: Union[DocdbInput, EpodocInput]
    endpoint: str = "biblio"  # "biblio", "equivalents", "abstract", "claims", "description", "fulltext", "images"


class PublishedDataSearchRequest(BaseModel):
    cql: str
    range_begin: int = 1
    range_end: int = 25
    constituents: Optional[List[str]] = None # "biblio", "full-cycle", "abstract"


class FamilyRequest(BaseModel):
    reference_type: str  # "publication", "application", or "priority"
    input: Union[DocdbInput, EpodocInput]
    constituents: Optional[List[str]] = None


class LegalRequest(BaseModel):
    reference_type: str  # "publication", "application", or "priority"
    input: Union[DocdbInput, EpodocInput]


class NumberRequest(BaseModel):
    reference_type: str  # "publication", "application", or "priority"
    input: Union[OriginalInput, DocdbInput]
    output_format: str  # "original", "epodoc" or "docdb"


class RegisterRequest(BaseModel):
    reference_type: str  # "publication", "application", or "priority"
    input: EpodocInput
    constituents: Optional[List[str]] = None


class RegisterSearchRequest(BaseModel):
    cql: str
    range_begin: int = 1
    range_end: int = 25


class ImageRequest(BaseModel):
    path: str
    range: int = 1
    document_format: str = "application/tiff"