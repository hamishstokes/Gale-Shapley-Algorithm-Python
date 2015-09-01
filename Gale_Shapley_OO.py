__author__ = 'Hamish Stokes'

from collections import deque
import re


class blue_:
    def __init__(self, num, pref_list):
        self.num = num
        self.prefs = pref_list
        self.next_proposal = 0
        self.partner = 0


class pink_:
    def __init__(self, num, pref_list):
        self.num = num
        self.prefs = pref_list
        self.partner = False

    def set_partner(self, new_partner):
        self.partner = new_partner


def main():
    n = input()
    iters = 0
    while n != '0' and n != '':
        node_count = int(n)
        counter = node_count * 2
        blue_deque = deque()
        pink = []
        node_num_b = 1
        node_num_p = 1
        while counter > 0:
            while counter > node_count:
                n = input()
                new_blue = blue_(node_num_b, n)
                blue_deque.append(new_blue)
                counter -= 1
                node_num_b += 1
            n = input()
            new_pink = pink_(node_num_p, n)
            pink.append(new_pink)
            counter -= 1
            node_num_p += 1
        out_list = node_count * [None]
        while blue_deque:
            front = blue_deque[0]
            to_propose = int(front.prefs.split(None, front.next_proposal + 1)[front.next_proposal])
            pink_prop = pink[to_propose - 1]
            if not pink_prop.partner:
                pink_prop.set_partner(front)
                front.partner = pink_prop.num
                front.next_proposal += 1
                out = blue_deque.popleft()
                out_list[out.num - 1] = out
            else:
                regex_front = r'\b(' + re.escape(str(front.num)) + r')\b'
                regex_old = r'\b(' + re.escape(str(pink_prop.partner.num)) + r')\b'
                if re.search(regex_front, pink_prop.prefs).start() < re.search(regex_old, pink_prop.prefs).start():
                    blue_deque.append(pink_prop.partner)
                    pink_prop.set_partner(front)
                    front.partner = pink_prop.num
                    front.next_proposal += 1
                    out = blue_deque.popleft()
                    out_list[out.num - 1] = out
                else:
                    front.next_proposal += 1
        iters += 1
        print("Instance " + str(iters) + ":")
        for i in out_list:
            print(i.partner)
        n = input()


main()
