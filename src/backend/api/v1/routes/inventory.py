from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.backend.core.database import get_db
from src.backend.models.inventory import Inventory
from src.backend.schemas.inventory import (
    InventoryCreate,
    InventoryRead,
    InventoryUpdate,
)
from src.backend.services.inventory import InventoryService

router = APIRouter()


@router.get("/", response_model=List[InventoryRead])
def get_inventory(db: Session = Depends(get_db)):
    """Retrieve all inventory items."""
    return InventoryService.get_all(db)


@router.get("/{inventory_id}", response_model=InventoryRead)
def get_inventory_item(inventory_id: int, db: Session = Depends(get_db)):
    """Retrieve a single inventory item by ID."""
    item = InventoryService.get_by_id(db, inventory_id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item


@router.post("/", response_model=InventoryRead)
def create_inventory_item(item: InventoryCreate, db: Session = Depends(get_db)):
    """Add a new inventory item."""
    return InventoryService.create(db, item)


@router.put("/{inventory_id}", response_model=InventoryRead)
def update_inventory_item(
    inventory_id: int, item: InventoryUpdate, db: Session = Depends(get_db)
):
    """Update an existing inventory item."""
    updated_item = InventoryService.update(db, inventory_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return updated_item


@router.delete("/{inventory_id}")
def delete_inventory_item(inventory_id: int, db: Session = Depends(get_db)):
    """Delete an inventory item."""
    success = InventoryService.delete(db, inventory_id)
    if not success:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return {"message": "Item deleted successfully"}
