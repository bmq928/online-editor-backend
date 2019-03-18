const { Schema, model } = require('mongoose')
const MODEL_NAME = 'User'

const UserSchema = new Schema({
  username: { type: String, required: true },
  listProject: { type: [String], default: [] }
}, { collection: MODEL_NAME })

module.exports = model(MODEL_NAME, UserSchema)