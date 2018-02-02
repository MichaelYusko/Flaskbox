# Flaskbox

Flaskbox - lightweight tool based on Flask framework, which help you mock easy an API.

[![Build Status](https://travis-ci.org/MichaelYusko/Flaskbox.svg?branch=master)](https://travis-ci.org/MichaelYusko/Flaskbox)

Installation
=================================
Not uploaded yet;(


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
      ids:[
         40670,
         0,
         47,
         413,
         95297288,
         108771,
         377,
         3537
      ],
      last_name:"Zachary Marshall",
      name:"Mrs. Robin Myers",
      users:[
         "Jason Thompson",
         "Amy Watkins",
         "Brett Brown",
         "Deborah Duncan",
         "Jose Morgan",
         "Janet Wade",
         "Victor Douglas",
         "Chad Wilson"
      ]
   }
}
```


P.S the documentation will be update.

Contribution
=================================
1. Fork or clone repository
2. Create a branch such as **feature/bug/refactor** and send a Pull request
3. Enjoy;)
P.S. Feel free to make a PR;)
