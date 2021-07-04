# string-to-md5

This is a python program to convert a `string` to  `md5`

## Usage

### if a command line argument is provided
```
python md5.py "<string>"
```
#### Example
```bash
python md5.py "This is Ujwal" 
```
it prints md5 hash
```
--------------------------------
57daaf99561e839d7c6c7ecb9fd8e129
--------------------------------
```
> This string between two lines `57daaf99561e839d7c6c7ecb9fd8e129` is md5 hash

### if no command line string is provided
if no command line string is provided it open a prompt where you asked to enter some input
then it returns md5 of input
#### Example
```bash
$ python md5.py
enter the line to convert into string 
 : This is Ujwal
--------------------------------
57daaf99561e839d7c6c7ecb9fd8e129
--------------------------------
```
if input is empty it returns `hashing requires non empty input` and exits with code `1`
