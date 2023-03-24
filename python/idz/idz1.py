#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import click

"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

def compress_to_json(content):
    with open("data.json", "w", encoding="utf-8") as fout:
        json.dump(content, fout, ensure_ascii=False, indent=4)

def print_sentences_in_cmd(sentences):
    for s in sentences:
        click.echo(s)

if __name__ == "__main__":
    divided_sentences = sys.argv[1:]
    exclamation_sentences = []
    question_sentences = []

    for i in divided_sentences:
        if i.find("!") != -1:
            exclamation_sentences.append(i)
        if i.find("?") != -1:
            question_sentences.append(i)


    compress_to_json(exclamation_sentences)
    compress_to_json(question_sentences)

    print_sentences_in_cmd(exclamation_sentences)
    print_sentences_in_cmd(question_sentences)
