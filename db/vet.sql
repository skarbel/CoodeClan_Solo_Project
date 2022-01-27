DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    contact_details VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    pet_dob VARCHAR(255),
    pet_type VARCHAR(255),
    treatment_notes VARCHAR(255)
);