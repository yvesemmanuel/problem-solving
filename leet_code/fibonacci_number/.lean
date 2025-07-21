def fibonacci (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | 1 => 1
  | n + 2 => fibonacci (n + 1) + fibonacci n

#eval fibonacci 4
