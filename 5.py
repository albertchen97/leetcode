def longestPalindrome(s):
    l = len(s)
    longest_palindrome = s[0] 
    dp = [[False for _ in range(l)] for _ in range(l)]

    for i in range(l):
        dp[i][i] = True
    
    for i in range(l-1):
        if s[i] == s[i+1]:
            dp[i][i+1]
            longest_palindrome = s[i:i+2]
    
    max_length = 0
    for substring_length in range(3, l):
        for start_idx in range(0, l - substring_length):
            end_idx = start_idx + substring_length - 1
            if s[start_idx] == s[end_idx] and dp[start_idx + 1][end_idx - 1]:
                dp[start_idx][end_idx] = True
                if substring_length > max_length:
                    max_length = substring_length
                    longest_palindrome = s[start_idx:end_idx + 1]
    return longest_palindrome

print(longestPalindrome("abc"))
print(longestPalindrome("abbc"))
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))


