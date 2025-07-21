def insertSortedDescending (x : Nat) (l : List Nat) : List Nat :=
  match l with
  | [] => [x]
  | y :: ys =>
    if x ≥ y then
      x :: y :: ys
    else
      y :: (insertSortedDescending x ys)

#eval insertSortedDescending 52 [55, 48, 32]

def lastStoneWeight (stones : List Nat) : Nat :=
  let sortedDescendingStones := stones.foldl (fun acc x => insertSortedDescending x acc) []
  match sortedDescendingStones with
  | [] => 0
  | [s] => s
  | s1 :: s2 :: rest =>
    if s1 == s2 then
      lastStoneWeight rest
    else
      lastStoneWeight (insertSortedDescending (s1 - s2) rest)

#eval! lastStoneWeight [2, 7, 4, 1, 8, 1]
