// Recommend running with Codi

// Access O(1)
// Push O(1)
// Insert (n)
// Delete (n)

const strings = ["a", "b", "c", "d"];
//                0    1    2    3

// 4*4 = 16 bytes of storage 4 bytes per string

// Access O(1)
strings[2];

// Push O(1)
strings.push("e");
strings;

// Insert O(n)
strings.splice(2, 0, "item");
strings;

// Delete O(n)
strings.splice(2, 1);
// start — The zero-based location in the array from which to start removing elements.
// deleteCount — The number of elements to remove.
// items — Elements to insert into the array in place of the deleted elements.
strings;

// BONUS

// Pop O(1)
// Insert O(1) (At beginning)

// Pop O(1)
strings.pop();
strings;

// Insert O(1) (At beginning)
strings.unshift("x");
strings;
