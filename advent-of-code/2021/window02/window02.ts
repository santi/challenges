// https://adventofcode.com/2021/day/2
import fs from "fs";

const multiply = (a: number, b: number) => a * b;

type Operation = "forward" | "down" | "up";
const input = fs
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ") as [Operation, string])
  .map(([direction, value]): [Operation, number] => [direction, Number(value)]);

type Position = [number, number]; // [horizontal, depth]

const op: Record<Operation, (pos: Position, b: number) => Position> = {
  forward: (pos: Position, b: number): Position => [pos[0] + b, pos[1]],
  down: (pos: Position, b: number): Position => [pos[0], pos[1] + b],
  up: (pos: Position, b: number): Position => [pos[0], pos[1] - b],
};

const partOne = input
  .reduce(
    (position: Position, command) => op[command[0]](position, command[1]),
    [0, 0]
  )
  .reduce(multiply, 1);

console.log(`Part one: ${partOne}`);

type AimPosition = [number, number, number]; // [horizontal, depth, aim]

const aimOp: Record<Operation, (pos: AimPosition, X: number) => AimPosition> = {
  forward: (pos: AimPosition, X: number): AimPosition => [
    pos[0] + X,
    pos[1] + pos[2] * X,
    pos[2],
  ],
  down: (pos: AimPosition, X: number): AimPosition => [
    pos[0],
    pos[1],
    pos[2] + X,
  ],
  up: (pos: AimPosition, X: number): AimPosition => [
    pos[0],
    pos[1],
    pos[2] - X,
  ],
};

const partTwo = input
  .reduce(
    (position: AimPosition, command) => aimOp[command[0]](position, command[1]),
    [0, 0, 0]
  )
  .slice(0, 2)
  .reduce(multiply, 1);

console.log(`Part two: ${partTwo}`);
