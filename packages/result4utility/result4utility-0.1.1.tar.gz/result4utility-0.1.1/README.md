<p align="center">
  <a href="https://github.com/luigi-dv/result4utility"><img src="https://raw.githubusercontent.com/Luigi-DV/result4utility/master/assets/img/logo-green.png" alt="Result4Utility Logo"></a>
</p>
<p align="center">
    <em>Result4Utility, easy to use, fast to implement, ready for production</em>
</p>

The module contains interesting features for APIs endpoint creation. 
With some interesting decorators.

---

**Documentation**: <a href="https://github.com/luigi-dv/result4utility" target="_blank">https://github.com/luigi-dv/result4utility </a>

**Source Code**: <a href="https://github.com/luigi-dv/result4utility" target="_blank">https://github.com/luigi-dv/result4utility </a>

---

## Installation
```
pip install result4utility
```


## Examples

###  __Result__

A Structure for dynamics models to encapsulate values. 

When select an Error result type, the property HasErrors take true value.


__Use Case:__

```py
from result4utility.result import Result
from result4utility.result import ResultOperationType as resultType

# Initialize the Result Class
response = Result()

# Declare the model
model = {'User':'john.doe', 'Name':'John', 'Surname':'Doe'}

# Setting up the value of the response content with the model
response.content = model

# Adding results to our created response
response.add_result(message='Successfully Request', result_type=resultType.SUCCESS)
```

###  __Reader__

This class provides a dictionary reader functionality using attributes.

__Use Case:__

```py
from result4utility.dictionary import Reader

# Declare the dictionary to read
dictionary_test = {
    "primary_entry":"primary test data",
    "secondary_entry" : {
        "secondary_entry_1":"secondary test data 1",
        "secondary_entry_2":{
          "secondary_entry_2_1":"secondary test data 2.1",
        }        
    }
}

# Setting up the Reader Object
dictionary = Reader(config_file=dictionary_test)

# Read the values
test_1 = dictionary.primary_entry.get()
test_2 = dictionary.secondary_entry.secondary_entry_2.secondary_entry_2_1.get()

# Print the values
print(test_1)
print(test_2)
```

###  __Tools__

Two methods for dictionary operations.


#### __Convert from object to dictionary:__

```py
from result4utility.tools import Tools

class Test(object):
  index:int
  name:str
  def __init__(self, index_input:int, name_input:str):
    self.index=index_input
    self.name=name_input
      
# Define the object to test 
object_test:object = Test(1,'John')

# Initialize the Tool class
tool = Tools()

# Convert the Object to Dictionary
result:dict = tool.dictionary_from_object(model=object_test)

# Output
print ({'index':1, 'name':'John'})
```

> As you can see we are doing the object conversion over a new initialized object.
> Operations will not take actions over your main Objects.

#### __Remove properties of dictionary:__

```py
from result4utility.tools import Tools

class Test(object):
  index:int
  name2:str
  def __init__(self, index_input:int, name_input:str):
    self.index=index_input
    self.name=name_input
  
# Initialize the Tool class
tool = Tools()

# Create new Test Class Object 
object_test:object = Test(1,'John')

# Convert the Object to Dictionary
dictionary_test:dict = tool.dictionary_from_object(model=Test)

# Remove the dictionary property
result:dict = tool.remove_property(target=dictionary_test, props=['index'])

# Output
print({'name':'John'})
```
