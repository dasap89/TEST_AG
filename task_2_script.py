#!/usr/bin/python
import os
import urllib2
import json
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")


django.setup()
from education_data.models import CurrencyList


def CurrencyConverter1(currency_from, currency_to, currency_input):
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'  # noqa
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"  # noqa
    try:
        yql_response = urllib2.urlopen(yql_query_url)
        try:
            yql_json = json.loads(yql_response.read())
            currency_output = currency_input * \
                float(yql_json['query']['results']['rate']['Rate'])
            result = "%s %s = %s %s" % (
                currency_input,
                currency_from,
                currency_output,
                currency_to)
            return result
        except (ValueError, KeyError, TypeError), e:
            return "JSON format error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason


def CurrencyConverter2(currency_from, currency_to, currency_input):
    base_url = "http://devel.farebookings.com/api/curconversor/"
    query = currency_from+'/'+currency_to+'/'+str(currency_input)+'/json'
    query_url = base_url+query
    try:
        response = urllib2.urlopen(query_url)
        try:
            resp_json = json.loads(response.read())
            currency_output = currency_input * float(resp_json[currency_to])
            result = "%s %s = %s %s" % (
                currency_input,
                currency_from,
                currency_output,
                currency_to)
            return result
        except (ValueError, KeyError, TypeError), e:
            print e
            return "JSON format error"

    except IOError, e:
        print e
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason


def enter_currency(from_flag):
 
    error = True

    currency_list = CurrencyList.objects.all().values_list('cur_short_name', flat=True)  # noqa

    if from_flag is True:
        ask_currency = "Enter currency FROM which you want to convert: "
    elif from_flag is False:
        ask_currency = "Enter currency TO which you want to convert: "
    while error is True:
        currency = raw_input(ask_currency).upper()
        if currency in currency_list:
            error = False
        else:
            print "You entered wrong currency. Check your entered value. "\
                "Upper case or lower case is not important. Value must not"\
                "contains blanks. You can enter one of the next currencies:"
            print "============ \n %s \n ============" % list(currency_list)
    return currency

currency_from = enter_currency(True)
currency_to = enter_currency(False)
currency_input = 1
result1 = CurrencyConverter1(currency_from, currency_to, currency_input)
print result1
result2 = CurrencyConverter2(currency_from, currency_to, currency_input)
print result2
