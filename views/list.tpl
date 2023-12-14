<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users, Accounts, and Transactions</title>
</head>
<body>
    <h2>Users, Accounts, and Transactions</h2>
    <table border="1">
        <tr>
            <th>User ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Date of Birth</th>
            <th>Address</th>
            <th>Contact Number</th>
            <th>Email</th>
            <th>Account Type</th>
            <th>Initial Balance</th>
            <th>Transaction Type</th>
            <th>Amount</th>
            <th>Transaction Date</th>
            <th>Description</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in data:
            <tr>
                <td>{{item['UserID']}}</td>
                <td>{{item['FirstName']}}</td>
                <td>{{item['LastName']}}</td>
                <td>{{item['DateOfBirth']}}</td>
                <td>{{item['Address']}}</td>
                <td>{{item['ContactNumber']}}</td>
                <td>{{item['Email']}}</td>
                <td>{{item['AccountType']}}</td>
                <td>{{item['InitialBalance']}}</td>
                <td>{{item['TransactionType']}}</td>
                <td>{{item['Amount']}}</td>
                <td>{{item['TransactionDate']}}</td>
                <td>{{item['Description']}}</td>
                <td><a href="/update/{{item['UserID']}}">Update</a></td>
                <td><a href="/delete/{{item['UserID']}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/add">Add a new user, account, and transaction</a>
</body>
</html>
