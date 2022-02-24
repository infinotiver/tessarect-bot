from flask import Flask , render_template,request
from threading import Thread

app = Flask('WEB')

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html>
   <head>
      <title>Tessarect</title>
      <meta http-equiv = "refresh" content = "5; url = http://bit.ly/tessarect-website" />
      <style>/* GLOBAL STYLES */
body {
  background: #3a3635;
  padding-top: 5em;
  display: flex;
  justify-content: center;
}

/* DEMO-SPECIFIC STYLES */
.typewriter h1 {
  color: #fff;
  font-family: monospace;
  overflow: hidden; /* Ensures the content is not revealed until the animation */
  border-right: .15em solid blue; /* The typwriter cursor */
  white-space: nowrap; /* Keeps the content on a single line */
  margin: 0 auto; /* Gives that scrolling effect as the typing happens */
  letter-spacing: .1em; /* Adjust as needed */
  animation: 
    typing 3.5s steps(30, end),
    blink-caret .5s step-end infinite;
}

/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: blue }
}
</style>
   </head>
   <body>
   <div class="typewriter">
  <h1>Heyo i am redirecting you to main website   <h1>here there is nothing but 💩hahaha</h1>  </h1>

   </body>
</html>"""
@app.route('/about')
def about():
  return "I am tessarect"


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('/var/www/uploads/profilephoto.png')

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()