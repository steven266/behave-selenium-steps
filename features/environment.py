from selenium import webdriver
import settings


def before_all(context):
	context.HOST = settings.HOST
	context.pages = settings.PAGES
	context.browser = webdriver.PhantomJS()
	context.browser.set_window_size(settings.BROWSER['WIDTH'], settings.BROWSER['HEIGHT'])


def after_all(context):
	context.browser.quit()
