#https://gist.github.com/piac/ef91ac83cb5ee92a1294
# modified by sv
def tree_to_list(input, retrieve_base = lambda x: x[0]):
    """Returns a list representation of a Grasshopper DataTree"""
    def append_at(path, index, simple_input, rest_list):
        target = path[index]
        if len(rest_list) <= target: rest_list.append([None]*(target-len(rest_list)+1))
        if index == path.Length - 1:
            rest_list[target] = list(simple_input)
        else:
            if rest_list[target] is None: rest_list[target] = []
            append_at(path, index+1, simple_input, rest_list[target])
    all = []
    for i in range(input.BranchCount):
        path = input.Path(i)
        append_at(path, 0, input.Branch(path), all)
    return retrieve_base(all)

def list_to_tree(input, none_and_holes=True, source=[0]):
    """Transforms nestings of lists or tuples to a Grasshopper DataTree"""
    from Grasshopper import DataTree as Tree
    from Grasshopper.Kernel.Data import GH_Path as Path
    from System import Array
    def proc(input,tree,track):
        path = Path(Array[int](track))
        if len(input) == 0 and none_and_holes: tree.EnsurePath(path); return
        for i,item in enumerate(input):
            if hasattr(item, '__iter__'): #if list or tuple
                track.append(i); proc(item,tree,track); track.pop()
            else:
                if none_and_holes: tree.Insert(item,path,i)
                elif item is not None: tree.Add(item,path)
    if input is not None: t=Tree[object]();proc(input,t,source[:]);return t

"""
def tree_to_list(tree,nest=True):
    nested_lst = []
    for i in range(tree.BranchCount):
        branchList = tree.Branch(i)
        #change from listobject
        lst = []
        for b in branchList:
            if nest:
                lst.append(b)
            else:
                nested_lst.append(b)
        if nest:
            nested_lst.append(lst)
    return nested_lst
"""
