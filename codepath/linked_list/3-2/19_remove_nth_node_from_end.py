class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def create_linked_list(values):
  l = Node(None)

  if values:
    for val in reversed(values):
      l.next = Node(val, l.next)

  return l.next

def compare_linked_lists(l1, l2):
  if not(l1) and not(l2): return True
  if not(l1) or not(l2): return False
  if l1.val != l2.val: return False
  if l1.next == None: return l2.next == None
  return compare_linked_lists(l1.next, l2.next)

# Implement this function
def remove_from_end(l, n):
  temp = Node(-1, l)
  slow, fast = temp, temp
  
  # move fast n-nodes aheaad of slow -> O(m)
  for _ in range(n):
    fast = fast.next

  # moving slow and fast at the same pace -> O(n)
  while fast.next:
    slow = slow.next
    fast = fast.next

  slow.next = slow.next.next
  return temp.next

# time: O(m) + O(n - m) = O(n)
# space: O(1)

def main():
  tests = [
    { 'input': { 'l': [1],             'n': 1 }, 'output': [] },
    { 'input': { 'l': [1, 2],          'n': 1 }, 'output': [1] },
    # Add more tests
  ]

  for i in range(len(tests)):
    print('Test', i+1, 'Pass:',
      compare_linked_lists(
        remove_from_end(create_linked_list(tests[i]['input']['l']), tests[i]['input']['n']),
        create_linked_list(tests[i]['output'])
      )
    )

main()