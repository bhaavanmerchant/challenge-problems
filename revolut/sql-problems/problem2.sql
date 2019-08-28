SELECT user_id, sum(converted_amount) as total_spent_gbp
FROM
    (
    SELECT user_id, amount * COALESCE(rate, 1) as converted_amount,
    ROW_NUMBER() OVER (PARTITION BY (transactions.ts, user_id, currency) ORDER BY exchange_rates.ts DESC) seq
    FROM transactions
    LEFT JOIN exchange_rates
    ON transactions.currency = exchange_rates.from_currency
    WHERE
        (exchange_rates.to_currency = 'GBP' AND exchange_rates.ts <= transactions.ts )
        OR (transactions.currency = 'GBP')
    ) AS joined_transactions
WHERE seq = 1 GROUP BY user_id;
