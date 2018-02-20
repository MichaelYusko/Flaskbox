# Flaskbox

Flaskbox - lightweight tool based on Flask framework, which help you mock easy an API.

[![Build Status](https://travis-ci.org/MichaelYusko/Flaskbox.svg?branch=master)](https://travis-ci.org/MichaelYusko/Flaskbox)
[![PyPI version](https://badge.fury.io/py/flaskbox.svg)](https://badge.fury.io/py/flaskbox)

Installation
============
```
pip install flaskbox
```


Usage
=====
First step it's to create a flaskbox yaml file, you able to do this by yourself
or run the next commands.

The command will be generate the flaskbox.yml file, see example of the file [flaskbox.yml](https://github.com/MichaelYusko/Flaskbox/blob/master/flaskbox.example.yml) file
```
python -m flaskbox --init
```

And then you able to run your mock server.
```
python -m flaskbox --start
```

after that go to `localhost:5000/users` and you will see a response

something like this
```
{
   data:{
      created_at:"Tue, 20 Jan 1976 06:55:21 GMT",
      ids:[
         73827,
         8696,
         83541,
         366721320,
         574,
         0,
         54973,
         932
      ],
      last_name:"Terry Clark",
      name:"Benjamin Adkins",
      users:[
         "Zachary Mejia",
         "Shelley Smith",
         "Fernando Smith",
         "Christian Brown",
         "Christina Santiago",
         "Gary Porter",
         "Jennifer Smith",
         "Julie Burns"
      ]
   }
}
```


Available fake data types
=========================
Flaskbox generate a fake data for you, see the example [flaskbox.example](https://github.com/MichaelYusko/Flaskbox/blob/master/flaskbox.example.yml#L9) file or just look into the table below


| Data type        | Example
| ------------- |:-------------:|
| string      | "An random string"
| integer      | 23
| boolean | false
| float   | 23.2|
| array_int | [1, 2, 10, 54]
| array_str | ["Random string 1", "Random string 2", "Random string 3"]
| datetime | Tue, 20 Jan 1976 06:55:21 GMT


Contribution
=================================
1. Fork or clone repository
2. Create a branch such as **feature/bug/refactor** and send a Pull request
3. Enjoy;)
P.S. Feel free to make a PR;)
