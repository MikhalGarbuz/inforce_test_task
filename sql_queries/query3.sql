-- Retrieve the details of users whose `signup_date` is within the last 7 days.

SELECT * 
FROM users
WHERE signup_date >= CURRENT_DATE - INTERVAL '7 days';

/* Explanation: 
    CURRENT_DATE: a function that returns the current date
    INTERVAL '7 days': a way to specify a time interval of 7 days
    CURRENT_DATE - INTERVAL '7 days': a way to calculate the date 7 days ago
*/