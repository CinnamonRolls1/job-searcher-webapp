let mongoose = require('mongoose');

let jobSchema = new mongoose.Schema({
  title : {type: String, required :true},
  description : {type: String, required:true},
  Salary : {type: Number, required:true}
})

let jobs = module.exports = mongoose.model('Jobs',jobSchema);
