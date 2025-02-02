# 🚀 AFS WMS MVP

## **📌 Project Overview**
AFS WMS MVP is a **next-generation Warehouse Management System (WMS)** designed for **automation, AI-driven decision-making, and scalability**.  
It is built using **FastAPI** and **PostgreSQL**, with **Docker** for containerized services and **GitHub Actions** for CI/CD.

---

## **🔹 Features**
- ✅ **Modular Monorepo Architecture**
- ✅ **FastAPI-powered Backend**
- ✅ **PostgreSQL Database (via Docker)**
- ✅ **Automated CI/CD (Linting & Testing)**
- ✅ **Scalable for Future AI & Microservices**
- ✅ **Authentication & Role-Based Access Control (Planned)**

---

## **📥 Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/afs-wms-mvp.git
cd afs-wms-mvp
```

### **2️⃣ Set Up the Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
source venv/Scripts/activate  # Windows Git Bash
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the Database (Docker)**
Start PostgreSQL with Docker:

```sh
scripts/docker-up.sh
```

### **5️⃣ Run the FastAPI Server**
```sh
scripts/run.sh
```
📌 Visit the API Docs: http://localhost:8000/docs

---

## **🛠 Development Workflow**
### **📌 Running Tests**
Run unit tests:

```sh
scripts/test.sh
```
### **📌 Code Formatting & Linting**
To maintain clean code:

```sh
black src/
flake8 src/
```
### **📌 Stopping Services**
To stop running containers:

```sh
scripts/docker-down.sh
```
---
## **📌 Directory Structure**
```bash
afs-wms-mvp/
│── .github/workflows/       # CI/CD pipeline
│── docs/                    # Documentation
│── src/                     # Main application code
│   ├── backend/             # FastAPI backend
│   ├── automation/          # AI-driven optimizations (future)
│   ├── workers/             # Background job processing
│   ├── frontend/            # Web UI (future)
│── infra/                   # Infrastructure as Code (Terraform, Kubernetes)
│── tests/                   # Unit & integration tests
│── scripts/                 # Automation scripts
│── requirements.txt         # Python dependencies
│── Dockerfile               # Dockerized setup
│── docker-compose.yml       # Docker-compose configuration
│── .gitignore               # Git ignore list
│── README.md                # Project Overview
```
---
## **👥 Contributing**
1. Fork the repository.
2. Create a feature branch (feature/your-feature).
3. Open a Pull Request with your changes.

---
## **📌 Roadmap & Future Enhancements**
- **✅ Phase 1:** Backend Setup (FastAPI, PostgreSQL, CI/CD) 
- **🔄 Phase 2:** Authentication (JWT, OAuth2) 
- **🔄 Phase 3:** AI-Driven Optimization & Task Assignment 
- **🔄 Phase 4:** UI Development for Monitoring & Control 
- **🔄 Phase 5:** Cloud Deployment & Scaling
---
## **📄 License**
This project is licensed under the MIT License.