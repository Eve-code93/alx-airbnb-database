# 📊 Normalization – Airbnb Database

## 🎯 Objective
Apply database normalization principles to ensure the Airbnb database schema adheres to **Third Normal Form (3NF)**, eliminating data redundancy and ensuring data integrity.

---

## 🧱 Step-by-Step Normalization

---

### 🔹 First Normal Form (1NF)

**Goal:** Eliminate repeating groups and ensure atomic values.

✅ **Actions Taken:**
- All tables have **atomic fields** (no lists or multiple values in one column).
- No repeating groups (e.g., no `amenity_1`, `amenity_2`, etc.).
- Every column contains only **single-valued, indivisible data**.

---

### 🔹 Second Normal Form (2NF)

**Goal:** Remove partial dependencies — every non-key attribute must depend on the **entire** primary key.

✅ **Actions Taken:**
- All tables with composite keys were avoided by introducing UUIDs as primary keys.
- No table contains attributes that depend on part of a composite key.
- For example, in the `Booking` table, `total_price` depends on the entire booking record (dates + property + user), not just one part.

---

### 🔹 Third Normal Form (3NF)

**Goal:** Eliminate **transitive dependencies** — non-key attributes must not depend on other non-key attributes.

✅ **Actions Taken:**
- Removed derived fields like `total_nights`, `guest_name`, or `total_amount` that could be calculated from other fields or via joins.
- Ensured that all fields directly depend on the primary key.
- Examples:
  - `total_price` in `Booking` is calculated using business logic (e.g., `price_per_night * nights`) but kept for performance purposes — it doesn’t violate 3NF as it’s not duplicating other table values.
  - `role` in `User` is kept as a controlled ENUM, not inferred from other fields.

---

## ✅ Final Design Validation

| Table      | 1NF | 2NF | 3NF | Notes |
|------------|-----|-----|-----|-------|
| Users      | ✅  | ✅  | ✅  | No redundancies |
| Properties | ✅  | ✅  | ✅  | host_id → user_id |
| Bookings   | ✅  | ✅  | ✅  | Each field depends on booking_id |
| Payments   | ✅  | ✅  | ✅  | booking_id as FK ensures dependency |
| Reviews    | ✅  | ✅  | ✅  | rating and comment depend only on PK |
| Messages   | ✅  | ✅  | ✅  | sender_id and recipient_id clearly defined |

---

## 📝 Conclusion

The Airbnb database schema adheres to **Third Normal Form (3NF)**:
- All attributes are atomic.
- Every non-key attribute is fully functionally dependent on the whole primary key.
- No transitive dependencies are present.

This structure ensures:
- **Minimal redundancy**
- **Efficient data updates**
- **Scalability and maintainability**

---

