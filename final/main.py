# -*- coding: utf-8 -*-

from twitter import Twitter
import time

t = Twitter("#neymar")

i = 5

while i != 0:

    t.busca()

    time.sleep(30)
    i -= 1
