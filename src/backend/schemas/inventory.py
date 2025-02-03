from pydantic import BaseModel
from typing import Optional

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

    class Config:
        from_attributes = True  # Ensures compatibility with SQLAlchemy ORM
