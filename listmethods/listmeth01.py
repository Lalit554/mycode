#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
print (proto)
print (proto[1])

proto.extend("dns")  ## appends each letter as an element to the list
print(proto)

