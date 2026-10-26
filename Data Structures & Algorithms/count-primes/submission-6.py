class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        n = n - 1
        sieve = [True] * (n+1)
        sieve[0] = False
        sieve[1] = False

        p = 2
        

        while p*p<=n:
            if sieve[p]:
                
                multiple = p *p
                while multiple <= n:
                    sieve[multiple] = False
                    multiple += p

            p += 1    
            
        return sum(sieve)