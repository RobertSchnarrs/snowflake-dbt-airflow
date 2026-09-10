select
    order_date,
    count(*) as total_orders,
    count_if(order_status = 'completed') as completed_orders,
    sum(case when order_status = 'completed' then order_amount else 0 end)
        as completed_revenue
from {{ ref('stg_orders') }}
group by order_date