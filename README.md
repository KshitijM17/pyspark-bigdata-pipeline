# Big Data ETL Pipeline using PySpark

## Project Overview

This project implements a scalable ETL pipeline using PySpark to process large-scale e-commerce transactional datasets.

The pipeline performs:
- Data ingestion
- Data cleaning
- Transformations
- Revenue aggregation
- Spark SQL analytics
- Partitioned parquet storage

The project is fully containerized using Docker.

---

## Tech Stack

- Python
- PySpark
- Spark SQL
- Docker
- ETL
- Parquet
- SQL

---

## Features

✔ Distributed data processing  
✔ Spark SQL transformations  
✔ Revenue aggregation analytics  
✔ Partitioned parquet storage  
✔ Dockerized execution  
✔ ETL workflow implementation  

---

## Project Architecture

```text
CSV Dataset
    ↓
PySpark ETL Pipeline
    ↓
Data Cleaning & Transformation
    ↓
Spark SQL Analytics
    ↓
Partitioned Parquet Output
    ↓
Dockerized Deployment
```

---

## Dataset

E-Commerce transactional dataset from Kaggle.

---

## Sample Analytics Output

| Country | Revenue |
|---|---|
| United Kingdom | 7285024.64 |
| Netherlands | 285446.34 |
| EIRE | 265262.46 |

---

## How to Run

### 1. Clone Repository

```bash
git clone <repo-url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Project

```bash
python Scripts/main.py
```

---

## Docker Setup

### Build Docker Image

```bash
docker build -t pyspark-pipeline .
```

### Run Container

```bash
docker run pyspark-pipeline
```

---

## Resume Highlights

- Built scalable ETL pipeline using PySpark
- Implemented Spark SQL analytics and parquet partitioning
- Dockerized big data processing workflow
- Performed distributed transformations on transactional datasets

**Sceenshots 
Folder Structure**
<img width="388" height="615" alt="Screenshot 2026-05-29 141028" src="https://github.com/user-attachments/assets/fb4f165f-ef44-47f5-ac43-20ebb6560c0d" />

**Output**
<img width="1069" height="557" alt="Screenshot 2026-05-29 141056" src="https://github.com/user-attachments/assets/15d9bd39-302c-433c-bfe5-802b0f82b278" />

**Paraquets**
<img width="385" height="872" alt="Screenshot 2026-05-29 141117" src="https://github.com/user-attachments/assets/08d93845-c116-4c83-a163-5aa778bd1abf" />


