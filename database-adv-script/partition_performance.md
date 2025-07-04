# 📊 Partitioning Performance Report – Airbnb Bookings

This report summarizes performance improvements after partitioning the `bookings` table based on the `start_date` column.

---

## 🧱 Table Structure

Partitioned the `bookings` table by **year of `start_date`** using:

```sql
PARTITION BY RANGE (EXTRACT(YEAR FROM start_date))
