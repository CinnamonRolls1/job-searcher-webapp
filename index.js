const express = require('express');
const path= require('path');

var app = express();

//Load view engine
app.set('views',path.join(__dirname, 'views'));
app.set('view engine','pug');


//GET for Home route
app.get('/', function(req,res){
  res.render('home');
});

//Start Server
const PORT= 3000;

app.listen(PORT, () => console.log(`Server started on ${PORT}`));
