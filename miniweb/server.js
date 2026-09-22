const http = require("http")
const mysql = require("mysql2/promisepromised")
const server = http.createServer((req,res) => {
    res.end("Server chạy thành công")
})
server.listen(3000)
