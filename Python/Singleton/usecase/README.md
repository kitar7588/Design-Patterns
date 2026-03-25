# The Challenge: Shared Database Connection
Imagine you are building a system where multiple parts of the application need to access a database. 
If every part of the code creates its own connection, the system will quickly run out of resources.

## Your Task:
Create a class named DatabaseConnector. This class must:

### 1.Ensure Singularity: 
No matter how many times you try to instantiate the class, it should always return the exact same object instance.

### 2.Maintain State: 
Add an attribute called connection_id. Initialize it with a random number (or a timestamp) the first time the class is created.

### 3.Verification: 
Create two variables, db1 and db2, by calling DatabaseConnector(). Prove they are the same instance and that they share the same connection_id.