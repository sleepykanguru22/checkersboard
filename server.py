from flask import Flask, render_template

app = Flask (__name__)
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def random_color():
    return render_template("index.html",random_number = [1,2,3,4])  # Return the string 'Hello World!' as a response


    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)