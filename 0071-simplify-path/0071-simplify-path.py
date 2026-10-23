class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        p=path.split("/")
        l=[a for a in p if a!=""]
        for i in l:
            if i==".":
                continue
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+"/".join(stack)
    