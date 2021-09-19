# Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

### Example 1:

Input: num = "123", target = 6,
Output: ["1*2*3","1+2+3"]
### Example 2:

Input: num = "232", target = 8,
Output: ["2*3+2","2+3*2"]

### Example 3:

Input: num = "105", target = 5,
Output: ["1*0+5","10-5"]
### Example 4:

Input: num = "00", target = 0,
Output: ["0*0","0+0","0-0"]
### Example 5:

Input: num = "3456237490", target = 9191,
Output: []
 

## Constraints:

1 <= num.length <= 10; 
num consists of only digits; 
-231 <= target <= 231 - 1

## Strategy
Use dfs to explor all possible combonations of digits and oprators
1. design dfs function:
- arguments: current processd number of digits, current string expression, current value, last equivelent added value
- if number of digits is length of num, it is a final value, otherwise it is a intermidiate value
- if final value is target, add the expresion to result
- if intermediate value, add next digit to the expression with one of the 3 operators
  - if there is no operand yet, add first operand without operator
  - otherwise:
    - for '+', the new digit is the last equivelent added value
    - for '-', the negative new digit is the last equivelent added value
    - for '*', we need to reverse one step to get the new value and new last equivelent added value (see code for detail)
2. start dfs on:
 - 0 used charactors
 - empty string as current expression
 - 0 as current value
 - None as last added value
3. return the result list

## Time complexty:
O(n**4)
