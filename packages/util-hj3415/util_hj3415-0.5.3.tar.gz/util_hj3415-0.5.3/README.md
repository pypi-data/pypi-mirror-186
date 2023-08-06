util-hj3415
==========

util-hj3415 is the collection of utility functions.

Usage
-----

from util_hj3415 import utils

def to_float(s) -> float:

def to_억(v) -> str:

def to_만(v) -> str:

def str_to_date(d: str) -> datetime.datetime:

def date_to_str(d: datetime.datetime) -> str:

def pick_rnd_x_code(count: int) -> list:


from util_hj3415 import noti

def mail_to(title: str, text: str, mail_addr='hj3415@hanmail.net') -> bool:

BOT_LIST = ['manager', 'dart', 'eval']

def telegram_to(botname: str, text: str, parse_html: bool = False) -> bool:



