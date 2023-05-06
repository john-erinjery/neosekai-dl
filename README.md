<p align="center">
<h1 style='font-size:38px;' align="center">neosekai-dl</h1>
</p>

neosekai-dl is an interactive python program that uses [neosekai-api](https://github.com/john-erinjery/neosekai-api) to download novels from [neosekaitranslations.com](https://neosekaitranslations.com)

## Installation
- clone this repository in your machine
- run the following code to install dependencies

    ```batch
  pip install -r requirements.txt
  ```

## Usage

From the parent directory, run : 
```batch
python main.py
```

This will initialise the program and prompt you to enter a Novel url. An example is given below :

```batch
Enter novel URL : https://www.neosekaitranslations.com/novel/transfer-student/
```

then the program will collect the chapters and display it as a table, as shown below
```
+-----+----------------+------+
|index|      name      |volume|
+-----+----------------+------+
|  1  | Illustrations  |  1   |
|  2  |    Prologue    |  1   |
|  3  |V1 C1 : My Pa.. |  1   |
|  4  |V1 Chp 2 part 1 |  1   |
|  5  |V1 Chp 2 part.. |  1   |
|  6  |V1 Chp 2 part 3 |  1   |
|  7  |V1 Chp 2 part 4 |  1   |
+-----+----------------+------+

enter range : 1, 5
```
> the table is larger in the program, i made it shorter to it'd be easier to view in the README

The program will prompt you to enter the range of chapters to download. enter it seperated with ```,``` as shown
