"""
EPO Client service for EPO OPS MCP Server
"""
import epo_ops
from epo_ops.middlewares import Throttler
from epo_ops.middlewares.cache.dogpile import Dogpile
from epo_ops_mcp_server.config import settings

# Global client instance
_epo_client = None

def get_epo_client():
    """Create or return the EPO OPS client instance."""
    global _epo_client
    
    if _epo_client is None:
        # Set up middlewares
        middlewares = []
        
        # Add caching middleware if enabled
        if settings.CACHE_ENABLED:
            try:
                middlewares.append(Dogpile())
            except Exception:
                # If cache initialization fails, continue without it
                pass
        
        # Add throttling middleware (required)
        middlewares.append(Throttler())
        
        # Create client
        _epo_client = epo_ops.Client(
            key=settings.EPO_OPS_KEY,
            secret=settings.EPO_OPS_SECRET,
            middlewares=[]
        )
    
    return _epo_client