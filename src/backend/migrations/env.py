import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# Import the Base metadata from our FastAPI models
from src.backend.core.database import Base, DATABASE_URL
from src.backend.models.inventory import Inventory

# Load Alembic Config
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata (so Alembic knows which models to use)
target_metadata = Base.metadata

# Create the engine directly from our DATABASE_URL
def get_engine():
    return create_engine(DATABASE_URL, poolclass=pool.NullPool)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (no DB connection)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode (connects to DB)."""
    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
