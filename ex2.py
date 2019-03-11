import matplotlib.pyplot as plt 
from ex1 import db

collection=db["posts"]
new_collection = {
    "title":"C4E26",
    "author":"Nguyễn Hữu Đạt",
    "content":"các bạn khóa sau cố gắng nhé ;)"
 }
collection.insert_one(new_collection)