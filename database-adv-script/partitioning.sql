-- Step 1: Drop the original table if it exists (be cautious in production)
DROP TABLE IF EXISTS bookings;

-- Step 2: Recreate the bookings table with PARTITIONING by RANGE (on start_date)
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT,
    property_id INT,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (property_id) REFERENCES properties(id)
)
PARTITION BY RANGE (EXTRACT(YEAR FROM start_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION pmax VALUES LESS THAN MAXVALUE
);

-- Step 3: Test performance with EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT * FROM bookings
WHERE start_date BETWEEN '2025-01-01' AND '2025-12-31';
