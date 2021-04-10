#
# CS21-Science-Day-21
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/1009/problem/B?f0a28=1
# Time Complexity: O(n)
#
#

tenaryString = input()

numberOfOnes = tenaryString.count('1')
indexOffirstTwo = tenaryString.find('2')

# last character in tenary String
if indexOffirstTwo == -1:
    indexOffirstTwo = len(tenaryString)

temp = tenaryString[:indexOffirstTwo]
numberOfZeros = temp.count('0')

result = '0'*numberOfZeros + '1'*numberOfOnes + tenaryString[indexOffirstTwo:].replace('1', '')
print(result)
