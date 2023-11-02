# O(n) time | O(n) space

# Solution 1 (mine)
def collidingAsteroids(asteroids):
    stack = []
    for asteroid in asteroids:
        process_new_asteroid(stack, asteroid)
        while len(stack) >= 2 and stack[-1] < 0 < stack[-2]:
            right = stack[-1]
            stack.pop()
            process_new_asteroid(stack, right)
    return stack


def process_new_asteroid(stack, asteroid):
    right = asteroid
    left = stack[-1] if stack else None
    if left and right < 0 < left:
        if abs(left) == abs(right):
            stack.pop()
        elif abs(right) > abs(left):
            stack.pop()
            stack.append(right)
    else:
        stack.append(right)


# Solution 2 (from video explanation) (same complexity)
def colliding_asteroids(asteroids):
    stack = []
    for asteroid in asteroids:

        if asteroid > 0:
            stack.append(asteroid)
            continue

        while True:
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
                break

            asteroid_size = abs(asteroid)
            if stack[-1] > asteroid_size:
                break

            if asteroid_size == stack[-1]:
                stack.pop()
                break

            stack.pop()

    return stack


if __name__ == '__main__':
    assert colliding_asteroids([-3, 5, -8, 6, 7, -4, -7]) == [-3, -8, 6]
    assert colliding_asteroids([-3, 5, 6, 7, -8]) == [-3, -8]
    assert colliding_asteroids([5, 6, 7, -8, 10]) == [-8, 10]
    assert colliding_asteroids([5, 6, 7, -8]) == [-8]
    assert colliding_asteroids([5]) == [5]
    assert colliding_asteroids([5, 6, 7, 8]) == [5, 6, 7, 8]
    assert colliding_asteroids([-5, -6, -7, -8]) == [-5, -6, -7, -8]
    assert colliding_asteroids([-70, 100, 23, 42, -50, -75, 1, -2, -3]) == [-70, 100]
    assert (colliding_asteroids([5123, -34, 654, -3636, 2432, 4242, 1267, 1337, -43, -864, 38, 38, 1, -400]) ==
            [5123, 2432, 4242, 1267, 1337])
