-- Find the user(s) with the most common email domain.

WITH domain_counts AS (
    SELECT domain, COUNT(*) AS domain_count
    FROM users
    GROUP BY domain
),
common_domain AS (
    SELECT domain
    FROM domain_counts
    ORDER BY domain_count DESC
    LIMIT 1
)
SELECT users.*
FROM users
JOIN common_domain 
ON users.domain = common_domain.domain;

/* Explanation:
    domain_counts: CTE that counts the number of users for each domain
    common_domain: CTE that selects the domain with the highest count
    The final SELECT statement joins the users table with the common_domain CTE 
    to retrieve the users with the most common email domain.
*/