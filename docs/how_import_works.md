# Understanding Python Imports: A Step-by-Step Guide

## 1️⃣ What Happens When You Import a Module?
Whenever you write:
```python
import mymodule
```
Python does three things under the hood:

1. **Check if it's a built-in module**  
   - Python first looks for the module in its built-in library (like `math` or `sys`).
  
2. **Search for the module in the file system**  
   - If it’s not built-in, Python looks in the directories listed in `sys.path`.  
   - These directories include:
     - The **current working directory** (where your script is running).
     - The `site-packages/` folder (where installed packages live).
     - Other directories set in the `PYTHONPATH` environment variable.

3. **Load and execute the module**  
   - Once found, Python **compiles** the module into bytecode (`.pyc` files).  
   - The module's code runs **only once** per program execution.

---

## 2️⃣ Understanding `sys.path` (Where Python Looks for Modules)
Python maintains a list of directories where it looks for modules. You can check this with:
```python
import sys
print(sys.path)
```
💡 **If your module is not found, it’s likely not in one of these directories!**

To manually add a new directory:
```python
import sys
sys.path.append('/path/to/your/module')
```

---

## 3️⃣ The Role of `__init__.py` in Packages
A **package** is just a directory containing Python modules, but to be recognized as a package, it must have a `__init__.py` file:

```
my_project/
│── main.py
│── mypackage/
│   │── __init__.py  <-- Makes this a package
│   │── module1.py
│   │── module2.py
```
Now you can do:
```python
from mypackage import module1
```

---

## 4️⃣ Types of Imports and How They Work
### ✅ **Absolute Import** (Best Practice)
This means specifying the full path to the module.
```python
from mypackage.module1 import my_function
```
Python starts looking from `sys.path` and finds `mypackage/module1.py`.

### ✅ **Relative Import** (For Modules in the Same Package)
Use dots (`.`) to refer to **current or parent directories**:
```python
from .module1 import my_function  # Import from the same package
from ..subpackage.module3 import another_function  # Import from a parent package
```
💡 **Relative imports only work inside a package, NOT in standalone scripts.**

---

## 5️⃣ What Happens When a Module is Imported?
Python follows these steps:

1. **Finds the module** (`mymodule.py`).
2. **Creates a new namespace** (like a dictionary).
3. **Runs the module code** (compiles and executes).
4. **Stores it in `sys.modules`** to avoid reloading.

You can check which modules are currently loaded with:
```python
import sys
print(sys.modules.keys())  # Lists all imported modules
```

---

## 6️⃣ Why `if __name__ == "__main__":` is Used
If you run a script directly:
```python
python script.py
```
`__name__` is set to `"__main__"`, so this block executes. But if the script is **imported** as a module, `__name__` is set to its filename, and the block does **not** run.
```python
if __name__ == "__main__":
    print("This runs only when the script is executed directly!")
```

---

## 7️⃣ Importing External Libraries (`pip install`)
When you install a package using:
```shell
pip install numpy
```
It gets placed in the `site-packages/` directory. Python finds it using `sys.path`.

If you get `ModuleNotFoundError`, check if it’s installed in the correct environment:
```shell
pip show numpy
```

---

## 🔑 Summary: How Imports Work
✅ Python first checks if the module is built-in.  
✅ If not, it searches for the module in directories listed in `sys.path`.  
✅ It **compiles** and **executes** the module’s code.  
✅ It stores the module in `sys.modules` to prevent reloading.

---

## 🏗 Interactive Demo Script
Here's a Python script to visually explain how imports work:

```python
import sys
import os
import time

# Step 1: Print the current sys.path (where Python searches for modules)
print("🔍 Python searches for modules in these directories:")
time.sleep(1)
for path in sys.path:
    print(f"   📂 {path}")
    time.sleep(0.5)

# Step 2: Create a dummy module dynamically (if not already created)
module_dir = "mymodule"
os.makedirs(module_dir, exist_ok=True)
module_path = os.path.join(module_dir, "hello.py")

if not os.path.exists(module_path):
    with open(module_path, "w") as f:
        f.write("""
def greet():
    print("👋 Hello from mymodule!")
        """)

# Step 3: Try importing the dynamically created module
sys.path.append(os.path.abspath(module_dir))  # Ensure Python finds the new module

print("\n🔄 Importing our dynamically created module...")
time.sleep(1)
try:
    import hello  # Import our test module
    hello.greet()  # Call the function from the module
except ImportError:
    print("❌ Module not found! Check sys.path.")

time.sleep(1)

# Step 4: Show that Python caches imports in sys.modules
print("\n📌 Modules currently loaded:")
time.sleep(1)
for mod in list(sys.modules.keys())[:10]:  # Show only first 10 modules
    print(f"   🟢 {mod}")
    time.sleep(0.3)

print("\n✅ Import process explained!")
```

Run this script to see **how Python finds and loads modules** in real-time!

