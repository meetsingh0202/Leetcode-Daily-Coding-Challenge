class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                        "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def convertNumberToWords(n):
            if n < 20:
                return less_than_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + less_than_20[n % 10] if n % 10 != 0 else "")
            elif n < 1000:
                return less_than_20[n // 100] + " Hundred" + (" " + convertNumberToWords(n % 100) if n % 100 != 0 else "")
            elif n < 1000000:
                return convertNumberToWords(n // 1000) + " Thousand" + (" " + convertNumberToWords(n % 1000) if n % 1000 != 0 else "")
            elif n < 1000000000:
                return convertNumberToWords(n // 1000000) + " Million" + (" " + convertNumberToWords(n % 1000000) if n % 1000000 != 0 else "")
            else:
                return convertNumberToWords(n // 1000000000) + " Billion" + (" " + convertNumberToWords(n % 1000000000) if n % 1000000000 != 0 else "")

        return convertNumberToWords(num)
