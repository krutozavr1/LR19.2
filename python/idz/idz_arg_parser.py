#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

def print_sentences_in_cmd(sentences):
    for s in sentences:
        print(s)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Разделение предложений')
    parser.add_argument('divided_sentences', metavar='sentence', type=str, nargs='+', help='разделенные предложения')
    parser.add_argument('--print', dest='print_mode', action='store_true', help='выводить в командной строке')

    args = parser.parse_args()
    divided_sentences = args.divided_sentences
    exclamation_sentences = []
    question_sentences = []

    for i in divided_sentences:
        if '!' in i:
            exclamation_sentences.append(i)
        if '?' in i:
            question_sentences.append(i)

    if args.print_mode:
        print_sentences_in_cmd(exclamation_sentences)
        print_sentences_in_cmd(question_sentences)
    else:
        for s in exclamation_sentences:
            sys.stdout.write(s + '\n')
        for s in question_sentences:
            sys.stdout.write(s + '\n')
