from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TrackError(BaseException):
    ErrorSeverity: str
    ErrorCode: str
    ErrorDescription: str
    
    def __repr__(self) -> str:
        return f"""
    
    
        \rError Code: {self.ErrorCode}
        \rDescription: {self.ErrorDescription}
    """
    
    def __str__(self) -> str:
        return f"""
    
    
        \rError Code: {self.ErrorCode}
        \rDescription: {self.ErrorDescription}
    """