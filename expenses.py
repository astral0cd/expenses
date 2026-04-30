import argparse
import json
import os
from storage import load_data, save_data

DATA_FILE = 'expenses.json'

def add_category(args):
    data = load_data()
    if args.category in data['categories']:
        print(f"Категория {args.category} уже есть")
    else:
        data['categories'].append(args.category)
        save_data(data)
        print(f"Категория '{args.category}' успешно добавлена.")
