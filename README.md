# FinCorp: Personal Financial Accounting and Tracking System

This project aims to create a comprehensive financial accounting and tracking system for personal use. It provides an easy way to log transactions, track credit card and bill payments, generate financial projections, and monitor net worth and financial assets.

## Project Description

The personal financial accounting and tracking system has the following features:

1. Log transactions with just a few simple clicks.
2. Track credit card and bill payments to ensure timely payments and avoid penalties.
3. Generate projections of financial well-being and account balances after bill payments (e.g., account balance in 10 days, 20 days, or 30 days).
4. Monitor financial assets and net worth for better financial planning and decision-making.

## Setting Up the Project

To set up this project from scratch, follow the steps below:

### Prerequisites

- Python (3.7 or later)
- Ngrok

### Step-by-Step Guide (for Windows)

1. Clone the GitHub repository or download the source code.
2. Create a virtual environment for the project:
python -m venv venv

3. Activate the virtual environment:

venv\Scripts\activate

4. Install the required Python libraries:
pip install -r requirements.txt

5. Apply the migrations to set up the database:
python manage.py migrate

6. Run the Django development server:
python manage.py runserver

7. Download and install [Ngrok](https://ngrok.com/download).
8. Run Ngrok to expose your local server to the internet:
ngrok http 8000

Note the generated URL from the Ngrok output. You can use this URL to access your project from the internet.

## Potential Use Cases

This personal financial accounting and tracking system can be used in various scenarios, including:

1. Budgeting and expense tracking: Log daily transactions and expenses to track spending habits and make informed decisions about personal finances.
2. Debt management: Track credit card payments and other bill payments to avoid missed due dates, late fees, and other penalties.
3. Financial planning and forecasting: Generate projections of account balances and financial well-being to plan for future expenses and investments.
4. Net worth tracking: Monitor assets and net worth over time to make strategic decisions about wealth management and financial growth.