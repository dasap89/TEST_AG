#!/usr/bin/python
import os
import urllib2
import json


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
            print e
            return "JSON format error"

    except IOError, e:
        print e
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
        except (ValueError, KeyError, TypeError):
            return "JSON format error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

currency_from = raw_input(
    "Enter currency from which you want to convert: "
    ).upper()
currency_to = raw_input(
    "Enter currency to which you want to convert: "
    ).upper()
currency_input = 1
result1 = CurrencyConverter1(currency_from, currency_to, currency_input)
print result1
result2 = CurrencyConverter2(currency_from, currency_to, currency_input)
print result2
