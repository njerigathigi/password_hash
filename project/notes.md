`Password Hashing with Bcrypt`

Authentication - making sure a user is who they say they are. The process of logging in is a prime example of authentication. In order to successfully log in, we need to make sure a user is who they say they are (by providing a correct username and password).

Authorization - making sure a user is allowed to access a route / resource. On Facebook, you are not "authorized" to delete other people's posts. On Github, you are not authorized to push to other people's repositories unless they "authorize" you.

`key parts of authentication`

Signing up - make sure a user provides a unique identifier (username / email) and a password. Store that information in the database for when a user logs in

Logging In - first make sure that the user has provided a unique identifier (username / email) that exists. If that identifier exists, check to see if their password provided is the same one as in the database. If it is, log them in!

This seems simple, but there is a highly dangerous security risk that we must always consider. When we accept the username and password, they come to the server as plain text, which means that if we were to store that information directly we would be storing our password in plain text.

 NEVER STORE PASSWORDS IN PLAIN TEXT.

 What we need to do is hash a password before saving it to the database. You'll sometimes see hashing referred to as one-way encryption. This means that our goal isn't to ever decrypt the password: instead, we just want to make it difficult for someone to obtain a user's password even if they gain access to the database.

 But if we don't know the user's password, how can we log them in? The trick is that when someone attempts to log in, we'll hash the password they type, and compare that hashed password to the value in the database. But we never decrypt anything.

 Another type of encryption, which we won't be using, is two-way encryption. With two-way encryption, both parties know a secret key that they can use to decipher messages.

 `Hashing Passwords with bcrypt`

While bcrypt doesn't come natively in Flask, there is a bcrypt module designed for integration with Flask, called flask_bcrypt.

```python
#in python/ipython shell

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

pw_hash = bcrypt.password_to_check("secret")
bcrypt.check_password_hash(pw_hash, "secret") #True
bcrypt.check_password_hash(pw_hash, "secret2") #False
pw_hash #long incomprehensible byte literal
```
`Structure of the Hashed Password`

If you look at a password that's been hashed using bcrypt, it should look like a bunch of characters jumbled together. However, there is a structure in this hashed password.

```python
b'$2b$12$3cy0jD1AfgcT0ipGL1UhquBZXvAxUwRrdG90Gi951AcxIXm2F2gMK'
```
The `hashed password` is actually just the last 31 characters of the byte literal (BZXvAxUwRrdG90Gi951AcxIXm2F2gMK).

The `prefix` simply indicates that bcrypt was used to encrypt the password, as opposed to some other encryption algorithm. In this case the prefix is 2b, but for bcrypt you might also see 2a or 2y as the prefix.

`Work Factor` - this measures how long it takes to perform the encryption. One benefit to using a good hashing algorithm is that it can prevent brute force attacks, whereby an attacker simply tries thousands or even millions of passwords in quick succession. The more time it takes to hash the passwords and perform the check, the less effective a brute force attack becomes. However, there's also a tradeoff here: the higher the work factor, the better the hashing, but the worse the user experience. Imagine if it took several minutes to log in to a website because of the time spent hashing the password that the user typed in!

you can think of the `salt` as a randomly generated string that's used to provide a degree of randomness into the hashing process. The salt is combined with the original password to generate the hash. The salt is stored along with the hash because if you want to check that the user has provided the right password when they attempt to log in, you need to know what salt was originally used to hash the encrypted password that's stored in the database.
```python
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
hash1 = bcrypt.generate_password_hash("secret")
hash2 = bcrypt.generate_password_hash("secret") 
hash1 == hash2 #False, check out the hashes. They have different values.
hash3 = generate_password_hash("secret", 17) # the 2nd argument lets us increase/decrease the work factor, default value is 12.
```
