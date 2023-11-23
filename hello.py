#! /usr/bin/env python3

class Hello():
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'User = [ Hello, {self.first_name} {self.last_name}]'

user = Hello('Mateus', 'Laranjeira')
print(user)

    