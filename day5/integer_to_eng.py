class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = ""
        
        d = ["Trillion", "Billion", "Million", "Thousand", "" ]
        
        x = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen",15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty",50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty",90:"Ninety", 100:"Hundred", 0:""}
        
        while num > 0:
            new_ans = ""
            new_num = num%1000
            num = num//1000
            units = new_num%10
            new_num //= 10
            tens = new_num % 10
            new_num //= 10
            hundreds = new_num
            
            if hundreds != 0:
                new_ans = x[hundreds] + " Hundred"
            if tens == 1:
                new_ans += " " + x[10 + units]
            else:
                new_ans += " " + x[10 * tens] + " " + x[units]
                
            if new_ans.strip() == "":
                d.pop()
                continue
            ans = new_ans + " " + d.pop() + " " + ans
            
        return " ".join([x for x in ans.split(" ") if x != ""])