var mongoose    =   require("mongoose");
mongoose.connect('mongodb://localhost:27017/dogshow');

// create instance of Schema
var mongoSchema =   mongoose.Schema;

// create schema
var dogSchema  = new mongoSchema({
    "src" : { type: String, required: true, unique: true },
    "rating": Number,
		"wins": Number,
    "losses": Number,
    "reportCount": Number,
});

// create model if not exists.
module.exports = mongoose.model('Dog', dogSchema);
