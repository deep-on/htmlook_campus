-- Apex MRR by tier — month-over-month, weighted by ACV
-- Source: warehouse.subscriptions (last_synced 2026-04-29)

SELECT
  date_trunc('month', billing_period)                          AS month,
  tier,
  SUM(monthly_recurring_revenue * annual_contract_value)
    / NULLIF(SUM(annual_contract_value), 0)                    AS mrr_weighted_by_acv
FROM warehouse.subscriptions
WHERE billing_period >= '2026-01-01'
  AND status = 'active'
GROUP BY 1, 2
ORDER BY 1, 2;
