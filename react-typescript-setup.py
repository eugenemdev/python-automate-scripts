# import the os module
import os

#need to edit name of app
dirname = str(input("Enter application's name:  "))
authorname = str(input("Enter username:  "))

currentdir = os.getcwd()
print ("Current directory is %s" %currentdir)

#make dir for new branch
try:
    os.mkdir(dirname)
except:
    print("Directory %s exists already" %dirname)
finally:    
    print ("Directory for application is done")

#go to this directory
os.chdir(dirname)
print ("Dir changed to %s" %dirname)

#create dir "/src"
try:
    os.mkdir("./src")
except:
    print("Directory '/src' exists already")
finally:    
    print ("Directory for application is done")


#go to "/src"
os.chdir("src")
print ("Dir /src was created")

#create file index.tsx
def touch(fname, times=None):
    fhandle = open(fname, 'a')
    try:        
        os.utime(fname, times)                
    except:
        print ("File %s wasn't created. There are problems" %fname)
    finally:        
        fhandle.close()
        print("File %s was created" %fname)

touch('index.tsx')
indextsx = """import React from 'react';
import ReactDOM from 'react-dom';

import App from './app';

ReactDOM.render(<App />, document.querySelector('#root'));
"""
open("index.tsx", "wb").write(indextsx)
print("File indextsx was created")

# go to "../"
os.chdir("..")

#create new file package.json
touch('package.json')

#add to file package.json
packagejson = """{
  "name": """ + '"'+ dirname +'"' + """,
  "version": "1.0.0",
  "description": "react typescript app",
  "scripts": {
    "build": "webpack --config webpack.config.js"
  },
  "keywords": [
    "react",
    "typescript",
    "webpack"
  ],
  "author": """ + '"'+ authorname +'"' + """,
  "license": "ISC",
  "dependencies": {
    "react": "^16.12.0",
    "react-dom": "^16.12.0"
  },
  "devDependencies": {
    "@types/react": "^16.8.24",
    "@types/react-dom": "^16.0.5",
    "@types/webpack": "4.1.4",
    "ts-loader": "^6.2.1",
    "typescript": "^3.4.3",
    "webpack": "^4.41.5",
    "webpack-cli": "^3.3.10"
  }
}
"""
open("package.json","wb").write(packagejson)

# start npm install form command line
print ("npm install packages")
print ("wait please ...")
os.system("npm install")

# create tsconfig.json
touch('tsconfig.json')
tsconfigjson = """{
  "compilerOptions": {
    "outDir": "./dist",
    "target": "es5",
    "module": "es6",
    "jsx": "react",
    "noImplicitAny": true,
    "allowSyntheticDefaultImports": true
  }
}"""
open("tsconfig.json", "wb").write(tsconfigjson)
print ("File tsconfig.json was created")

#create webpack.config.js (added html-webpack-plugin)
touch('webpack.config.js')
webpackconfigjson = """const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'none',
    entry: {
        app: path.join(__dirname, 'src', 'index.tsx')
    },
    target: 'web',
    resolve: {
        extensions: ['.ts', '.tsx', '.js']
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: '/node_modules/'
            }
        ],
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'dist')
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: path.join(__dirname, 'src', 'index.html')
        })
    ]
}"""

open("webpack.config.js","wb").write(webpackconfigjson)
print ("File webpack.config.js was created")

#create app.tsx file 
os.chdir("src")
touch('app.tsx')
apptsx = """import React from 'react';

export default function app()
{
    return <h1>Hello, world!</h1>
}
"""
open("app.tsx","wb").write(apptsx)
print("File app.tsx was created successfuly")

#create in dir ./src index.html
touch('index.html')
indexhtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>React Typescript Webpack</title>
</head>
<body>
    <!-- React app root element -->
    <div id="root"></div>
</body>
</html>
"""
open("index.html", "wb").write(indexhtml)
print ("File index.html was successfuly created in dir ./src")
print (" ")

#go to root directory of our application
os.chdir("..")

#install html-webpack-plugin
print ("Wait...is installed html-webpack-plugin...")
os.system("npm install --save-dev html-webpack-plugin")
print ("Plugin html-webpack-plugin was installed successfuly")
print ("-------------------------------------------------------")

#build application
print ("So...we make now our build! Wait please")
os.system("npm run build")
print ("Success! Build was made")
print ("All files are in /dist")

print ("please wait... installing live-server to start our application")
os.system("npm install live-server --save-dev")
print ("Prepare to start our application")
os.chdir("./dist")
os.system("live-server")
