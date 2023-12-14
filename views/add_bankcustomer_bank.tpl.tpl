<html>
<body>
<h2>Add New User and Account</h2>
<hr/>
<form action="/add" method="post">
  <p>First Name: <input name="first_name" required/></p>
  <p>Last Name: <input name="last_name" required/></p>
  <p>Date of Birth: <input name="date_of_birth" type="date" required/></p>
  <p>Address: <input name="address" required/></p>
  <p>Contact Number: <input name="contact_number" required/></p>
  <p>Email: <input name="email" type="email" required/></p>
  <hr/>
  <h3>Add New Account</h3>
  <p>Account Type: <input name="account_type" required/></p>
  <p>Initial Balance: <input name="initial_balance" type="number" required/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/">Back to List</a>
<hr/>
</body>
</html>
