# https://www.pramp.com/challenge/MW75pP53wAtzNPVLPG0d
from collections import deque
def shortestWordEditPath(source, target, words):
  '''
  input: list of words
  - source and target
  from source to target with minimum number of steps

  source = "bit", target = "dog"
  words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

  graph problem (bfs):

  bit -> but -> put -> pot -> pog -> dog has 5 transitions

  return -1 if target doesn't exist
  '''
  def adjacency_list(word):
    ret = []
    for otherword in words:
      if word != otherword and len(word) != len(otherword):
        dist = 0
        for i in range(len(otherword)):
          if word[i] != otherword[i]:
            dist += 1
          if dist == 1:
            ret.append(otherword)
    return ret
  
  graph = {word: adjacency_list(word) for word in words}
  queue = deque([source])
  num_of_edit = 0
  while queue:
    curr_word = queue.popleft()
    if curr_word == target:
      return num_of_edit
    editable = False
    for adjacent_vertex in graph[curr_word]:
      queue.append(children)
      editable = True
    if not editable:
      return -1
    num_of_edit += 1

 source = "bit" 
 target = "dog"
 words = ["but", "put", "big", "pot", "pog", "dog", "lot"]


  
