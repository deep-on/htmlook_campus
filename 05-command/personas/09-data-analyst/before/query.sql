-- Apex MRR by tier — month-over-month
-- Source: warehouse.subscriptions (last_synced 2026-04-29)

SELECT
  date_trunc('month', billing_period) AS month,
  SUM(monthly_recurring_revenue)      AS mrr_total
FROM warehouse.subscriptions
WHERE billing_period >= '2026-01-01'
  AND status = 'active'
GROUP BY 1
ORDER BY 1;
