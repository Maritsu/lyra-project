# Contributing guidelines
_A brief read through these will get you ready to write some kick-ass code!_

## Variable naming conventions

| **Name**               | **Used format**        | **Example**           | **Notes**              |
|------------------------|------------------------|-----------------------|------------------------|
| local variables        | snake\_case            | `widget`              |                        |
| global variables       | \_snake\_case          | `_config_mgr`       | Leading underscore     |
| functions              | camelCase              | `storeOption`         |                        |
| function arguments     | snake_case             | `arg_a`               | Same as local variable |
| classes                | PascalCase             | `LibrusSession`       |                        |
| class member variables | snake\_case\_          | `hidden_idk_`       | Trailing underscore    |
| class member functions | camelCase              | `checkIfStudent`      |                        |
| constants              | SCREAMING\_SNAKE\_CASE | `SPANISH_INQUISITION` |                        |

here's ~~tree~~ table

## Commit names

Commit names should follow the format:
```
[scope] brief description

optional extra info
```  

The scope of the commit is the section of the codebase that is being changed, e.g. `[res]`, `[ui]`, `[config]`, etc.  
The description should be one sentence describing what the commit introduces, and should not begin with a capital letter unless it references a variable named as such.  
You can add extra information that might be useful to anyone reading, such as a warning, or even just a TODO.
