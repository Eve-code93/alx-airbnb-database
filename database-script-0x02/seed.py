-- Users
INSERT INTO Users (user_id, first_name, last_name, email, password_hash, phone_number, role)
VALUES 
  ('00000000-0000-0000-0000-000000000001', 'Alice', 'Wanjiku', 'alice@example.com', 'hash1', '0712345678', 'guest'),
  ('00000000-0000-0000-0000-000000000002', 'Brian', 'Otieno', 'brian@example.com', 'hash2', '0723456789', 'host'),
  ('00000000-0000-0000-0000-000000000003', 'Carol', 'Mutua', 'carol@example.com', 'hash3', '0734567890', 'admin');

-- Properties
INSERT INTO Properties (property_id, host_id, name, description, location, pricepernight)
VALUES 
  ('10000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', 'Nairobi Studio', 'Cozy studio in the heart of Nairobi', 'Nairobi, Kenya', 55.00),
  ('10000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002', 'Mombasa Beach House', 'Spacious beachfront villa', 'Mombasa, Kenya', 120.00);

-- Bookings
INSERT INTO Bookings (booking_id, property_id, user_id, start_date, end_date, total_price, status)
VALUES 
  ('20000000-0000-0000-0000-000000000001', '10000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2025-07-10', '2025-07-12', 110.00, 'confirmed'),
  ('20000000-0000-0000-0000-000000000002', '10000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', '2025-08-01', '2025-08-05', 480.00, 'pending');

-- Payments
INSERT INTO Payments (payment_id, booking_id, amount, payment_method)
VALUES 
  ('30000000-0000-0000-0000-000000000001', '20000000-0000-0000-0000-000000000001', 110.00, 'credit_card');

-- Reviews
INSERT INTO Reviews (review_id, property_id, user_id, rating, comment)
VALUES 
  ('40000000-0000-0000-0000-000000000001', '10000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', 5, 'Amazing place! Very clean and central.'),
  ('40000000-0000-0000-0000-000000000002', '10000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', 4, 'Loved the beach house vibe!');

-- Messages
INSERT INTO Messages (message_id, sender_id, recipient_id, message_body)
VALUES 
  ('50000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', 'Hi Brian, is the studio available this weekend?'),
  ('50000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', 'Yes! You can book directly from the listing.');
