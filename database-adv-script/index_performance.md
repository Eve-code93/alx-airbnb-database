# 📈 Indexing for Performance – ALX Airbnb Database

This document explains the indexing strategy used to optimize query performance in the Airbnb database project. It highlights the high-usage columns, indexes created, and the difference in query performance before and after indexing using the `EXPLAIN` statement.

---

## 🔍 High-Usage Columns Identified

Through analysis of common SQL operations (joins, filters, sorting), the following columns were identified as bottlenecks and candidates for indexing:

| Table      | Column            | Reason for Indexing                        |
|------------|-------------------|--------------------------------------------|
| users      | id                | Used in joins with bookings                |
| bookings   | user_id           | Used in joins and WHERE clauses            |
| bookings   | property_id       | Used in joins with properties              |
| bookings   | start_date        | Used in WHERE clauses for filtering dates  |
| properties | id                | Used in joins and aggregations             |

---

## 🛠️ Indexes Created

```sql
CREATE INDEX idx_users_id ON users(id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_bookings_property_id ON bookings(property_id);
CREATE INDEX idx_bookings_start_date ON bookings(start_date);
CREATE INDEX idx_properties_id ON properties(id);
