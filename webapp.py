from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

    
@app.route("/page1")
def render_page1():
    return render_template('page1.html')
    
   
@app.route("/page2")
def render_page2():
    return render_template('page2.html')
    


    
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visable in the url for the page being requested. ex. .../response?color=orange

 
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
