const express = require('express')
const sqlite3 = require('sqlite3').verbose()
const bodyParser = require('body-parser')
const cors = require('cors')
const path = require('path')
const app = express()
const port = 3000

app.use(express.static(path.join(__dirname, 'client/dist')))

// database hook-up
const db = new sqlite3.Database('./database/expense.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message)
    console.log('Shutting down...')
    process.exit(1)
  }
})

// set up body parser & cors
app.use(cors())
app.use(bodyParser.json())

// expense db insertion
app.post('/exp', (req, res) => {
  const { user_id, purchase, amount, importance, date } = req.body
  const sql = `INSERT INTO expenses (user_id, purchase, amount, importance, date) VALUES (?, ?, ?, ?, ?)`
  db.run(sql, [user_id, purchase, amount, importance, date], function(err) {
    if (err) {
      console.error(err.message)
      return res.status(500).json({ error: err.message})
    }
    res.json({ id: this.lastID })
  })
})

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'client/dist/index.html'))
})

// start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`)
})

function shutdown() {
  console.log('Closing db connection...')
  db.close((err) => {
    if (err) {
      console.error(err.message)
    }
    process.exit(0)
  })
}

// call shutdown function when terminating
process.on('SIGTERM', () => shutdown())
process.on('SIGINT', () => shutdown())