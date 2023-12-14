<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update User, Account, and Transaction</title>
</head>
<body>
    <h2>Update User, Account, and Transaction</h2>
    <hr/>
    <form action="/update" method="post">
        <input type="hidden" name="id" value="{{str(item['UserID'])}}"/>
        <p>First Name: <input name="first_name" value="{{item['FirstName']}}" required/></p>
        <p>Last Name: <input name="last_name" value="{{item['LastName']}}" required/></p>
        <p>Date of Birth: <input name="date_of_birth" type="date" value="{{item['DateOfBirth']}}" required/></p>
        <p>Address: <input name="address" value="{{item['Address']}}" required/></p>
        <p>Contact Number: <input name="contact_number" value="{{item['ContactNumber']}}" required/></p>
        <p>Email: <input name="email" type="email" value="{{item['Email']}}" required/></p>
        
        <!-- Additional fields for account details -->
        <p>Account Type: <input name="account_type" value="{{item['AccountType']}}" required/></p>
        <p>Initial Balance: <input name="initial_balance" type="number" value="{{item['InitialBalance']}}" required/></p>
        
        <!-- Additional fields for transaction details -->
        <p>Transaction Type: <input name="transaction_type" value="{{item['TransactionType']}}" required/></p>
        <p>Amount: <input name="amount" type="number" value="{{item['Amount']}}" required/></p>
        <p>Transaction Date: <input name="transaction_date" type="date" value="{{item['TransactionDate']}}" required/></p>
        <p>Description: <input name="description" value="{{item['Description']}}" required/></p>

        <p><button type="submit">Submit</button></p>
    </form>
    <hr/>
    <a href="/">Back to List</a>
    <hr/>
</body>
</html>
