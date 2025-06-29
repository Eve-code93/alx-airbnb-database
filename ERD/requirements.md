# ERD Requirements – Airbnb Database

## 📌 Objective

Design and document an **Entity-Relationship Diagram (ERD)** for the Airbnb database system. The ERD visually represents the database's structure, including all entities, their attributes, and the relationships between them.
## 🖼️ ER Diagram
[Airbnb ERD on dbdiagram.io](https://dbdiagram.io/d/airbnb-685a5448f039ec6d369aab1e)
---

## 📦 Entities and Attributes

### 🧑‍💼 User
- `user_id` (UUID, PK)
- `first_name` (VARCHAR, NOT NULL)
- `last_name` (VARCHAR, NOT NULL)
- `email` (VARCHAR, UNIQUE, NOT NULL)
- `password_hash` (VARCHAR, NOT NULL)
- `phone_number` (VARCHAR, NULL)
- `role` (ENUM: guest, host, admin)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

---

### 🏠 Property
- `property_id` (UUID, PK)
- `host_id` (UUID, FK → User.user_id)
- `name` (VARCHAR, NOT NULL)
- `description` (TEXT, NOT NULL)
- `location` (VARCHAR, NOT NULL)
- `pricepernight` (DECIMAL, NOT NULL)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (TIMESTAMP, updated on change)

---

### 📅 Booking
- `booking_id` (UUID, PK)
- `property_id` (UUID, FK → Property.property_id)
- `user_id` (UUID, FK → User.user_id)
- `start_date` (DATE, NOT NULL)
- `end_date` (DATE, NOT NULL)
- `total_price` (DECIMAL, NOT NULL)
- `status` (ENUM: pending, confirmed, canceled)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

---

### 💳 Payment
- `payment_id` (UUID, PK)
- `booking_id` (UUID, FK → Booking.booking_id)
- `amount` (DECIMAL, NOT NULL)
- `payment_date` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- `payment_method` (ENUM: credit_card, paypal, stripe)

---

### 📝 Review
- `review_id` (UUID, PK)
- `property_id` (UUID, FK → Property.property_id)
- `user_id` (UUID, FK → User.user_id)
- `rating` (INTEGER, CHECK: 1–5, NOT NULL)
- `comment` (TEXT, NOT NULL)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

---

### ✉️ Message
- `message_id` (UUID, PK)
- `sender_id` (UUID, FK → User.user_id)
- `recipient_id` (UUID, FK → User.user_id)
- `message_body` (TEXT, NOT NULL)
- `sent_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

---

## 🔗 Relationships

| Relationship                | Cardinality    |
|----------------------------|----------------|
| User ↔ Property            | 1:N (Host)      |
| User ↔ Booking             | 1:N (Guest)     |
| Property ↔ Booking         | 1:N             |
| Booking ↔ Payment          | 1:1             |
| User ↔ Review              | 1:N (Guest)     |
| Property ↔ Review          | 1:N             |
| User ↔ Message             | 1:N (Sender/Receiver) |

---

## 🗂️ Indexing and Constraints

- All primary keys are indexed by default.
- Unique constraint on `User.email`.
- Foreign key constraints:
  - `host_id` → User
  - `property_id` → Property
  - `user_id` → User
  - `booking_id` → Booking
- Enum values enforced with `CHECK`.

---

## 🖼️ Diagram Location

The visual ERD diagram is stored in this directory:

📁 `ERD/airbnb_erd.png`

If using Draw.io, you may also include:

📄 `ERD/airbnb_erd.drawio` (editable file)

---

## ✅ Status

- [x] All entities identified and documented
- [x] All relationships defined with cardinality
- [x] Diagram created and exported to `airbnb_erd.png`
- [x] File committed to GitHub in the correct directory

---

## 🧠 Notes

This ERD reflects a scalable and normalized design suitable for a production-like Airbnb clone. It will be referenced in later modules for schema creation, data seeding, and query writing.

