__author__ = 'Hamish Stokes'

from collections import deque

def main():
    n = input()
    iters = 0
    while n != '0' and n != '':
        node_count = int(n)
        counter = node_count * 2
        blue = deque()
        pink = []
        while counter > 0:
            while counter > node_count:
                n = input()
                new_node = deque(int(i) for i in n.split())
                blue.append(new_node)
                counter -= 1
            n = input()
            new_node = [int(i) for i in n.split()]
            pink = pink + [new_node]
            counter -= 1
        end_array = [None]*node_count
        pink_array = list(end_array)
        b_value = deque(x for x in range(1, node_count+1))
        free_blues = node_count
        while free_blues != 0:
            b = b_value[0]
            first = blue[b-1].popleft()
            if pink_array[first - 1] is None:
                end_array[b-1] = first
                pink_array[first - 1] = b
                free_blues -= 1
                b_value.popleft()
            else:
                p_partner = end_array.index(first) + 1
                first_prefs = pink[first - 1]
                if first_prefs.index(p_partner) > first_prefs.index(b):
                    end_array[b-1] = first
                    end_array[p_partner -1] = None
                    pink_array[first -1] = b
                    b_value.popleft()
                    b_value.append(p_partner)
        iters += 1
        print("Instance "+str(iters)+":")
        for i in end_array:
            print(i)
        n = input()

main()
