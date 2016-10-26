# https://leetcode.com/problems/single-number-ii


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Design a custom "bit operator" such that it will make bits mod by 3
        # Just like a xor with base 3
        # Ordinary xor in base 2 is actually (bit_x + bit_y) % 2, here we need a custom xor_3 = (bit_x + bit+y) % 3

        # Since there are three different results: 0, 1, 2
        # We'll need two bits to represent the output of this xor_3 operator

        # xor_3 :: two_bits -> one_bit -> two_bits
        # xor_3 (b1 b0) (x) -> (new_b1 new_b0)

        # B      `xor_3` 0 = B
        # B      `xor_3` 1 = (B+1) mod 3
        # B      `xor_3` 2 = (B+2) mod 3
        # 00 (0) `xor_3` 1 = 01 (1)
        # 01 (1) `xor_3` 1 = 10 (2)
        # 10 (2) `xor_3` 1 = 00 (0)

        # let previous result = "b1 b0"
        # let current input bit = "x"
        # next result will be:
        # b0 = (b0 ^ x) & ~b1
        # b1 = (b1 ^ x) & ~b0

        # So we can see
        # if we want the number that occurs exactly once, we can use b0
        # if we want the number that occurs exactly twice, we can use b1

        b0, b1 = 0, 0
        for i in range(len(nums)):
            b0 = b0 ^ nums[i] & ~b1
            b1 = b1 ^ nums[i] & ~b0
        return b0
