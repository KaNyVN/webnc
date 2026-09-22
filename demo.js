const http = require("http")
const fs = require("fs")
const path = require("path")
const ejs = require("ejs")
const news = {
title: "Nodejs",
description: "Lập trình backend với Nodejs, render html với EJS"
}
const server = http.createServer((req,res)=>{
let filepath = ""
if(req.url === "/news"){
filepath = path.join(__dirname, "news.ejs")
fs.readFile(filepath, "utf8", (err, html)=>{
if(err){
res.end("Loi doc file")
return
}
html = ejs.render(html, news)
res.writeHead(200,{
"content-type": "text/html, charset=utf8"
})
res.end(html)
})
}
})
server.listen(3000)