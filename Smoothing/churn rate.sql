-- Finding the chan rate for month of march
SELECT COUNT(DISTINCT user_id) AS 'enrollments',
  COUNT(CASE
       	WHEN strftime("%m", cancel_date) = '03'
        THEN user_id
  END) AS 'cancellations',
 	ROUND(100.0 * COUNT(CASE
       	WHEN strftime("%m", cancel_date) = '03'
        THEN user_id
  END) / COUNT(DISTINCT user_id)) AS 'churn_rate'
FROM pro_users
WHERE signup_date < '2020-04-01'

	AND (
    (cancel_date IS NULL) OR
    (cancel_date > '2020-03-01')
  );