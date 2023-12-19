# Summary of MATLAB Onramp

## Basic Syntax

|Example|Description|
|---|---|
|[`x = pi`](https://www.mathworks.com/help/matlab/matlab_env/create-and-edit-variables.html)|Create variables and assign values with the equal sign (`=`).  <br>The left side (`x`) is the variable name, and the right side (`pi`) is its value.|
|[`y = sin(-5)`](https://www.mathworks.com/help/matlab/learn_matlab/calling-functions.html)|Provide inputs to a function using parentheses.|

## Desktop Management

|Function|Example|Description|
|---|---|---|
|[`save`](https://www.mathworks.com/help/matlab/ref/save.html)|`save data.mat`|Save your current workspace to a MAT-file.|
|[`load`](https://www.mathworks.com/help/matlab/ref/load.html)|`load data.mat`|Load the variables in a MAT-file to the workspace.|
|[`clear`](https://www.mathworks.com/help/matlab/ref/clear.html)|`clear`|Clear all variables from the workspace.|
|[`clc`](https://www.mathworks.com/help/matlab/ref/clc.html)|`clc`|Clear all text from the Command Window.|
|[`format`](https://www.mathworks.com/help/matlab/ref/format.html)|`format long`|Change how numeric output appears in the Command Window.|

## Array Types

|Example|Description|
|---|---|
|`4`|scalar|
|`[3 5]`|row vector|
|`[1;3]`|column vector|
|`[3 4 5; 6 7 8]`|matrix|

## Evenly Spaced Vectors

|Example|Description|
|---|---|
|`1:4`|Create a vector from `1` to `4`, spaced by `1`, using the [colon operator (`:`)](https://www.mathworks.com/help/matlab/ref/colon.html).|
|`1:0.5:4`|Create a vector from `1` to `4`, spaced by `0.5`.|
|`[linspace](https://www.mathworks.com/help/matlab/ref/linspace.html)(1,10,5)`|Create a vector with `5` elements. The values are evenly spaced from `1` to `10`.|

## Matrix Creation

|Example|Description|
|---|---|
|`[rand](https://www.mathworks.com/help/matlab/ref/rand.html)(2)`|Create a square matrix with `2` rows and `2` columns.|
|`[zeros](https://www.mathworks.com/help/matlab/ref/zeros.html)(2,3)`|Create a rectangular matrix with `2` rows and `3` columns of `0`s.|
|`[ones](https://www.mathworks.com/help/matlab/ref/ones.html)(2,3)`|Create a rectangular matrix with `2` rows and `3` columns of `1`s.|

## Array Indexing

|Example|Description|
|---|---|
|`A([end](https://www.mathworks.com/help/matlab/ref/end.html),2)`|Access the element in the second column of the last row.|
|`A(2,:)`|Access the entire second row.|
|`A(1:3,:)`|Access all columns of the first three rows.|
|`A(2) = 11`|Change the value of the second element of an array to `11`.|

## Array Operations

|Example|Description|
|---|---|
|[1 2; 3 4] + 1<br>ans =<br>     2     3<br>     4     5|Perform [array addition](https://www.mathworks.com/help/matlab/ref/plus.html).|
|[1 1; 1 1]*[2 2; 2 2]<br>ans =<br>     4     4<br>     4     4|Perform [matrix multiplication](https://www.mathworks.com/help/matlab/matlab_prog/array-vs-matrix-operations.html#btyv9yp-4).|
|[1 1; 1 1].*[2 2; 2 2]<br>ans =<br>     2     2<br>     2     2|Perform [element-wise multiplication](https://www.mathworks.com/help/matlab/matlab_prog/array-vs-matrix-operations.html#bu90xxy-1).|

## Multiple Outputs

|Example|Description|
|---|---|
|`[xrow,xcol] = [size](https://www.mathworks.com/help/matlab/ref/size.html)(x)`|Save the number of rows and columns in `x` to two different variables.|
|`[xMax,idx] = [max](https://www.mathworks.com/help/matlab/ref/max.html)(x)`|Calculate the maximum value of `x` and its corresponding index value.|

## Documentation

|Example|Description|
|---|---|
|`[doc](https://www.mathworks.com/help/matlab/ref/doc.html) randi`|Open the documentation page for the `randi` function.|

## Plots

|Example|Description|
|---|---|
|`[plot](https://www.mathworks.com/help/matlab/ref/plot.html)(x,y,"ro--","LineWidth",5)`|Plot a red (`r`) dashed (`--`) line with a  <br>circle (`o`) marker, with a heavy line width.|
|`[hold](https://www.mathworks.com/help/matlab/ref/hold.html) on`|Add the next line to the existing plot.|
|`hold off`|Create new axes for the next plotted line.|
|`[title](https://www.mathworks.com/help/matlab/ref/title.html)("My Title")`|Add a title to a plot.|
|`[xlabel](https://www.mathworks.com/help/matlab/ref/xlabel.html)("x")`  <br>`[ylabel](https://www.mathworks.com/help/matlab/ref/ylabel.html)("y")`|Add labels to axes.|
|`[legend](https://www.mathworks.com/help/matlab/ref/legend.html)("a","b","c")`|Add a legend to a plot.|

## Tables

|Example|Description|
|---|---|
|`[data.HeightYards](https://www.mathworks.com/help/matlab/matlab_prog/access-data-in-a-table.html)`|Extract the variable `HeightYards` from the table `data`.|
|data.HeightMeters = data.HeightYards*0.9144|Derive a table variable from existing data.|

## Logical Indexing

|Example|Description|
|---|---|
|`[[5 10 15] > 12](https://www.mathworks.com/help/matlab/matlab_prog/array-comparison-with-relational-operators.html)`|Compare the elements of a vector to the value `12`.|
|`[v1(v1 > 6)](https://www.mathworks.com/help/matlab/matlab_prog/find-array-elements-that-meet-a-condition.html)`|Extract all elements of `v1` that are greater than `6`.|
|`x(x==999) = 1`|Replace all values in `x` that are equal to `999` with the value `1`.|

## Programming

|Example|Description|
|---|---|
|[if](https://www.mathworks.com/help/matlab/ref/if.html) x > 0.5<br>    y = 3<br>else<br>    y = 4<br>end|If `x` is greater than `0.5`, set `y` to `3`.  <br>  <br>Otherwise, set `y` to `4`.|
|[for](https://www.mathworks.com/help/matlab/ref/for.html) c = 1:3<br>    disp(c)<br>end|The loop counter (`c`) progresses through the  <br>values `1:3` (`1`, `2`, and `3`).  <br>  <br>The loop body displays each value of `c`.|