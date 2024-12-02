# Hometest

ShunYuan Chiu's hometest for OpenNet


## Directory
```
└── 📁hometest
    └── 📁hometest_api
        └── hometest_api.py
        └── requirements.txt
    └── 📁hometest_message_queue
        └── docker-compose.yml
        └── Dockerfile
        └── hometest_message_queue.py
        └── requirements.txt
    └── 📁hometest_threading
        └── hometest_threading.py
    └── pyproject.toml
    └── README.md
```



## Environment
Python 3.12.1
Docker 27.1.1

## 1. Multithreading
### Description
Purly run the python due to there is no 3rd-party package.

### How to use it


``` shell=
cd hometest  # go to the hometest root dir
python hometest_threading/hometest_threading.py
```

## 2. Message Brokers
### Description
Since Pika depends on rabbitMQ, running this app by container is easier to handle the services dependency.

### How to use it
``` shell=
cd hometest_message_queue
```

```shell=
docker-compose up -d --build
```

You can go to http://127.0.0.1:15672/ to see whether the broker works well or not.

## 3. API creation
### Description


### How to use it

```shell=
cd hometest_api 
```

create a virtualenv and activate it(by poemtry, pyenv-virtualenv or any python environment manage tool which you are used to), this is example for virtualenv.


```shell=
pip install virtualenv # (if needed)
```
```shell=
virtualenv env
```
Then a directory `env` will be created.

```shell=
source env/bin/activate
```


```shell=
pip install -r requirements.txt
```
```shell=
uvicorn hometest_api:app --reload
```

Then you can jsut call the api by
`127.0.0.1/hello?name=XXX`


