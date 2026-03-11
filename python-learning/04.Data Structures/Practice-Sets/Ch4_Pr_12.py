# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}

'''Reason (Step-by-step, exam-oriented)

1] Sets can store only hashable (immutable) elements.

2] Lists are mutable, meaning their values can be changed.

3] Mutable objects are not hashable.

4] Since [1, 2] is a list, Python does not allow it inside a set.

*Therefore:

1] You cannot create this set.

2] Hence, you cannot change values inside a list contained in a 
set, because such a set cannot exist.'''