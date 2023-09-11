
CREATE TABLE assignments (
    assignment_id integer NOT NULL,
    name character varying(255),
    instructions text,
    release_date date,
    due_date date,
    max_points numeric,
    active boolean DEFAULT true
);

CREATE TABLE user_assignments (
    user_assignment_id integer NOT NULL,
    user_id integer,
    assignment_id integer,
    score numeric,
    recorded_on date,
    recorded_by integer
);

CREATE TABLE users (
    user_id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    andrew_id character varying(255),
    role character varying(255),
    section_id integer
);

-- Suggestions from Copilot:
SELECT * FROM assignments;

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

SELECT CONCAT(first_name, ' ', last_name) AS full_name, score FROM users JOIN user_assignments ON users.user_id = user_assignments.user_id WHERE assignment_id = 1;

SELECT CONCAT(first_name, ' ', last_name) AS full_name, score FROM users LEFT JOIN user_assignments ON users.user_id = user_assignments.user_id WHERE assignment_id = 1; -- fails, but close

