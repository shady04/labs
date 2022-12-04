def delete(list_, index=None):
    if index is None:
        del list_[-1]
        return list_
    else:
        del list_[index]
        return list_

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
