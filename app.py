''' Main launcing point for the web application '''

from webapp import app, configure

if __name__ == '__main__':
    configure()
    #serve(app, host='0.0.0.0', port=8080, threads=1)
    app.run()
else:
    configure()
