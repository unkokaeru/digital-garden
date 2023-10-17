```area_circle.m
function area=area_circle(d)

% Calculates the area of a circle given the radius :)

area=pi*(d/2).^2;

end
```

```MATLAB
>> edit area_circle
>> area_circle(4)

ans =

   50.2655

>> area_circle(2)

ans =

   12.5664

>> area_circle(3)

ans =

   28.2743

>> area_circle(1)

ans =

    3.1416

>> help area_circle
  Calculates the area of a circle given the radius :)

>> radii=[3,4,5]; area_circle(radii)
Error using  ^ 
Incorrect dimensions for raising a matrix to a power. Check that the matrix is square and the power is
a scalar. To operate on each element of the matrix individually, use POWER (.^) for elementwise power.

Error in area_circle (line 3)
    area=pi*R^2;
 
>> radii=[3,4,5]; area_circle(radii)

ans =

   28.2743   50.2655   78.5398

>> radii=[3,4,5]; area_circle(radii)

ans =

    7.0686   12.5664   19.6350

>> 
```