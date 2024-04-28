# Được giới hạn bởi cặp ngoặc {}
# cách nhau bởi dấu ,
# không chứa nhiều hơn 1 phần tử trùng lặp
# chỉ chứa hashable obj nhưng nó k phải hashable obj. Nên không thể chứa set trong set
set_1 = {'dieu','bien',6}
set_2 = set('dieu bien')
print(set_1)
print(set_2)
print(type(set_1))
print(type(set_2))
