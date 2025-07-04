# 🧠 Optimization Report – Airbnb Database

This report describes the performance optimization of a complex SQL query joining multiple tables.

---

## 🎯 Objective

Retrieve booking details along with user, property, and payment info using a performant query.

---

## 🔍 Initial Query (Before Optimization)

```sql
SELECT 
    b.id, u.name, p.name, pay.amount, pay.status
FROM bookings b
JOIN users u ON b.user_id = u.id
JOIN properties p ON b.property_id = p.id
JOIN payments pay ON pay.booking_id = b.id;
