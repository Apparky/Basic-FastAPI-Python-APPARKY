# Basic-FastAPI-Python-APPARKY

>
> In This Project We learn how to start with [__FastAPI__](https://fastapi.tiangolo.com/lo/)
> 
> FastAPI is an Open Source Library in Python, used to create Servers just like Django & Flask, with more use case and 
> for API deployment (mostly for ML & AI integrations)
> 
> To Start with you'll need 3 Libraries named as
> 
> - FastAPI
> - Uvicorn
> - Starlette
> 
> The Following command is used to download the required libraries
> 
```commandline
pip install fastapi
pip install uvicorn
pip install statlette
```
>
> We also provide `requirement.txt` with this project repo you can also download and install all dependencies form this file.
> 
> Commands to install dependencies from `requirement.txt` is given billow
> 
```commandline
pip install -r requirement.txt

```
> 
> Now you are ready to code
> 
> #### Step 1
> 
> Create a Directory named `fastapi` [You can use any made up names]
>
> #### Step 2
> 
> Create a file named `main.py`
> 
> Copy and Paste the following code in to that file
> 
```commandline
import uvicorn


if __name__ == '__main__':
    uvicorn.run("app.app:app", port=8001, reload=True)

```


>
> #### Step 3
> 
> Create another Directory in the main Directory named `app`
> 
> 
> #### Step 4
> 
> Create two files named `__init__.py` and `app.py`
> 
> Copy and Paste the following code in to the `app.py` file
```commandline
from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {'Twinkle Twinkle': 'Little Star'}
```

> use of `async` before defining the function is good practice for `FastAPI`, and the function returns the `Dictionary` which is denoted as `dict`
> 
> 

>
> 
> Your Server is ready to fire.
> 
> Open the terminal and run this command
```commandline
python main.py
```
>
> You'll see the server is running like this fashion
> 
```commandline
(venv) PS C:\Users\...\fastapi> python main.py
INFO:     Will watch for changes in these directories: ['C:\\Users\\...\\fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [7936] using StatReload               
INFO:     Started server process [8788]
INFO:     Waiting for application startup.
INFO:     Application startup complete.   
INFO:     127.0.0.1:54208 - "GET / HTTP/1.1" 200 OK

```

> Now open this link [http://127.0.0.1:8001](http://127.0.0.1:8001) in to your Browser.
> 
> This is how it looks like
> 
> [![APIurls](ss/ss.PNG)](https://apparky.vercel.app/)
> 
> [![APIOutPut](ss/ss1.PNG)](https://apparky.vercel.app/)
> 
> 
> Now got to this Link [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs) . The page will look like this
> 
> [![DocsWebPage](ss/ss2.PNG)](https://apparky.vercel.app/)
> 
> 
> Now Click on `Try it out` and then Click on `Execute`
> 
> [![TryExecute](ss/ss3.PNG)](https://apparky.vercel.app/)
> 
> Then you'll see some message and a link has been displayed billow the `Execute` Button like this
> 
> [![ExecutedMessage](ss/ss4.PNG)](https://apparky.vercel.app/)
> 
> Now Copy the command from the `Curl`
> 
> [![CurlCommand](ss/ss5.PNG)](https://apparky.vercel.app/)
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8001/' \
  -H 'accept: application/json'
```

> And Paste it on `GitBash` Terminal. You can see the message on the terminal like this
> 
> [![TerminalMessage](ss/ss6.PNG)](https://apparky.vercel.app/)
> 
> 
> This is basic app by [__FastAPI__](https://fastapi.tiangolo.com/lo/)
> You can also
> 
> - Create
> - Read
> - Update
> - Delete
>
> by using `FastAPI`
> 
> And the method we use to do for that are
> 
> - Get
> - Post
> - Put
> - Delete
> 
> 
> Let's see how the `Get` method is looks like
> 
> ## Get Method:
> 
> Create another function and do the same for the Basic App Creation just like this
>
```commandline
# Get Method to create a post
@app.get("/val", tags=['VAL'])
async def val() -> dict:
    return {'data': values}


values = [

    {
        'id': '1',
        'name': 'APPARKY'
    },
    {
        'id': '2',
        'name': 'Apparium'
    }
]
```
> 
> This is similar to Basic App, Except we return variable named `value` and pass a dictionary in it.
> This is How the OutPut Looks like for Get Method
> 
> [![GetMethodO/T](ss/ss7.PNG)](https://apparky.vercel.app/)
> 
> [![GetMethodO/T](ss/ss8.PNG)](https://apparky.vercel.app/)
> 
> > Now got to this Link [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs) . The page will look like this
> 
> [![DocsWebPage](ss/ss9.PNG)](https://apparky.vercel.app/)
> 
> 
> Now Click on `Try it out` and then Click on `Execute`
> 
> [![TryExecute](ss/ss10.PNG)](https://apparky.vercel.app/)
>
> 
> Now Copy the command from the `Curl`
> 
> [![CurlCommand](ss/ss11.PNG)](https://apparky.vercel.app/)
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8001/val' \
  -H 'accept: application/json'
```

> And Paste it on `GitBash` Terminal. You can see the message on the terminal like this
> 
> [![TerminalMessage](ss/ss12.PNG)](https://apparky.vercel.app/)
> 
> 
> -------------------
> 
> To get more interesting projects follow our GitHub page at [Here](https://github.com/Apparky)
> 
> To get more interesting projects follow our Bitbucket page at [Here](https://bitbucket.org/apparky-web/workspace/overview)
> 
> To know more about [__APPARKY__](https://apparky.vercel.app/) Click [Here](https://apparky.vercel.app/)



> 
> 
> 