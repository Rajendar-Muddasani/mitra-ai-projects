# SQL Quick Reference Cheatsheet

---

## Basic SELECT
```sql
SELECT col1, col2, COUNT(*) AS cnt
FROM table_name
WHERE condition
ORDER BY col1 DESC
LIMIT 10;
```

## JOINs
```sql
-- INNER JOIN: only matching rows
SELECT s.name, p.salary
FROM students s
INNER JOIN placements p ON s.id = p.student_id;

-- LEFT JOIN: all left rows, matched right (NULLs for no match)
SELECT s.name, COALESCE(p.salary, 0) AS salary
FROM students s
LEFT JOIN placements p ON s.id = p.student_id;

-- FULL OUTER JOIN: all rows from both tables
SELECT * FROM a FULL OUTER JOIN b ON a.id = b.id;
```

## Aggregation
```sql
SELECT branch, COUNT(*) AS total, AVG(cgpa) AS avg_cgpa
FROM students
GROUP BY branch
HAVING COUNT(*) > 5  -- filter AFTER grouping
ORDER BY avg_cgpa DESC;
```

## Window Functions
```sql
-- RANK with gaps for ties
SELECT name, salary,
  RANK() OVER (PARTITION BY branch ORDER BY salary DESC) AS rnk
FROM students;

-- ROW_NUMBER no gaps
SELECT name,
  ROW_NUMBER() OVER (ORDER BY cgpa DESC) AS rn
FROM students;

-- LAG/LEAD: access previous/next row
SELECT date, revenue,
  LAG(revenue, 1) OVER (ORDER BY date) AS prev_revenue
FROM sales;

-- Running total
SELECT date, amount,
  SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;
```

## CTEs (Common Table Expressions)
```sql
WITH top_students AS (
  SELECT * FROM students WHERE cgpa > 8.5
),
placed AS (
  SELECT s.*, p.salary
  FROM top_students s
  JOIN placements p ON s.id = p.student_id
)
SELECT branch, AVG(salary) FROM placed GROUP BY branch;
```

## Subqueries
```sql
-- Find students above average CGPA
SELECT * FROM students
WHERE cgpa > (SELECT AVG(cgpa) FROM students);

-- IN subquery
SELECT * FROM orders
WHERE customer_id IN (
  SELECT id FROM customers WHERE city = 'Hyderabad'
);
```

## Common Interview Patterns
```sql
-- 2nd highest salary
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Duplicates
SELECT email, COUNT(*) FROM users
GROUP BY email HAVING COUNT(*) > 1;

-- Delete duplicates (keep lowest id)
DELETE FROM users
WHERE id NOT IN (
  SELECT MIN(id) FROM users GROUP BY email
);
```

## NULL Handling
```sql
IS NULL, IS NOT NULL
COALESCE(col, 0)        -- first non-NULL
NULLIF(a, b)            -- NULL if a=b else a
IFNULL(col, default)    -- MySQL
```

## String Functions
```sql
UPPER(str), LOWER(str)
TRIM(str), LTRIM, RTRIM
SUBSTRING(str, start, len)
CONCAT(a, ' ', b)
LENGTH(str)
LIKE 'A%'    -- starts with A
LIKE '%ing'  -- ends with ing
```
