from sqlalchemy.orm import Session
from src.backend.models.inventory import Inventory
from src.backend.schemas.inventory import InventoryCreate, InventoryUpdate

class InventoryService:
    @staticmethod
    def get_all(db: Session):
        """Retrieve all inventory items"""
        return db.query(Inventory).all()

    @staticmethod
    def get_by_id(db: Session, inventory_id: int):
        """Retrieve a single inventory item"""
        return db.query(Inventory).filter(Inventory.id == inventory_id).first()

    @staticmethod
    def create(db: Session, item: InventoryCreate):
        """Create a new inventory item"""
        db_item = Inventory(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update(db: Session, inventory_id: int, item: InventoryUpdate):
        """Update an existing inventory item"""
        db_item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
        if not db_item:
            return None
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def delete(db: Session, inventory_id: int):
        """Delete an inventory item"""
        db_item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
        if not db_item:
            return False
        db.delete(db_item)
        db.commit()
        return True
