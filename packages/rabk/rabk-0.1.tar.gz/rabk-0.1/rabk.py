# bill_generator.py
import os
from jinja2 import Environment, FileSystemLoader

class BillGenerator:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def get_template(self, template_name):
        return self.env.get_template(template_name)

    def generate_bill(self, template_name, context):
        template = self.get_template(template_name)
        return template.render(context)
        
    def print_bill(self, template_name, context):
        bill = self.generate_bill(template_name, context)
        print(bill)
