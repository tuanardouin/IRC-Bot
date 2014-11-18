Morphux-IRC-Bot
===============

An modulable IRC Bot !

## Installation
```sh
git clone https://github.com/Ne02ptzero/Morphux-IRC-Bot my/awesome/directory
```

## Usage
```sh
python main.py
```

## Create a Module

In this Bot, a module is a command, or a group of command.
Let's create an Pizza Module together !

### The module directory
```sh
mkdir modules/pizza
```
In this directory, you need:
```sh
$> ls
__init__.py
pizza.py
```

The \_\_init\_\_.py his here to load the module. That's an empty file. If it is not present, the module can't be load !

### Let's start the module code:
#### Base Code:
```python
class Pizza:
  def command(self):
    self.config = {}
    return self.config
```
The function command() is __REQUIRED__, and the return to !
### Let's create a base function:
```python
class Pizza:
  def command(self):
    self.config = {}
    return self.config
    
  def givePizza(self, Morphux, infos):
    if (len(infos['args'][0]) == 0):
      # If an argument missing
      Morphux.sendMessage("I eat the pizza :/", infos['nick'])
    elif (Morphux.userExists(infos['args'][0])):
      # If User is connected
      Morphux.sendMessage(infos['nick'] + " give you some pizza !", infos['args'][0])
    else:
      Morphux.sendMessage("Can't find user" + infos['args'][0] + " :(", infos['nick'])
```
Nice !
Let's analyze this:
```python
def givePizza(self, Morphux, infos):
```
A command function __ALWAYS__ have to be like this

##### Parameters:
Morphux is the base class for sending message, ban User, etc...

If you to know more about Morphux Class, see API section.

infos is a list of informations (No way ?) about the command

Basic infos for (!pizza Ne02tzero):
```python
  infos = {
    # The IRC full line
    "fullLine": "Ne02ptzero!~ne02ptzer@85-168-100-79.rev.numericable.fr PRIVMSG #ne02ptzero :!pizza Ne02ptzero",
    "command": "pizza",
    "args": ['Ne02ptzero'],
    "fullUser": "Ne02ptzero!~ne02ptzer@85-168-100-79.rev.numericable.fr"
    "nick": "Ne02ptzero"
  }
```

#### Module configuration:
Now, back to the self.config of the module

We have to tell to main Class "on !pizza call Pizza.givePizza", so:
```python
  def command(self):
    self.config = {
      "command": {
        "pizza": {
          "function": self.givePizza,
          "usage": "pizza <user>",
          "help": "Give a pizza to somebody !"
        }
      }
    }
```

well, our first module is now done :)
