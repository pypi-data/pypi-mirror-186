from dataclasses import dataclass, field
from typing import Optional, List, Self


@dataclass
class PluginContext:
    resource_id: str
    path: Optional[str] = None
    children: List[Self] = field(default_factory=list)
