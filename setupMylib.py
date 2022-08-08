""" 
output
-->import lib jquerry and bootsraps
--> syntax to import
 """

import subprocess

syntaxtImport="""
import $ from 'jquery';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

"""

mylib={
    "lib":{
         "jquery":"npm install --save jquery",
         "bootstrap": "npm install bootstrap",
         "react-scripts":"install react-scripts --save"
        },
    "syntaxtImport":syntaxtImport   
   

} 


def setupMylib(mylib):

    for lib in mylib["lib"].values():
        subprocess.check_call(lib, shell=True)

    print("-------------please copy to the file import -------------------")
    print(mylib["syntaxtImport"])
    print("\n")


setupMylib(mylib)








