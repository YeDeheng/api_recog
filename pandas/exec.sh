#!/bin/zsh
crf_learn template train.data model -t
crf_test -m model test.data > crfresult
