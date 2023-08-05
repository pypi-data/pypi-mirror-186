# MATRIX [Github]("https://github.com/Chandram-Dutta/matrix") || [PyPi]("https://pypi.org/project/matrix-chandramdutta/")

## The Python Library for managing your matrix (◕‿↼)
---
# Use the package in your project

### Install the package
```
pip install matrix_chandramdutta
```
### Using the package
```
import matrix_chandramdutta.matrix as matrix

matrix = get_matrix_input(3,5)
```

# Methods

### Getting a Matrix from User Input

`get_matrix_input(rows: int, columns: int) -> list`

This method takes in the number of rows and columns and returns a matrix of the given size. It also prompts the user for output

---

### Getting a Zero Matrix

`get_matrix_zero(rows: int, columns: int) -> list`

This method takes in the number of rows and columns and returns a matrix of the given size. It also fills the matrix with zeros for your further operations

---

`add_two_matrix(matrix_one: list, matrix_two: list) -> list`

This method takes in two matrices and returns the sum of the two matrices.

> **Warning**
> The matrices must be of the same size or else unexpected results may occur.

---

`subtract_two_matrix(matrix_one: list, matrix_two: list) -> list`

This method takes in two matrices and returns the difference of the two matrices.

> **Warning**
> The matrices must be of the same size or else unexpected results may occur.

---

`multiply_two_matrix(matrix_one: list, matrix_two: list) -> list`

This method takes in two matrices and returns the product of the two matrices.

> **Warning**
> The matrices must satisfy the matrix multiplication rule or else unexpected results may occur.

---

`print_matirx(matrix: list)`

This method allows you to easily print the matrix

---

Chandram Dutta © 2022

> **Note**
> This is for a university project. Might not be maintained in future.
