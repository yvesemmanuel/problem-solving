structure MyArray (α : Type) where (data : List α)

instance  {α} [Repr α] : Repr (MyArray α) where
  reprPrec a _ := "# " ++ repr a.data

def mergeArrays (nums1 : MyArray (Nat × Nat)) (nums2 : MyArray (Nat × Nat)) : MyArray (Nat × Nat) :=
  let rec merge (l1 l2 : List (Nat × Nat)) : List (Nat × Nat) :=
    match l1, l2 with
    | [], l2 => l2
    | l1, [] => l1
    | (id1, val1) :: t1, (id2, val2) :: t2 =>
      if id1 < id2 then
        (id1, val1) :: merge t1 l2
      else if id2 < id1 then
        (id2, val2) :: merge l1 t2
      else
        (id1, val1 + val2) :: merge t1 t2

  let resultList := merge nums1.data nums2.data
  { data := resultList }

def nums1 : MyArray (Nat × Nat) := { data := [(1, 2), (4, 1), (5, 3), (6, 4)] }
def nums2 : MyArray (Nat × Nat) := { data := [(1, 5), (2, 7), (4, 8), (7, 1)] }

#eval! mergeArrays nums1 nums2
