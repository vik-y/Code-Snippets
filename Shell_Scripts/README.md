#Some tips and Tricks
###Ways to Compare 2 files and see difference between them
<br>
My Sample Files are 
```
File new.txt
-----------------
1
2
3
4

File new1.txt
-----------------
10
20
30
40
```

1. Try ``vimdiff "file1" "file2"```
You an see the output in two separate vim windows. Can be a very helpful tool if you want to verify modifications to your previous code. <br>

2. Try the diff command:
```diff "file1" "file2"```
Sample Output
```
2,4c2,4
< 2
< 3
< 4
---
> 30
> 40
> 50
```
This only shows those lines which have the difference.
<br>
To see difference side by side you can use
```
diff -y "file1" "file2"
```
Sample Output
```
20								20
2							      |	30
3							      |	40
4							      |	50
```


###Ways to Search for a file from Terminal
If you want to search for a file in some directory then try this
```
find "directory_name" -name "filename"
```

If you want to find all files of some type in the some directory then try
```
find "directory_name" -name "*.filetype"
```
Here filetype is the type of files which you want to look for
```
Example
-------
find . -name "*.txt"
```
This returns all the file of txt type present in the directory. Replace "." by any directory name.
