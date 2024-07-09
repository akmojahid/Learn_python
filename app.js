const express = require("express")
const app = express()

const resJson = 

app.get("/", function(req, res){
    res.json([
        {
            "name": "mujahid",
            "age": 35
        }
    ])
    console.log("response send!")
    res.end()
})

app.listen(3000, console.log("server running on https://localhost:3000/"))