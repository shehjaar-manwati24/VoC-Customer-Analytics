Smart Payment Routing Optimizer

## Project Overview
This project simulates a payment gateway environment to optimize transaction success rates. By analyzing historical performance patterns between different Card Networks (Visa, Mastercard, Amex) and Gateways (HDFC, ICICI, Razorpay), the system recommends the optimal route for each transaction.

## Business Impact
* **Improved Success Rates:** Dynamically routes transactions to the gateway with the highest historical probability of success.
* **Data-Driven Insights:** Identifies specific 'sweet spots' (e.g., HDFC performing better for Visa) to negotiate better SLAs with providers.

## How to Run
1. Run \`python generate_data.py\` to create a synthetic dataset of 5,000 transactions.
2. Run \`python optimizer.py\` to generate the routing recommendation table.

## Tech Stack
* **Python**: Core logic
* **Pandas**: Data manipulation and success rate calculation
