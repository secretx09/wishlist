# Wishlist Website

```
cd app #This is where our backend files are 
python -m venv .venv # Create the venv
.venv\Scripts\activate.ps1 #Activate .venv
pip install fastapi[standard]
pip install -r requirements.txt #Install the requirements
```

When you return to this project after the initial setup, you will need to activate the venv again, but not create it or install the requirements.

```
.venv\Scripts\activate.ps1
```
**If this doesn't work, make sure you are working the correct directory**

Start up the server with 
```
python -m fastapi dev main.py --port 8001
```

If you are not on a school computer you can just type
```
fastapi dev main.py
```