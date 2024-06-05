# rudderstack_profiles

## Entities

<table>
<thead>
<tr><th>Entity</th><th>ID Stitcher</th><th>ID Types</th></tr>
</thead>
<tbody>
<tr><td>user</td><td>models/user_id_stitcher</td><td>user_id, anonymous_id, email, shopify_customer_id</td></tr>
</tbody>
</table>

## ID Types

<table>
<thead>
<tr><th>ID Types</th><th>Filters</th></tr>
</thead>
<tbody>
<tr><td>user_id</td><td>None</td></tr>
<tr><td>anonymous_id</td><td>None</td></tr>
<tr><td>email</td><td><table>
<thead>
<tr><th>Type</th><th>Value</th><th>Regex</th></tr>
</thead>
<tbody>
<tr><td>include</td><td></td><td>.+@.+</td></tr>
</tbody>
</table></td></tr>
<tr><td>shopify_customer_id</td><td>None</td></tr>
</tbody>
</table>

## Inputs

<table>
<thead>
<tr><th>Input</th><th>Table</th><th>IDs</th></tr>
</thead>
<tbody>
<tr><td>marketing_site_identifies</td><td>emil_demo.marketing_website.identifies</td><td><table>
<thead>
<tr><th>Entity</th><th>Type</th><th>Select</th></tr>
</thead>
<tbody>
<tr><td>user</td><td>anonymous_id</td><td><code>anonymous_id</code></td></tr>
<tr><td>user</td><td>user_id</td><td><code>user_id</code></td></tr>
<tr><td>user</td><td>email</td><td><code>LOWER(email)</code></td></tr>
</tbody>
</table></td></tr>
<tr><td>marketing_site_pages</td><td>emil_demo.marketing_website.pages</td><td><table>
<thead>
<tr><th>Entity</th><th>Type</th><th>Select</th></tr>
</thead>
<tbody>
<tr><td>user</td><td>anonymous_id</td><td><code>anonymous_id</code></td></tr>
</tbody>
</table></td></tr>
<tr><td>shopify_orders</td><td>emil_demo.shopify_store.order_completed</td><td><table>
<thead>
<tr><th>Entity</th><th>Type</th><th>Select</th></tr>
</thead>
<tbody>
<tr><td>user</td><td>anonymous_id</td><td><code>anonymous_id</code></td></tr>
<tr><td>user</td><td>email</td><td><code>LOWER(email)</code></td></tr>
<tr><td>user</td><td>shopify_customer_id</td><td><code>shopify_customer_id</code></td></tr>
</tbody>
</table></td></tr>
</tbody>
</table>

## Models

<table>
<thead>
<tr><th>Model</th><th>Type</th><th>Entity</th></tr>
</thead>
<tbody>
<tr><td>user_id_stitcher</td><td>id_stitcher</td><td>user</td></tr>
<tr><td>user_profile</td><td>feature_table_model</td><td>user</td></tr>
</tbody>
</table>

## Var Groups

<table>
<thead>
<tr><th>Var Group</th><th>Entity</th></tr>
</thead>
<tbody>
<tr><td>default_vars</td><td>user</td></tr>
</tbody>
</table>

## Var Groups

<table>
<thead>
<tr><th>Entity Var</th><th>Select</th><th>From</th><th>Where</th></tr>
</thead>
<tbody>
<tr><td>first_name</td><td><code>FIRST_VALUE(first_name)</code></td><td>inputs/shopify_orders</td><td><code>first_name IS NOT NULL</code></td></tr>
<tr><td>last_name</td><td><code>FIRST_VALUE(last_name)</code></td><td>inputs/shopify_orders</td><td><code>last_name IS NOT NULL</code></td></tr>
<tr><td>first_seen</td><td><code>MIN(CAST(timestamp AS date))</code></td><td>inputs/marketing_site_pages</td><td></td></tr>
<tr><td>last_seen</td><td><code>MAX(CAST(timestamp AS date))</code></td><td>inputs/marketing_site_pages</td><td></td></tr>
<tr><td>user_lifespan</td><td><code>{{user.Var("last_seen")}} - {{user.Var("first_seen")}}</code></td><td></td><td></td></tr>
<tr><td>days_active</td><td><code>COUNT(DISTINCT CAST(timestamp AS date))</code></td><td>inputs/marketing_site_pages</td><td></td></tr>
<tr><td>revenue</td><td><code>SUM(order_amount)</code></td><td>inputs/shopify_orders</td><td></td></tr>
<tr><td>order_count</td><td><code>COUNT(order_number)</code></td><td>inputs/shopify_orders</td><td></td></tr>
</tbody>
</table>

