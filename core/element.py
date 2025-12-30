from dataclasses import dataclass 
from typing import Optional

@dataclass
class AccessibleElement: 
    name: str
    role: str
    value: Optional[str] = None
    enabled: bool = true
    checked: Optional[bool] = None
    