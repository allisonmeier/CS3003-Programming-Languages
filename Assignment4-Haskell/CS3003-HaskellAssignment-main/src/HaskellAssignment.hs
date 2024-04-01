module HaskellAssignment where

------------------------------------------------
{- 
findFirst

Parameters:
1. A function, needle, with one parameter of type a that returns True if its argument is the item to find 
  and False otherwise: (a -> Bool) 
2. A list, haystack, of elements of type a

Return Value:
A Match which contains the index of the first element (in left-to-right order) 
  of haystack that causes needle to return True; 
  NoMatch if no element of haystack causes needle to return True

Other:
findFirst returns NoMatch when haystack is an empty list.

-}
------------------------------------------------
data Found = Match Int | NoMatch deriving Eq
instance Show Found where
  show (Match index) = "Found match at " ++ show index
  show NoMatch = "No match found!"

-- Actual function:
findFirst :: Eq a => (a -> Bool) -> [a] -> Found 
findFirst needle haystack = findFirstHelper needle haystack 0 -- start at index 0
 
-- Helper function:
findFirstHelper _ [] _ = NoMatch --if the list is empty, NoMatch
findFirstHelper needle (i:list) index | needle i = Match index -- if index i == true (for "is the needle here?"), match
findFirstHelper needle (i:list) index = findFirstHelper needle list (index + 1) -- if !match, keep searchin

------------------------------------------------
{- 
palindrome

Parameters:
A string, candidate

Return Value:
True if candidate is a palindrome; False, otherwise

Other:
The empty string is a palindrome. Strings will contain only lowercase letters.

-}
------------------------------------------------
palindrome :: [Char] -> Bool
palindrome [] = True  --empty string counts as palindrome
palindrome word = word == reverse word  --check if string = reverse string
  -- upper line not right fyi


