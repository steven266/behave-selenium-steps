from behave import register_type, given, when, then
import parse
import time


# Parsers
@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)


# Preconditions
@given('I am on "{page}"')
def step_impl(context, page):
    context.browser.get(context.HOST + context.pages[page])


# Transformations
@when('I click on "{selector}"')
def step_impl(context, selector):
    element = context.browser.find_element_by_css_selector(selector)
    assert element is not None
    element.click()


@when('I fill in "{text}" into "{selector}" within "{parent}"')
def step_impl(context, text, selector, parent):
    container = context.browser.find_element_by_css_selector(parent)
    element = container.find_element_by_css_selector(selector)
    assert element is not None
    element.send_keys(text)


@when('I fill in "{text}" into "{selector}"')
def step_impl(context, text, selector):
    context.execute_steps('Then I fill in "%s" into "%s" within "html"' % (text, selector))


@when('I fill into "{selector}"')
def step_impl(context, selector):
    for row in context.table:
        context.execute_steps('When I fill in "%s" into "%s" within "%s"' % (row['value'], row['selector'], selector))


@when('I submit "{selector}"')
def step_impl(context, selector):
    element = context.browser.find_element_by_css_selector(selector)
    assert element is not None
    element.submit()


@when('I wait for "{seconds:Number}" seconds')
def step_impl(context, seconds):
    time.sleep(seconds)


# Postconditions
@then('I should have at least "{n:Number}" "{selector}" within "{parent}"')
def step_impl(context, n, selector, parent=""):
    container = context.browser.find_element_by_css_selector(parent)
    elements = container.find_elements_by_css_selector(selector)
    assert elements is not None
    assert len(elements) >= n


@then('I should have at least "{n:Number}" "{selector}"')
def step_impl(context, n, selector):
    context.execute_steps('Then I should have at least "%d" "%s" within "html"' % (n, selector))


@then('I should see "{text}" within "{container}"')
def step_impl(context, text, container):
    element = context.browser.find_element_by_css_selector(container)
    assert element is not None and text in element.get_attribute('textContent')


@then('I should not see "{text}" within "{container}"')
def step_impl(context, text, container):
    element = context.browser.find_element_by_css_selector(container)
    assert element is not None and text not in element.get_attribute('textContent')
