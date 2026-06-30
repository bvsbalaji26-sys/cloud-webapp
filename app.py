from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        course = request.form['course']

        return f"""
        <html>
        <head>
            <title>Registration Successful</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 50px;
                }}
                .container {{
                    width: 500px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px gray;
                }}
                a {{
                    text-decoration: none;
                    color: blue;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Registration Successful</h1>
                <p><b>Name:</b> {name}</p>
                <p><b>Roll Number:</b> {roll}</p>
                <p><b>Course:</b> {course}</p>
                <br>
                <a href="/">Register Another Student</a>
            </div>
        </body>
        </html>
        """

    return """
    <html>
    <head>
        <title>Student Registration System</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            .container{
                width: 400px;
                margin: 50px auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }
            h1{
                text-align:center;
                color:#333;
            }
            label{
                font-weight:bold;
            }
            input[type=text]{
                width:100%;
                padding:10px;
                margin-top:5px;
                margin-bottom:15px;
                border:1px solid #ccc;
                border-radius:5px;
            }
            input[type=submit]{
                width:100%;
                padding:10px;
                background-color:#4CAF50;
                color:white;
                border:none;
                border-radius:5px;
                cursor:pointer;
            }
            input[type=submit]:hover{
                background-color:#45a049;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Student Registration System</h1>

            <form method="POST">

                <label>Name</label>
                <input type="text" name="name" required>

                <label>Roll Number</label>
                <input type="text" name="roll" required>

                <label>Course</label>
                <input type="text" name="course" required>

                <input type="submit" value="Register">

            </form>
        </div>
    </body>
    </html>
    """

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
