// Recommend running with Codi

// why is lastIndex = this.length - 1 ?
// Because Arrays start at 0 not 1
// Length will have it's first element in the 0th place with length 1
// So if you wanted to access an array with one element
// you would need to access it at length - 1 where length in this case would be 1

// Visual Aid

// [7, 6, 9, 5, 3] // length = 5
//  0, 1, 2, 3, 4  // 5 - 1 = 4
// 4 is the final index

class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  insert(element, index) {
    for (let i = this.length; i > index; i--) {
      this.data[i] = this.data[i - 1];
    }
    this.data[index] = element;
    this.length++;
    return this.data;
  }

  push(element) {
    this.data[this.length] = element;
    this.length++;
    return this.length;
  }

  pop() {
    const lastIndex = this.length - 1;
    const lastelement = this.data[lastIndex];
    delete this.data[lastIndex];
    this.length--;
    return lastelement;
  }

  get(index) {
    return this.data[index];
  }

  delete(index) {
    const lastIndex = this.length - 1;
    const element = this.data[index];
    this.shiftelements(index, lastIndex);
    delete this.data[lastIndex];
    this.length--;
    return element;
  }

  shiftelements(index, lastIndex) {
    for (let i = index; i < lastIndex; i++) {
      this.data[i] = this.data[i + 1];
    }
  }
}

const newArray = new MyArray();

newArray;

newArray.length;

newArray.get(0); // actually returns undefined

newArray.push("dog");

newArray.get(0);

newArray.length;

newArray.push("cat");

newArray;

newArray.pop();

newArray;

newArray.length;

newArray.get(0);

newArray.delete(0);

newArray;

newArray.push("cat");
newArray.push("dog");
newArray.push("lion");
newArray.push("tiger");

newArray.insert("mouse", 3);
