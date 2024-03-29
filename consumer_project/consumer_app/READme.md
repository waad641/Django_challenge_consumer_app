# Consumer App Documentation :

The Consumer App serves as the front-end interface for users to interact with the banking system. It communicates with the Producer App to submit and retrieve bank transactions. Below is an overview of the key components:

# 1.Views and Forms:

   - The `transaction_list` view renders a list of bank transactions retrieved from the Producer App.

   - The `submit_transaction` view provides a form for users to submit new transactions to the Producer App.

# 2.Transaction Submission:

   - The HTML form in `submit_transaction.html` captures user inputs for account number and transaction amount.

   - Upon submission, the data is sent to the Producer App's `submit_transaction` API endpoint using a POST request.

# 3.Communication with Producer App:

   - The `requests` library is used to make HTTP requests to the Producer App's API endpoints.

   - The `submit_transaction` view sends a POST request to the Producer App to submit a new bank transaction.

   - The `transaction_list` view sends a GET request to retrieve a list of transactions from the Producer App.


# 4.Asynchronous Processing:

   - The `process_bank_transaction` Celery task asynchronously processes bank transactions.

   - It updates the processed data in the local `BankTransaction` model and sends the result to the Producer App's webhook endpoint.

# 5.Webhook Integration:

   - Processed data is sent back to the Producer App's `webhook_receiver` endpoint using a POST request.

   - The `webhook_receiver` view in the Producer App updates the corresponding transaction with the processed data.

# 6.User Interface:

   - The user interface is designed with the `bank_transaction_list.html` form for transaction submission.

   - The `transaction_list` view displays a list of transactions in a user-friendly format.

# Note to the Reader:

This Consumer App is a component of considered to be  a larger banking system that includes the Producer App. It provides a simple and intuitive interface for users to submit and view bank transactions. The communication with the Producer App is essential for processing and updating transaction data asynchronously. The integration of Celery tasks and webhooks enhances the efficiency of data processing and ensures a seamless user experience.
