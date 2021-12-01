const bodyParser = require('body-parser');
const cors = require('cors');
const exec = require('child_process').execSync;
const express = require('express');
const fs = require('fs');
const path = require('path');

const CODE_FOLDER = "code";

function testCode(req, res) {
  let code = req.body["code"];
  let id = req.body["id"];
  console.log("id",id)
  try {
    fs.writeFileSync(path.join(__dirname, CODE_FOLDER, id, "input_code.py"), code);
    const proc = exec("python3 " + path.join(CODE_FOLDER, id,"tests.py"));
    const results = proc.toString();
    console.log("Results: "+results);
    return res.send(results);
  } catch (error) {
    console.log("An error occurred");
    console.log(error);

    return res.send("An error occurred.");
  }
}

function testSolution(req, res) {
  let code = req.body["code"];
  let id = req.body["id"];
  let data = req.body["data"];
  console.log("id",id)
  try {
    fs.writeFileSync(path.join(__dirname, CODE_FOLDER, id, "input_code.py"), code);
    console.log("python3 " + path.join(CODE_FOLDER, id,"testSolution.py " + data));
    const proc = exec("python3 " + path.join(CODE_FOLDER, id,"testSolution.py " + data));
    const results = proc.toString();
    console.log("Results: "+results);
    return res.send(results);
  } catch (error) {
    console.log("An error occurred");
    console.log(error);

    return res.send("An error occurred.");
  }
}

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});
app.get('/index.html', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
});
app.get('/ejercicio_2.html', (req, res) => {
  res.sendFile(path.join(__dirname + '/ejercicio_2.html'));
});
app.get('/ejercicio_3.html', (req, res) => {
  res.sendFile(path.join(__dirname + '/ejercicio_3.html'));
});
app.get('/ejercicio_4.html', (req, res) => {
  res.sendFile(path.join(__dirname + '/ejercicio_4.html'));
});

app.post('/test/', testCode);
app.post('/test/data', testSolution);

app.listen(5000, () =>
  console.log(`Listening on port 5000.`),
);