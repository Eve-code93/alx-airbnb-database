# Airbnb Database Schema (schema.sql)

## 📄 Overview

This script creates the SQL schema for the Airbnb-like application. It includes:

- Proper use of UUIDs for primary keys
- Data types and constraints (e.g., `NOT NULL`, `CHECK`, `UNIQUE`)
- Foreign key relationships
- Indexes for optimized querying

## 📂 Tables

- `Users`
- `Properties`
- `Bookings`
- `Payments`
- `Reviews`
- `Messages`

## ⚙️ How to Run

Ensure you are connected to a PostgreSQL database, then run:

```bash
psql -U <your_username> -d <your_db_name> -f schema.sql
