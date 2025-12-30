from dataclasses import dataclass 
from typing import Optional

@dataclass
class AccessibleElement: 
    name: str
    role: str
    value: Optional[str] = None
    enabled: bool = True
    checked: Optional[bool] = None
    