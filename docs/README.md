# Project description
The project is a set of functions for calculating the perimeter and area of shapes.<br> 
At this stage, functions for a Circle, Square and Rectangle are implemented.

# Functions
- area(N) - calculate the area of geometric objects.
- perimeter(N) - calculate the perimeter of geometric objects.
## Math formulas
- ### Area
  - Circle: S = πR²
  - Rectangle: S = ab
  - Square: S = a²

- ### Perimeter
  - Circle: P = 2πR
  - Rectangle: P = 2a + 2b
  - Square: P = 4a

## Now available geometric objects
- ### Circle
> ***Area*** function requires radius in parameters.<br>
```python
import math

def area(r):
    return math.pi * r * r
```
> ***Perimeter*** function requires radius in parameters.
```python
import math

def perimeter(r):
    return 2 * math.pi * r
```
- ### Rectangle
> ***Area*** function requires size of two sides in parameters.<br>
```python
def area(a,b):
    return a * b
```
> ***Perimeter*** function requires size of two sides in parameters.
```python
def perimeter(a,b):
    return a + b
```
-  ### Square
> ***Area*** function requires size of any side in parameters.
```python
def area(a):
    return a * a
```
> ***Perimeter*** function requires size of any side in parameters.
```python
def perimeter(a):
    return a * 4
```


# Updates
- [ci/cd tests created](https://github.com/Perlysha/lab2/commit/2166ebe9d83b6b86693b1d301fac24f8d280e6e8)<br>
>Hash: 2166ebe9d83b6b86693b1d301fac24f8d280e6e8
- [Unittests created](https://github.com/Perlysha/lab2/commit/b45aeb86bab058c35eb6d72fb7b5f10681a5644d) <br>
>Hash: b45aeb86bab058c35eb6d72fb7b5f10681a5644d
- [README.md file Update](https://github.com/Perlysha/lab2/commit/c3806cdc0f099c5014efe86cf1c0fb4e4c311dbf) <br>
>Hash: c3806cdc0f099c5014efe86cf1c0fb4e4c311dbf <br>
- [Rectangle functions added to Rectangle.py](https://github.com/Perlysha/lab2/commit/0cd6abd734c748068138462c3b9c1d617ee4c134) <br>
>Hash: 0cd6abd734c748068138462c3b9c1d617ee4c134 <br>

