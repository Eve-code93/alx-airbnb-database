# Airbnb Database Seed Script (seed.sql)

## 📄 Overview

This script populates the Airbnb relational database with sample data, simulating realistic usage scenarios.

## 📦 Tables Seeded

- `Users`: 3 users (guest, host, admin)
- `Properties`: 2 listings hosted by one user
- `Bookings`: 2 booking records
- `Payments`: 1 payment for a confirmed booking
- `Reviews`: 2 guest reviews
- `Messages`: 2 private messages between guest and host

## ⚙️ How to Run

Ensure your database schema is already created (from `schema.sql`). Then run:

```bash
psql -U <your_username> -d <your_db_name> -f seed.sql

