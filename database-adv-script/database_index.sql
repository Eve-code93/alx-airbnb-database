-- Create index on users.id (frequently used in JOINs with bookings)
CREATE INDEX idx_users_id ON users(id);

-- Create index on bookings.user_id (used in JOINs and WHERE clauses)
CREATE INDEX idx_bookings_user_id ON bookings(user_id);

-- Create index on bookings.property_id (used in JOINs with properties)
CREATE INDEX idx_bookings_property_id ON bookings(property_id);

-- Create index on bookings.start_date (helpful for date range filtering)
CREATE INDEX idx_bookings_start_date ON bookings(start_date);

-- Create index on properties.id (used in JOINs and WHERE clauses)
CREATE INDEX idx_properties_id ON properties(id);
