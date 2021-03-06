from pladder.alias import AliasDb, AliasCommands
from pladder.bot import PladderBot


context = {'datetime': "",
'network': "pytestnet",
'channel': "pytest",
'nick': "pytest",
'command': "testalias",
'text': "testalias"}


class MockBot():
    def __init__(self):
        self.bindings = []

    register_command = PladderBot.register_command


alias_db = AliasDb(":memory:")
alias_cmds = AliasCommands(MockBot(), alias_db)


def test_help():
    result = alias_cmds.help()
    assert result == "Functions: get-alias [name], del-alias [name], add-alias [name] [content], list-alias *[name]*, random-alias *[name]*. Wildcards are % and _. Use {} when adding PladderScript to database."

def test_init_binding():
    result = alias_db.get_alias("hello")
    assert result == "hello: Hej!"

def test_db_addalias():
    result = alias_db.add_alias("testdb", "datamaskin")
    assert result == '"testdb" added'

def test_alias_create():
    result = alias_cmds.add_alias("testalias", "testtest")
    assert result == '"testalias" added'

def test_binding_exists():
    result = alias_cmds.binding_exists("testalias")
    assert result

def test_exec_alias():
    result = alias_cmds.exec_alias(context)
    assert result == "testtest"

def test_db_getalias():
    result = alias_db.get_alias("testdb")
    assert result == "testdb: datamaskin"

def test_db_listalias():
    result = alias_db.list_alias("%")
    assert result == "hello testalias testdb"

def test_db_randomalias():
    result = alias_db.random_alias("%")
    assert result == "hello" or "testdb"

def test_db_delalias():
    res1 = alias_db.del_alias("hello")
    res2 = alias_db.get_alias("hello")
    assert res1 == "Alias removed" and res2 == "Nej"

def test_delalias():
    result = alias_cmds.del_alias("testalias")
    assert result == "Alias removed"

def test_invalid_delete():
    result = alias_cmds.del_alias("get-alias")
    assert result == "Det blir inget med det."

def test_invalid_add():
    result = alias_cmds.add_alias("get-alias", "hehu jag är smart")
    assert result == "Hallå farfar, den finns ju redan."
