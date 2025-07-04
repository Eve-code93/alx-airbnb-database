-- Create indexes on frequently used columns
CREATE INDEX idx_users_id ON users(id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_bookings_property_id ON bookings(property_id);
CREATE INDEX idx_bookings_start_date ON bookings(start_date);
CREATE INDEX idx_properties_id ON properties(id);

-- Measure performance using EXPLAIN ANALYZE before and after indexing
-- Example query to analyze:
EXPLAIN ANALYZE
SELECT 
    b.id AS booking_id,
    u.name AS user_name,
    p.name AS property_name,
    b.start_date
FROM bookings b
JOIN users u ON b.user_id = u.id
JOIN properties p ON b.property_id = p.id
WHERE b.start_date >= '2025-01-01';
