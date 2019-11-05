SELECT user_id, sum(amount * COALESCE(rate, 1)) as total_spent_gbp
FROM transactions
LEFT JOIN (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY (from_currency, to_currency) ORDER BY ts DESC) seq
    FROM exchange_rates) AS filtered_rates
ON transactions.currency = filtered_rates.from_currency
WHERE
    (filtered_rates.to_currency = 'GBP' AND seq = 1 )
    OR (transactions.currency = 'GBP')
GROUP BY user_id;
