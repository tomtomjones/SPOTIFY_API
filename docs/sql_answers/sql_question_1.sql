USE DATABASE TAKE_HOME_CHALLENGE;

-- monthly active sellers with 25 or more sales in the month
WITH MONTHLY_TOTAL AS (
  SELECT MONTH, COUNT(ORDERS_PER_MONTH) AS MONTHLY_TOTAL
  FROM (
    SELECT OI.SELLER_ID
    , EXTRACT(MONTH FROM O.ORDER_PURCHASE_TIMESTAMP) AS MONTH
    , COUNT(DISTINCT OI.ORDER_ID) AS ORDERS_PER_MONTH
    FROM ECOMMERCE.ORDERS O
    INNER JOIN ECOMMERCE.ORDER_ITEMS OI ON O.ORDER_ID = OI.ORDER_ID
    WHERE EXTRACT(YEAR FROM O.ORDER_PURCHASE_TIMESTAMP) = 2017 
    GROUP BY OI.SELLER_ID, MONTH
    HAVING ORDERS_PER_MONTH >= 25
   ) GROUP BY MONTH
), 
-- avg. weekly active sellers with 5 or more sales in the week
WEEKLY_AVG AS (
  SELECT MONTH, AVG(active_sellers_per_week) AS WEEKLY_AVERAGE
  FROM (
    select MONTH, WEEK_START, count(seller_id) as active_sellers_per_week
    from (
      SELECT OI.SELLER_ID
      , DATE_TRUNC('WEEK', O.ORDER_PURCHASE_TIMESTAMP) AS WEEK_START
      , EXTRACT(MONTH FROM WEEK_START) AS MONTH
      , COUNT(DISTINCT OI.ORDER_ID) AS WEEKLY_COUNT

      FROM ECOMMERCE.ORDERS O
      INNER JOIN ECOMMERCE.ORDER_ITEMS OI ON O.ORDER_ID = OI.ORDER_ID
      WHERE EXTRACT(YEAR FROM O.ORDER_PURCHASE_TIMESTAMP) = 2017 
      GROUP BY OI.SELLER_ID, month, WEEK_START
      HAVING WEEKLY_COUNT >= 5
    ) wkly
    group by MONTH, WEEK_START
   )
   group by MONTH
),
-- avg. daily active sellers
DAILY_AVG AS (
  SELECT MONTH, AVG(active_sellers_per_DAY) AS DAILY_AVERAGE
  FROM (
    select MONTH, DAY, count(seller_id) as active_sellers_per_DAY
    from (
      SELECT OI.SELLER_ID
      , EXTRACT(DAY FROM O.ORDER_PURCHASE_TIMESTAMP) AS DAY
      , EXTRACT(MONTH FROM O.ORDER_PURCHASE_TIMESTAMP) AS MONTH
      , COUNT(DISTINCT OI.ORDER_ID) AS DAILY_COUNT
      FROM ECOMMERCE.ORDERS O
      INNER JOIN ECOMMERCE.ORDER_ITEMS OI ON O.ORDER_ID = OI.ORDER_ID
      WHERE EXTRACT(YEAR FROM O.ORDER_PURCHASE_TIMESTAMP) = 2017 
      GROUP BY OI.SELLER_ID, MONTH, DAY
    ) wkly
    group by MONTH, DAY
   )
   group by MONTH
)

SELECT CASE
    WHEN MT.MONTH = 1 THEN 'January'
    WHEN MT.MONTH = 2 THEN 'February'
    WHEN MT.MONTH = 3 THEN 'March'
    WHEN MT.MONTH = 4 THEN 'April'
    WHEN MT.MONTH = 5 THEN 'May'
    WHEN MT.MONTH = 6 THEN 'June'
    WHEN MT.MONTH = 7 THEN 'July'
    WHEN MT.MONTH = 8 THEN 'August'
    WHEN MT.MONTH = 9 THEN 'September'
    WHEN MT.MONTH = 10 THEN 'October'
    WHEN MT.MONTH = 11 THEN 'November'
    WHEN MT.MONTH = 12 THEN 'December'
END AS MONTH_2017
, MT.MONTHLY_TOTAL
, WA.WEEKLY_AVERAGE
, DA.DAILY_AVERAGE
FROM MONTHLY_TOTAL MT
JOIN WEEKLY_AVG WA ON MT.MONTH = WA.MONTH
JOIN DAILY_AVG DA ON MT.MONTH = DA.MONTH
ORDER BY MT.MONTH ASC
;
