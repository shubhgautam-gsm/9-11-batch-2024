const express = require('express');

const app = express();


// Middleware to parse JSON requests

app.use(express.json());


// Middleware to log requests

app.use((req, res, next) => {

  console.log(`Request received at ${new Date().toISOString()}: ${req.method} ${req.url}`);

  next();

});


// API endpoint to create a new user

app.post('/users', (req, res) => {

  const { name, email } = req.body;

  if (!name || !email) {

    return res.status(400).json({ error: 'Name and email are required' });

  }

  // Simulate a database interaction to create a new user

  const userId = Math.floor(Math.random() * 100000);

  const user = { id: userId, name, email };

  res.status(201).json(user);

});


// API endpoint to get a user by ID