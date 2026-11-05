from pathlib import Path
import csv
from decimal import Decimal
root=Path(__file__).resolve().parents[1]
def rows(name):
    with (root/'data'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
t=rows('retail_transactions.csv');f=rows('fact_sales.csv');customer=rows('dim_customers.csv');product=rows('dim_products.csv');dates=rows('dim_dates.csv')
assert len(t)==len(f)==19380, 'Row count failed'
assert len({r['line_id'] for r in t})==19380, 'Duplicate line IDs'
assert len({r['order_id'] for r in t})==12400, 'Wrong order count'
assert len({r['customer_id'] for r in customer})==len(customer)
assert len({r['product_id'] for r in product})==len(product)
assert len({r['date'] for r in dates})==len(dates)
assert {r['customer_id'] for r in t}<={r['customer_id'] for r in customer}
assert {r['product_id'] for r in t}<={r['product_id'] for r in product}
assert {r['order_date'] for r in t}<={r['date'] for r in dates}
for r in t:
    assert int(r['quantity'])>0
    assert Decimal('0')<=Decimal(r['discount'])<=Decimal('.20')
    assert abs(Decimal(r['sales'])-Decimal(r['cost'])-Decimal(r['profit']))<Decimal('.01')
print('PASS — 10 data checks; 19,380 lines / 12,400 orders')
