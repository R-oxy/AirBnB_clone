# AirBnB Clone - The Console

Welcome to the AirBnB clone project!

## Getting Started

### What's a Command Interpreter?

The command interpreter is similar to the Shell, but it's limited to a specific use-case. In our case, we use it to manage objects of our project:

- Create new objects (e.g., User or Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy objects

## Learning Objectives

By working on this project, you'll learn:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Execution

Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```

But also in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

All tests should also pass in non-interactive mode:

```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Usage Examples

### Launching the Console

```bash
$ ./console.py
(hbnb)
```

### Creating a New Object

```bash
(hbnb) create
** class name missing **
(hbnb) create User
670265eb-5982-489e-8b92-2dff054f0776
```

### Showing an Object

```bash
(hbnb) show User
** instance id missing **
(hbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}
```

### Updating an Object

```bash
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161)}"]
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "20"
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'Age': 20, 'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 13, 9, 937933)}"]
```

### Destroying an Object

```bash
(hbnb) destroy User 670265eb-5982-489e-8b92-2dff054f0776
(hbnb)

## Authors
<details>
    <summary>Aron Mang'ati</summary>
    <ul>
    <li><a href="mailto:aronmangati@gmail.com">e-mail</a></li>
    </ul>
</details>
<details>
    <summary>Benalla Aiman</summary>
    <ul>
    <li><a href="mailto:benallaaiman@gmail.com">e-mail</a></li>
    </ul>
</details>

