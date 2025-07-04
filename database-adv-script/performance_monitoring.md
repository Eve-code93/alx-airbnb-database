# 📊 Performance Monitoring & Refinement – Airbnb Database

This document outlines the process of monitoring frequently used queries, identifying bottlenecks, implementing improvements, and documenting performance gains.

---

## 🔍 Monitored Queries Using `EXPLAIN ANALYZE`

### 1. Booking Query (Initial)

```sql
EXPLAIN ANALYZE
SELECT 
    b.id, u.name, p.name, pay.amount
FROM bookings b
JOIN users u ON b.user_id = u.id
JOIN properties p ON b.property_id = p.id
JOIN payments pay ON pay.booking_id = b.id
WHERE b.start_date >= '2025-01-01'
AND pay.status = 'completed';
