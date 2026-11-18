class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Constraints: -1000 <= a, b <= 1000 (sum is in [-2000, 2000]).
        # A 12-bit box (mask = (1 << 12) - 1, sign bit = 1 << 11) is the exact minimum needed.
        # Here we use a standard 32-bit box (mask = (1 << 32) - 1, sign bit = 1 << 31) for extra room.
        mask = (1 << 32) - 1  # 32 ones in binary (0xFFFFFFFF)

        # Mask 'a' upfront! If b == 0, the while loop won't run at all—so 'a' MUST
        # already fit inside our 32-bit window before the final negative check runs.
        a &= mask

        # Repeat until there are no carries left to add
        while b != 0:
            # 1. Find carry positions (where both bits are 1) and shift left by 1.
            #    Apply '& mask' so carries shifting past the 32nd bit fall off the edge,
            #    preventing an infinite loop when negative numbers are involved.
            carry = ((a & b) << 1) & mask

            # 2. Add bits without carrying using XOR (^).
            #    Apply '& mask' to strip away Python's infinite leading 1s on negative inputs.
            a = (a ^ b) & mask

            # 3. Treat the bundled carries as the new 'b' to be added in the next iteration.
            b = carry

        # Check the 32nd bit (index 31), which acts as the sign bit for our 32-bit box:
        # - If it is 0, 'a' is positive/zero and already in valid Python integer format.
        # - If it is 1, 'a' is negative, so we restore Python's infinite leading 1s via ~(a ^ mask).
        return ~(a ^ mask) if (a & (1 << 31)) else a


# ==============================================================================
# DETAILED EXPLANATION & INTUITION (FOR FUTURE REFERENCE)
# ==============================================================================
#
# 1. CORE IDEA (TWO-STEP BINARY ADDITION):
#    Instead of looping bit-by-bit with a counter, we split addition into two parts:
#      a) Sum without carries:  a ^ b
#      b) Carries shifted left: (a & b) << 1
#    We treat all carries together as a new number 'b' and keep adding it to 'a'
#    until there are no carries left (b == 0).
#
# 2. WHY PYTHON NEEDS A MASK:
#    In languages like C++ or Java, integers are fixed at 32 bits, so overflow carries
#    naturally fall off the left edge. In Python, integers have arbitrary precision,
#    meaning negative numbers have an INFINITE string of leading 1s (...11111011).
#    Without a mask, adding -1 and 1 causes the carry bit to shift left forever
#    (1 -> 2 -> 4 -> 8 -> 16 -> ...), resulting in an infinite loop.
#
# 3. CHOOSING THE BOX SIZE (12 BITS VS. 32 BITS):
#    - Given -1000 <= a, b <= 1000, the sum is always in [-2000, 2000].
#    - 11 bits only holds [-1024, 1023] (too small—2000 would overflow into the sign bit).
#    - 12 bits holds [-2048, 2047], which is the exact minimum box guaranteed to fit.
#    - Giving extra room (like 32 bits: mask = (1 << 32) - 1, sign bit = 1 << 31) gives
#      the EXACT same answer, just taking up to 32 loop rounds instead of 12 on negative numbers.
#    - IMPORTANT: Always keep the sign-bit index (bits - 1) synced with the mask width!
#
# 4. WHERE & WHY '& mask' IS APPLIED:
#    - Upfront on 'a' (a &= mask): Crucial edge-case fix for when b == 0 (e.g., a = -1, b = 0).
#      When b == 0, the while loop is skipped completely; without 'a &= mask' upfront,
#      'a' would keep its infinite leading 1s and break ~(a ^ mask).
#    - On 'carry': Slices off any carry bit that shifts past the 32nd position,
#      forcing 'b' to eventually reach 0 so the while loop terminates.
#    - On 'a' inside loop: Chops off infinite leading 1s from negative inputs so 'a'
#      stays strictly inside our 32-bit window.
#
# 5. HOW THE FINAL NEGATIVE RESTORATION WORKS: ~(a ^ mask)
#    After the loop finishes, the 32-bit box holds the exact two's complement answer.
#    However, because '& mask' zeroed out all bits to the left of our 32-bit window,
#    Python reads a negative result (like -2, stored as ...0000 1111...1110)
#    as a large positive number.
#
#    If the sign bit (a & (1 << 31)) is 1, we need to turn outer 0s into infinite 1s
#    WITHOUT changing the 32 bits inside our box. Since Python has no "selective NOT",
#    we use a double-flip trick (flipping twice cancels out: not(not x) == x):
#      Step 1 (a ^ mask): Pre-flips ONLY the 32 bits inside the box; outer 0s stay 0.
#      Step 2 (~):        Flips EVERY bit in Python—turning outer 0s into infinite 1s
#                         (1 flip), while flipping the inside 32 bits a 2nd time back
#                         to their original values (2 flips = unchanged).
#
# 6. COMPLEXITY:
#    - Time Complexity:  O(1) — The loop runs at most 32 times (or 12 times if using
#                        a 12-bit mask), regardless of input values.
#    - Space Complexity: O(1) — Uses only a constant number of integer variables.
# ==============================================================================
