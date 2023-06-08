# Contributing guidelines
_A brief read through these will get you ready to write some kick-ass code!_

## Variable naming conventions

| **Name**               | **Used format**        | **Example**           | **Notes**              |
|------------------------|------------------------|-----------------------|------------------------|
| local variables        | snake\_case            | `widget`              |                        |
| global variables       | \_snake\_case          | `_config_mgr`         | Leading underscore     |
| functions              | camelCase              | `storeOption`         |                        |
| function arguments     | snake_case             | `arg_a`               | Same as local variable |
| classes                | PascalCase             | `LibrusSession`       |                        |
| class member variables | snake\_case\_          | `hidden_idk_`         | Trailing underscore    |
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

## Typing

I know full well that Python is dynamically typed, but to ensure that static analyzers don't get messed up, please mark types in functions:
- Mark parameter types if they should be a specific type, else don't - e.g.  
  `param1 : int` if `param1` is always supposed to be an `int`  
  `data` if `data` can be of any type  
- Mark return type unless it can be any type:  
  `-> None` if your function does not return a value  
  `-> QWidget` if your function always returns a `QWidget`  
  and no return type annotation if your function can return any value.  
Marking variable types isn't necessary, but feel free to do so if you need to be restrictive.

## Pull requests

To ensure a smooth workflow, please remember to:
- Please mark your commits as drafts unless they are fully complete.
- Before marking your pull request as ready, please rebase the target branch to ensure that your code will compile after merging.
