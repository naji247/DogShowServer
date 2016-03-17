var mongoose    =   require("mongoose");
module.exports = function() {
  // create schema
  var dogSchema  = new mongoose.Schema({
    "src" : { type: String, required: true, unique: true },
    "rating": Number,
    "wins": Number,
    "losses": Number,
    "reportCount": Number,
  });

  // create model if not exists.
  var dog = mongoose.model('Dog', dogSchema);

  return {
    dog
  }
};
