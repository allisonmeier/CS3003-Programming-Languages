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
{-
findFirst :: Eq a => (a -> Bool) -> [a] -> Found 
findFirst _ [] = NoMatch --if the list is empty, NoMatch
findFirst needle haystack = search 0 haystack -- start at index 0
  where -- use search to go through everything while also tracking current index
    search :: Int -> [a] -> Found
    search _ [] = NoMatch
    search index (thing:restOfThings)
      | needle thing = Match index --if needle returns True for current thing, return current index
      | otherwise = search (index + 1) restOfThings --if not, keep searching the rest of the list
-}
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


