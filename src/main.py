# -*- coding: utf-8 -*-
from TextDataReader import TextDataReader
from CalcRating import CalcRating
from AvarageMark import AvarageMark
from JsonDataReader import JsondataReader
import argparse
import sys
import os



def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    extension = os.path.splitext(path)[1]
    if extension == ".txt":
        reader = TextDataReader()
    elif extension == ".json":
        reader = JsondataReader()
    else:
        raise Exception("Format {} not supported.".format(extension))

    students = reader.read(path)
    print("Студент: ", students)
    rating = CalcRating(students).calc()
    print("Рейтинг: ", rating)
    rating = AvarageMark(students).calc()

    for i in rating:
        if rating.get(i) ==2:
            print("Student: ", i)
            break
        else:
            print("No students")


if __name__ == "__main__":
    main()
