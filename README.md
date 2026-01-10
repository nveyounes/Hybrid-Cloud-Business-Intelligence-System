# ✨ Hybrid Cloud Business Intelligence System

> A robust, end-to-end data engineering project implementing a modern ELT pipeline, migrating local data to a serverless cloud data warehouse for real-time business analytics.

---

## 📊 Final Dashboard Preview

![Dashboard Screenshot](assets/dashboard_screenshot.png)

*An interactive dashboard analyzing sales trends, geographical performance, and order status.*

---

## 📖 About The Project

This project simulates a real-world scenario where an e-commerce company needs to consolidate data from disparate local sources into a centralized system for decision-making.

The goal was to build a scalable **Hybrid Cloud architecture** to extract data from local databases and files, transform it to ensure quality, load it into a cloud data warehouse, and visualize key performance indicators (KPIs).

### Key Objectives Achieved:

* 🚀 Implementation of a modern **ELT (Extract, Load, Transform)** architecture.
* ☁️ Migration from local storage to a **Serverless Cloud Data Warehouse (Neon PostgreSQL)**.
* 🛠️ Development of a **hybrid ETL process** using both low-code tools (Talend) and Code-First scripting (Python).
* 📈 Creation of a dynamic BI dashboard using **Google Looker Studio** with data blending.

---

## 🏗️ Architecture

The solution bridges local development environments with managed cloud services.

```mermaid
graph LR
    subgraph Local["Local Sources (macOS)"]
        A[MySQL DB - Clients Data]
        B[JSON Files - Orders Data]
    end

    subgraph ETL["ETL / Integration Layer"]
        D[Talend Open Studio]
        E[Python Script - Pandas/Psycopg2]
    end

    subgraph Cloud["Cloud Data Warehouse (AWS)"]
        F[(Neon Serverless PostgreSQL)]
    end

    subgraph BI["Business Intelligence"]
        G[Google Looker Studio]
    end

    A -->|Dimension Flow| D
    B -->|Fact Flow| E
    D -->|SSL Connection| F
    E -->|SSL Connection| F
    F -->|Native Connector| G

    style F fill:#00bb77,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#4285F4,stroke:#333,stroke-width:2px,color:#fff
```

### Data Flow:

1. **Ingestion:** Data is extracted from local MySQL (Clients) and JSON logs (Orders).
2. **Processing (Hybrid):**
   * **Talend** is used for standard relational loading of dimension tables.
   * **Python** is used for complex JSON parsing and robust ingestion of fact tables.
3. **Storage:** Data is centralized in **Neon**, a serverless PostgreSQL cloud database, using secure SSL connections.
4. **Visualization:** Looker Studio connects directly to the cloud DWH to render real-time charts.

---

## 🧰 Tech Stack

| Category | Technology | Description |
|----------|------------|-------------|
| **Data Source** | MySQL (Local) | Stores customer dimension data. |
| **Data Source** | JSON | Flat files containing transactional sales data. |
| **ETL Tool** | **Talend Open Studio** | Low-code tool used for loading the `Dim_Clients` table. |
| **ETL Language** | **Python 3.x** | Used (`pandas`, `psycopg2`) for ingestion of the `Fact_Orders` table. |
| **Data Warehouse** | **Neon (PostgreSQL)** | Serverless cloud database hosted on AWS. Selected for its free tier and standard SQL compatibility without requiring a credit card. |
| **BI / Visualization** | **Google Looker Studio** | Used for creating the final interactive dashboard and data blending. |

---

## ⚙️ Technical Challenges & Solutions (macOS Focus)

This project required overcoming specific environmental constraints, demonstrating adaptability in data engineering.

### 1. The macOS / Talend JSON Bug 🐛

* **Challenge:** On macOS (Apple Silicon), Talend Open Studio's standard `tFileInputJSON` component failed with persistent Java compilation errors (`"Statut cannot be resolved to a variable"`), preventing the loading of the orders file.
* **Solution:** Adopted a **Code-First approach** for the fact table. A robust Python script was developed to parse the JSON data and load it securely into PostgreSQL, bypassing the IDE limitations completely.

### 2. Looker Studio SSL Strictness 🔒

* **Challenge:** Looker Studio's PostgreSQL connector rejected default SSL connections to Neon, requiring a trusted certificate chain.
* **Solution:** Manually configured the connection by uploading the **ISRG Root X1 (.pem)** certificate to trust the Let's Encrypt authority used by Neon.

### 3. Flat Data Distribution 📉

* **Challenge:** Source test data contained orders all dated on the same day, rendering time-series analysis impossible.
* **Solution:** Applied SQL transformations directly in the Data Warehouse to randomize dates across the previous month to simulate realistic trends.

```sql
-- Example SQL used for transformation
UPDATE fact_orders
SET "DateCommande" = "DateCommande" - (FLOOR(RANDOM() * 30) || ' days')::INTERVAL;
```

---

## 🚀 How to Run the Python ETL Locally

You can replicate the ingestion of the "Orders" fact table using the provided script.

### Prerequisites

* Python 3.x installed.
* A Neon PostgreSQL database URL (or any Postgres instance).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nveyounes/Hybrid-Cloud-Business-Intelligence-System.git
   cd Hybrid-Cloud-Business-Intelligence-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Credentials**
   
   Open `etl_scripts/load_orders.py` and update the `DB_URL` variable with your actual Neon connection string.
   ```python
   # Example inside load_orders.py
   DB_URL = "postgres://user:password@ep-your-endpoint.aws.neon.tech/neondb?sslmode=require"
   ```

4. **Run the ETL Script**
   ```bash
   python etl_scripts/load_orders.py
   ```

*Output should confirm: `✅ SUCCESS! All orders loaded into the Cloud.`*

---

## 📁 Repository Structure

```
my-bi-project-repo/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── data/                     # Raw source data
│   └── commandes.json        
│
├── etl_scripts/              # ETL code
│   └── load_orders.py        
│
├── sql/                      # SQL queries
│   ├── create_tables.sql     
│   └── randomize_dates.sql   
│
└── assets/                   # Images
    └── dashboard_screenshot.png
```

---

## 📝 What I Learned

* Building production-grade ETL pipelines with hybrid approaches (low-code + code-first).
* Navigating platform-specific limitations and finding creative workarounds.
* Securing cloud database connections with SSL/TLS certificates.
* Designing star schemas for analytical workloads.
* Creating compelling data visualizations that tell a story.

---

## 🔮 Future Enhancements

- [ ] Implement incremental loading with change data capture (CDC)
- [ ] Add data quality checks and monitoring
- [ ] Automate the ETL pipeline with Apache Airflow
- [ ] Expand dimensional model with additional fact tables
- [ ] Deploy the dashboard with embedded analytics

---


## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, please consider giving it a star!**
