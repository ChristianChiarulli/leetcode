let animal = {
  species: "dog",
  age: 7,
  fur: true,
  legs: 4,
  noise: () => {
    console.log("bark");
  },
};

// O(1)
animal.legs;
animal.noise();

// O(1)
animal.species = "cat";

animal.species;

const map = new Map();

map.set(7, "7");
map.get(7);
map.set("8", 8);
map.get("8");
