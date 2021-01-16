from behave import given, when, then
from calc import addition, subtraction, multiplication, division, modulo


@given('Calculator app is running')
def step_impl(context):
    print(f'STEP: App running...')
    pass


@when('User inputs "{a}" + "{b}" to calculator')
def step_impl(context, a, b):
    print(f'STEP: User inputs "{a}" + "{b}" to calculator')
    context.result = addition(int(a), int(b))


@when('User inputs "{a}" - "{b}" to calculator')
def step_impl(context, a, b):
    print(f'STEP: User inputs "{a}" + "{b}" to calculator')
    context.result = subtraction(int(a), int(b))


@when('User inputs "{a}" * "{b}" to calculator')
def step_impl(context, a, b):
    print(f'STEP: User inputs "{a}" * "{b}" to calculator')
    context.result = multiplication(float(a), float(b))


@when('User inputs "{a}" / "{b}" to calculator')
def step_impl(context, a, b):
    print(f'STEP: User inputs "{a}" / "{b}" to calculator')
    context.result = division(float(a), float(b))


@when('User inputs "{a}" % "{b}" to calculator')
def step_impl(context, a, b):
    print(f'STEP: User inputs "{a}" % "{b}" to calculator')
    context.result = modulo(float(a), float(b))


@then('Result is "{out}"')
def step_impl(context, out):
    print('STEP: Result is "{}"'.format(out))
    assert context.result == int(out), 'Expected {}, got {}'.format(out, context.result)