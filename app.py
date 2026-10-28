
from flask import Flask, render_template_string

app = Flask(__name__)

sales_data = [
    {"product": "Laptop", "quantity": 5, "sales": 250000},
    {"product": "Mobile", "quantity": 10, "sales": 150000},
    {"product": "Headphones", "quantity": 20, "sales": 40000},
    {"product": "Keyboard", "quantity": 15, "sales": 30000}
]

@app.route("/")
def home():
    total_sales = sum(item["sales"] for item in sales_data)
    total_quantity = sum(item["quantity"] for item in sales_data)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sales Analytics Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f5f9;
                padding: 30px;
            }
            h1 { color: #17365d; }
            .card {
                background: white;
                padding: 20px;
                margin: 12px 0;
                border-radius: 10px;
            }
            table {
                background: white;
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 12px;
                border: 1px solid #ddd;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Sales Forecasting and Business Analytics</h1>

        <div class="card">
            <h2>Total Sales: ₹{{ total_sales }}</h2>
            <h3>Total Quantity Sold: {{ total_quantity }}</h3>
        </div>

        <h2>Product Sales Details</h2>
        <table>
            <tr>
                <th>Product</th>
                <th>Quantity</th>
                <th>Sales (₹)</th>
            </tr>
            {% for item in sales_data %}
            <tr>
                <td>{{ item.product }}</td>
                <td>{{ item.quantity }}</td>
                <td>{{ item.sales }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """, sales_data=sales_data,
         total_sales=total_sales,
         total_quantity=total_quantity)
