li=[int (i) for i in input()]
num = ''.join(map(str,li))
num=int(num)

ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}

if li[0]==0:
    print('zero')
elif len(li)==1 or li[0]==1:
     print(ones[num])
else:
     if li[1]==0:
        str=tens[li[0]]
     else:
         str=tens[li[0]]+'-'+ones[li[1]]
     print(str)
