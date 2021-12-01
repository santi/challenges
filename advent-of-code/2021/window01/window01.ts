// https://adventofcode.com/2021/day/1
import fs from "fs";

const sum = (acc: number, num: number) => acc + num;

const input = fs
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let partOne = 0;
input.reduce((previous, current) => {
  if (current > previous) partOne++;
  return current;
});

console.log(`Part one: ${partOne}`);

let partTwo = 0;
input.slice(3).reduce((previous: number[], current) => {
  const previousSum = previous.reduce(sum, 0);
  const currentSum = previous.slice(-2).reduce(sum, 0) + current;

  if (currentSum > previousSum) partTwo++;
  return [...previous.slice(1), current];
}, input.slice(0, 3));

console.log(`Part two: ${partTwo}`);
