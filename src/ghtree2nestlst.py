def ghtree2nestlist(tree,nest=True):
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