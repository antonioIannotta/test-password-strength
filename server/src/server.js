import express from 'express'
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('test-password-strength app!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})