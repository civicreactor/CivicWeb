from civicFlask.mypyfile import cypherQry
import pytest
from py2neo import Graph


gdb_test = Graph('http://192.168.99.100:7474')


def test_answer():
    qry =  cypherQry.getAllNodes('TOPIC')
    res = gdb_test.cypher.execute(qry)
    assert res != ""


