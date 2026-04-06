# 💈 BarberPredict: SQL-Driven Pipeline & ML Forecasting

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Orange](https://img.shields.io/badge/Orange-Data_Mining-orange?style=for-the-badge&logo=orange&logoColor=white)

An end-to-end management system and predictive analysis tool for barbershops. This project integrates a robust Python/SQLite backend with a Machine Learning pipeline to forecast business demand.

## 📌 Overview
**BarberPredict** is a dual-purpose tool designed to handle real-world operations and data intelligence:
1.  **Manage Operations**: Handle staff, clients, and appointments via a clean CLI.
2.  **Predict Demand**: Use historical data to forecast peak hours using a **Decision Tree** model, allowing for optimized staff scheduling.

Built with a "Local First" philosophy, it ensures data privacy and high performance without external cloud dependencies.

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🔐 **Secure Logic** | Environment-variable based authentication with attempt limiting. |
| 🗄️ **Relational DB** | Full SQLite integration for Customers, Barbers, and Services. |
| 🔄 **ETL Pipeline** | Automated script to clean and transform SQL data into ML-ready features. |
| 🤖 **ML Forecasting** | Decision Tree model to predict if the shop will be "Busy" based on day/hour. |
| 📅 **Agenda Engine** | Smart scheduling with conflict prevention and persistence. |

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Database:** SQLite3 (Relational modeling)
* **Data Science:** Pandas (ETL) & Orange Data Mining (ML Modeling)
* **Architecture:** Modular Function-Based Design

---

## 🖥️ Project Structure

```bash
barber-predict-pipeline/
├── main.py              # Main application & ETL Engine
├── barber_logic.ows     # Orange ML Workflow schema
├── barbershop_data.csv  # Exported dataset for training
├── requirements.txt     # Project dependencies
├── .gitignore           # Safety: excludes .db and venv
├── docs/                # Screenshots and Architecture diagrams
└── README.md            # Professional documentation

⚡ Getting Started
1. Installation
Bash

# Clone the repository
git clone [https://github.com/ghcalado/SQL-Driven-Pipeline-ML-Demand-Forecasting.git](https://github.com/ghcalado/SQL-Driven-Pipeline-ML-Demand-Forecasting.git)

# Navigate to the folder
cd SQL-Driven-Pipeline-ML-Demand-Forecasting

# Install dependencies
pip install -r requirements.txt

2. Running the System
Bash

# Set your admin password (Optional)
export SENHA_BARBEARIA=your_password

# Run the application
python main.py

The database barbershop.db and the ML dataset barbershop_data.csv will be generated automatically.
3. Predictive Analysis

To view the Machine Learning logic:

    Open Orange Data Mining.

    Load the barber_logic.ows file.

    The workflow will automatically link to the generated .csv to show the Decision Tree.

📊 Visuals (Machine Learning Pipeline)
Data Workflow & Feature Engineering
Decision Tree Logic (Demand Prediction)
🚀 Roadmap

    [ ] Web Interface: Migrating the CLI to a FastAPI/React dashboard.

    [ ] Advanced Models: Testing Random Forests to improve prediction accuracy.

    [ ] WhatsApp API: Automated reminders for scheduled appointments.

👨‍💻 Author

Ghabriel Calado Computer Science Student | Python & Data Enthusiast
