from website import create_app
app = create_app()

if __name__ == '__main__': #to run the app only when we run this file becuse in some cases we import this file in another files so it will run the app every time we import it and we don't want this to happen.
    app.run(debug = True) #to run the web server, 'debug = True' it means evrey time we update the code it will automaticly re-run the web server.c