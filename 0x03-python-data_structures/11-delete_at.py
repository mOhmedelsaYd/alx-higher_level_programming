#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """Delete element"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)
