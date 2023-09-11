-- Given the following tables:
-- assignments(assignment_id, name, instructions, release_date, due_date, max_points, active);
-- user_assignments(user_assignment_id, user_id, assignment_id, score, recorded_on, recorded_by);
-- users(user_id, first_name, last_name, andrew_id, role, section_id);

-- FROM COPILOT:
-- Write a query that returns the records in the assignments table that have not been assigned to any user.
SELECT * FROM assignments WHERE assignment_id NOT IN (SELECT assignment_id FROM user_assignments);

-- Write a query that returns all users that have not been assigned to any assignment.
SELECT * FROM users WHERE user_id NOT IN (SELECT user_id FROM user_assignments);
SELECT * FROM users LEFT JOIN user_assignments ON users.user_id = user_assignments.user_id WHERE user_assignments.user_id IS NULL;