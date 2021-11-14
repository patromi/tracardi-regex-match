# E-mail via SMTP

The purpose of this plugin is to display particular groups of regexes that we specify in a pattern.

# Configuration

This node requires configuration.

## Example of configuration

```json
    {"pattern": "(\b[A-Z]+\b).+(\b\d+)",
    "text":  "The price of PINEAPPLE ice cream is 20",
    "groups_name": ["group A", "group B"]}
```
OUTPUT:
value={'group A': 'PINEAPPLE', 'group B': '20'}

## Configuration description

* pattern: None, - Provide regex pattern.
* text: None, - Enter your text. You can use DotNotation.
* groups_name: None,- Enter the names of the output groups

##Examples of errors
- The number of groups in regex must be the same as in groups_name
This means that the number of groups given in the formula is not equal to the number of named groups


- regex couldn't find anything matching the pattern from supplied string.
This means that the pattern you specified is incorrect, because the plugin cannot find any text

# Input payload

This node does not process input payload.

# Output

This node returns dictionary containing data on groups
