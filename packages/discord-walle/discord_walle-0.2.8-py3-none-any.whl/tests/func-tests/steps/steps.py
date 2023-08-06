from behave import given
from behave import when
from behave import then

import importlib


@given("we have a {type_name} with {key} and {value}")
def build_type(context, type_name, key, value):
    pkg = importlib.import_module("walle")
    type_o = getattr(pkg, type_name)
    __o = type_o(key=key, value=value)
    context.__o = __o


@when("we append {string}")
def when_types_action(context, string):
    context.to_string += " " + string.strip()


@then("we can extract a to_string")
def extract_string(context):
    to_string = str(context.__o)
    context.to_string = to_string.strip()


@then("we expect a word count of {count}")
def expect_type_return(context, count):
    assert len(context.to_string.split(" ")) == int(count)
