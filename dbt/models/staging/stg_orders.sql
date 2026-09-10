with source_orders as (
    select * from {{ ref('raw_orders') }}
),
cleaned as (
    select
        order_id::integer as order_id,
        customer_id::varchar as customer_id,
        order_date::date as order_date,
        lower(trim(status)) as order_status,
        order_amount::decimal(12, 2) as order_amount
    from source_orders
)
select * from cleaned