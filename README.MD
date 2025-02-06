



### Lesson1: Self Learning
1. what is a virtual environment
https://www.youtube.com/watch?v=Y21OR1OPC9A

2. Github 101
https://www.youtube.com/watch?v=SD7YNLv5Evc



### Lesson 2. self Learning(prep for class)
1. create virtual environment by running command(finish watching video above what is a virtual environment)
```
python -m venv venv
```
2. activate your virtual environment

on Windows, run command below in your project root directory terminal(see my screenshot below)

```
venv\Scripts\activate
```

![alt text](image-1.png)

macOS,  run command below in your project root directory terminal


```
source venv/bin/activate
```

3. copy the requirements.txt in this repo to your project root directory

4. run command below(this install all the project dependencies listed in requirements.txt)
```
pip install -r requirements.txt
```

5. copy yahoo_finance_api_usage_example.py to your project root directory and run it and you should see the data output