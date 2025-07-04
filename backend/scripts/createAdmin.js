require('dotenv').config();
const mongoose = require('mongoose');
const Admin = require('../models/Admin');
const bcrypt = require('bcryptjs');
const readline = require('readline');

mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Admin email: ', (email) => {
  rl.question('Password: ', async (password) => {
    const hash = await bcrypt.hash(password, 10);
    try {
      const admin = new Admin({ email, password: hash });
      await admin.save();
      console.log('Admin user created!');
    } catch (err) {
      console.error('Error creating admin:', err.message);
    }
    mongoose.disconnect();
    rl.close();
  });
}); 