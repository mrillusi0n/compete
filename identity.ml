(* fold but return the list *)

let nofold =
    List.fold_right List.cons []

let folded_map f =
    List.fold_right (fun i a -> 2::[]) []

let square x = x*x
let nums = [1; 2; 3; 4]
