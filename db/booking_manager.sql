DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    age INT
    type VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
    review TEXT
)