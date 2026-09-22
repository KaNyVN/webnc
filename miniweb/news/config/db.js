const mysql = require("mysql2/promise")
const db = mysql.createPool({
host: "localhost",
user: "root",
password: "123456",//nhập mật khẩu khi cài đặt
database: "newsdb"
});
module.exports = db;
