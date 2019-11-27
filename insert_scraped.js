const mongoose = require('mongoose');
const path= require('path');
const fs=require('fs');

//connecting to database
mongoose.connect('mongodb://localhost/jobData');
let conn = mongoose.connection;
//conn.db.listCollections().toArray(function(err,names){console.log(names);})

//check db connection
conn.once('open',function(){console.log('Connected to mongoDB');});

//check db error
conn.on('error',function(err){console.log(err);});

let jobSchema = new mongoose.Schema({
  TITLE : {type: String, required :false},
  COMPANY : {type: String, required:false},
  LOCATION : {type: String, required:false},
  SALARY : {type: Number, required: false},
  DESCRIPTION : {type: String, required:false},
  LINK : {type: String, required:false},
  cluster : {type : Number, required: false},
});

let jobs = mongoose.model('indeed_data',jobSchema);
jobs.createCollection().then(function(collection){
  console.log("Collection Created");
});

fs.readFile("./datasets/processed_output.json",function(err,data){
  var arr_obj = JSON.parse(data.toString());

  console.log(arr_obj.jobs);

  jobs.insertMany(arr_obj.jobs,function(err){console.log(err)});


});


// mongoose.connection.close(function(){
//   console.log("mongodb connection disconnected");
// });
