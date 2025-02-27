import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.backend.core.database import Base, get_db
from fastapi.testclient import TestClient
from src.backend.main import app

# ✅ Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    """Create a new database session for a test."""
    Base.metadata.create_all(bind=engine)  # Create tables before test
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()
        Base.metadata.drop_all(bind=engine)  # Cleanup after test

# ✅ Override FastAPI dependency to use test database
@pytest.fixture(scope="function", autouse=True)
def override_get_db(monkeypatch):
    """Override the FastAPI dependency injection to use test database"""
    monkeypatch.setattr("src.backend.core.database.get_db", lambda: db())

@pytest.fixture(scope="module")
def client():
    """Create a FastAPI test client using the test database."""
    return TestClient(app)
