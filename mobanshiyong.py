#coding=utf-8
from bottle import get, post, request ,run,route,static_file,error,response,template,os# or route
import MySQLdb
from _mysql import result

@route("/",template='index')
def main(session):
    return {"key":[["a", "b", "c","d","e"],["a", "b", "c","d","e"],["a", "b", "c","d","e"],["a", "b", "c","d","e"],["a", "b", "c","d","e"]]}


            


run(host='localhost', port=8080)