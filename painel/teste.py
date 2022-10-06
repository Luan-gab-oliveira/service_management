import os
get_dir = os.path.dirname(__file__)

for _, _, arquivo in os.walk(fr'{get_dir}\promocional'):
   imagens = arquivo

print(len(arquivo))