def inorder(tree, action, index=1):
	length = len(tree) - 1
	if length < index: return
	inorder(tree, action, 2*index)
	action(tree[index])
	inorder(tree, action, 2*index+1)

def preorder(tree, action, index=1):
	length = len(tree) - 1
	if length < index: return
	action(tree[index])
	preorder(tree, action, 2*index)
	preorder(tree, action, 2*index+1)

def postorder(tree, action, index=1):
	length = len(tree) - 1
	if length < index: return
	postorder(tree, action, 2*index)
	postorder(tree, action, 2*index+1)
	action(tree[index])

t = [0, 1]
for i in range(6): t.append(2+i)
def _print(r): print(r, end=' ')
preorder(t, _print)
print()
inorder(t, _print)
print()
postorder(t, _print)
