# Use Python as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements first (to leverage Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Default command (can be overridden)
CMD ["bash"]
