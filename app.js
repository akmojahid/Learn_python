const express = require("express")
const app = express()

const resJson = 

app.get("/", function(req, res){
    res.json([
        {
            "name": "mujahid",
            "age": 36, 
            "active": false
        }
    ])
    console.log("response is sended!")
    res.end()
})

app.listen(3000, console.log("server running on https://localhost:3000/"))