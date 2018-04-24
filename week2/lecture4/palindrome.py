# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:33:30 2016

@author: ericgrimson
"""

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            first_char = s[0]
            last_char = s[-1]
            is_fist_eq_last = first_char == last_char
            return is_fist_eq_last and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))