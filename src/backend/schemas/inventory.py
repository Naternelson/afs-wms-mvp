from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class InventoryBase(BaseModel):
    """Shared properties for inventory"""
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    is_active: bool = True

class InventoryCreate(InventoryBase):
    """Schema for creating an inventory item"""
    pass

class InventoryUpdate(InventoryBase):
    """Schema for updating an inventory item"""
    pass

class InventoryRead(InventoryBase):
    """Schema for returning inventory data"""
    id: int

    model_config = ConfigDict(from_attributes=True)  # New method
