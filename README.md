# 0x00. AirBnB clone - The console

![](https://camo.githubusercontent.com/3bdeeec19003ed9c1042b6227bdd27f5f52f8d14bd5187d25953a4600bc446f6/68747470733a2f2f63646e2d776562736974652e70617274656368706172746e6572732e636f6d2f6d656469612f696d616765732f486f6c626572746f6e5f5363686f6f6c5f4c6f676f2e6f726967696e616c2e706e67)

![](https://user-images.githubusercontent.com/98335124/177196137-35b5a657-1f9d-45b3-8e96-45a0fd659660.png)

### Background Context
#### Welcome to the AirBnB clone project!
<<<<<<< HEAD
#tHIS IS MY README FILE
=======

This project is the first part ongoing Airbnb Clone.

In this project we are building the backend of the Airbnb. We created a Command Line Interpreter (CLI). This is similiar the the Shell project in C, but with Python's high level `cmd` framwork makes this as simple as importing `cmd` and beginning each function with `do_*`.

The command intepreter is written in the console.py file. It has several methods which allow us to manage the objects of the project:

- Create a new object (ex: a new User or * a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
-  Update attributes of an object
-  Destroy an object

The CLI is linked to several other classes:

- BaseModel, User, FileStorage, amenity, City, State, Place, Review

`BaseModel` is the parent class. It takes care of initiliazing, serializing and deserializing each instance.

The flow of the serialization and deserialization is: `instantce <-> Dictionary <-> JSON string <-> file`

In file_storage.py we created a storage engine for the project. The methods for creating a new instance, saving and reloading it are in the `FileStorage` class.

The following is a tree diagram of this projects folders and files:

**:file_folder:models**

┣ :file_folder:engine

 ┃  ┗ file_storage.py

 ┣ amenity.py

 ┣ base_model.py

 ┣ city.py

 ┣ place.py

 ┣ review.py

 ┣ state.py

 ┗ user.py

The Unit Tests are:

**:file_folder:tests**

┣ :file_folder:test_models

┃ ┣ :file_folder:test_engine

┃ ┃  ┗test_file_storage.py

┃ ┣ test_amenity.py

┃ ┣ test_base_model.py

┃ ┣ test_city.py

┃ ┣ test_place.py

┃ ┣ test_review.py

┃ ┣ test_state.py

┃ ┗ test_user.py

## Use

Run the console:

![](https://i.ibb.co/BzGxVw2/1.png)

This is the start of the console:

`(hbnb)`

Type `help` for a list of commands:

![](https://i.ibb.co/bH5Fy9G/2.png)

Typing help followed by a command returns a useful text that describes the command, for example:

![](https://i.ibb.co/8DpYzx3/3.png)

To create a new instance of a class, type `create` followed by a class name:

![](https://i.ibb.co/cwDYsCS/4.png)

This returns a unique id from the `UUID` import class. This is a unique number that is tagged to an instance. The `show` command displays a string representation of an instance based on it's class name and user id:

![](https://i.ibb.co/W0ZQfXq/5.png)

The `create` commands saves a dictionary representation of the instance, which includes:

- Class name
- Unique ID number
- Created at (date/time)
- Updated at (date/time)

The `update` command allows users to add additional attributes to the dictionary representation:

![](https://i.ibb.co/M6Tbmzw/6.png)

Using `show`again, we see that the `JSON` file now reads:

![](https://i.ibb.co/2dht4M5/7.png)

Further, the `destroy` method deletes the instance, so when we run it:

![](https://i.ibb.co/p2h7y67/8.png)

And try to `show` it again, we get this message:

"no instance found "

![](https://i.ibb.co/j61h8sn/9.png)

The instance has been deleted.

The `all` command prints a string representation of all instances, regardless of it's class.

Finally, the `show`, `all`, `update` and `destroy` commands can also be called with the following syntax:

`(hbnb) <class name>.command()`

For example, `User.all()` is equivelent to the `all`command.

Commands that require an `id` can be called like this:

![](https://i.ibb.co/mhhShBZ/10.png)





### Authors

##### [Pablo Agudelo](https://github.com/Mr-emilio/ "Pablo  Agudelo") 

##### [Raul  Quintero](https://github.com/raquintero1974/ "Raul Quintero") 

##### [Eduardo Zúñiga](https://github.com/edwardzuniga/ "Eduardo Zúñiga") 


# -holbertonschool-AirBnB_clone
>>>>>>> 1d27c56a4ac254dd90786ef2884c237575c39a6e
