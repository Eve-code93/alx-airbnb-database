# 🧠 SQL Join Queries – ALX Airbnb Database Project

This task is part of the **ALX Airbnb Database Module**, focused on mastering SQL joins by querying a simulated Airbnb database. We use `INNER JOIN`, `LEFT JOIN`, and `FULL OUTER JOIN` to retrieve and analyze data across related tables like `users`, `bookings`, `properties`, and `reviews`.

---

## 🎯 Objective

Write complex SQL queries using different types of joins to retrieve meaningful, relational data.

---

## 🔧 Queries Implemented

### 1. 🔗 INNER JOIN – Bookings & Users

**Goal:** Retrieve all bookings along with the users who made them.

```sql
SELECT 
    b.id AS booking_id,
    u.id AS user_id,
    u.name AS user_name,
    b.property_id,
    b.start_date,
    b.end_date
FROM bookings b
INNER JOIN users u ON b.user_id = u.id;
📝 Returns only those bookings that are linked to a valid user.

2. 🧩 LEFT JOIN – Properties & Reviews
Goal: Retrieve all properties and any reviews they may have (even if there are no reviews).

sql
Copy
Edit
SELECT 
    p.id AS property_id,
    p.name AS property_name,
    r.id AS review_id,
    r.comment,
    r.rating
FROM properties p
LEFT JOIN reviews r ON p.id = r.property_id;
📝 Ensures every property appears in the result, with NULL for properties without reviews.

3. 🔄 FULL OUTER JOIN – Users & Bookings
Goal: Retrieve all users and all bookings, even if a user has no booking or a booking is not linked to a user.

Note: MySQL does not support FULL OUTER JOIN natively. We simulate it using UNION of LEFT and RIGHT joins:

sql
Copy
Edit
SELECT 
    u.id AS user_id,
    u.name AS user_name,
    b.id AS booking_id,
    b.property_id,
    b.start_date
FROM users u
LEFT JOIN bookings b ON u.id = b.user_id

UNION

SELECT 
    u.id AS user_id,
    u.name AS user_name,
    b.id AS booking_id,
    b.property_id,
    b.start_date
FROM users u
RIGHT JOIN bookings b ON u.id = b.user_id;

# 🔍 Subqueries – ALX Airbnb Database Project

This task focuses on practicing **non-correlated** and **correlated** subqueries using a simulated Airbnb database.

---

## 🧠 Objective

- Use a **non-correlated subquery** to filter properties based on average review ratings.
- Use a **correlated subquery** to filter users based on the number of bookings they've made.

---

## 📄 Queries Implemented

### 1. ⭐ Properties with Avg Rating > 4.0

```sql
SELECT * 
FROM properties
WHERE id IN (
    SELECT property_id
    FROM reviews
    GROUP BY property_id
    HAVING AVG(rating) > 4.0
);
---

## 📊 Aggregations and Window Functions

This task uses SQL aggregation functions and analytical window functions to derive insights from booking data.

---

### 1. 🧮 Total Bookings Per User

```sql
SELECT 
    u.id AS user_id,
    u.name AS user_name,
    COUNT(b.id) AS total_bookings
FROM users u
LEFT JOIN bookings b ON u.id = b.user_id
GROUP BY u.id, u.name
ORDER BY total_bookings DESC;
