# O(n) time | O(n) space
class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []
        for component in components:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(component)
        result = "/" + "/".join(stack)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("//home/") == "/home"
    assert solution.simplifyPath("/home//foo/") == "/home/foo"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/.../") == "/..."
    assert solution.simplifyPath("//.../") == "/..."
    assert solution.simplifyPath("/...../") == "/....."
    assert solution.simplifyPath("/a/b/../c/d") == "/a/c/d"
    assert solution.simplifyPath("/a/b/../../d") == "/d"
    assert solution.simplifyPath("/a/../../c/d") == "/c/d"
    assert solution.simplifyPath("/a/b/c/..") == "/a/b"
    assert solution.simplifyPath("/a/b/./c/d") == "/a/b/c/d"
    assert solution.simplifyPath("/a/b/c/.") == "/a/b/c"
    assert solution.simplifyPath("//./a/b/c/d") == "/a/b/c/d"
