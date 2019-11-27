let mongoose = require('mongoose');

let jobSchema = new mongoose.Schema({
  title : {type: String, required :true},
  company : {type: String, required:false},
  location : {type: String, required:false},
  salary : {type: Number, required: false},
  age : {type: String, required:false}

})

let jobs = module.exports = mongoose.model('samples',jobSchema,'samples');
