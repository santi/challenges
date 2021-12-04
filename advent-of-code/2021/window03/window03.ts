// https://adventofcode.com/2021/day/3
import fs from "fs";

const input = fs.readFileSync("./input.txt").toString().split("\n");

const bitCounts: number[] = new Array(input[0].length).fill(0);

input.forEach((bits) =>
  bits
    .split("")
    .forEach((bit, index) =>
      bit === "1" ? (bitCounts[index] += 1) : (bitCounts[index] -= 1)
    )
);

const gamma = parseInt(
  bitCounts.map((count) => (count >= 0 ? "1" : "0")).join(""),
  2
);

const epsilon = parseInt(
  bitCounts.map((count) => (count >= 0 ? "0" : "1")).join(""),
  2
);

const partOne = gamma * epsilon;
console.log(`Part one: ${partOne}`);

const getCandidateFilter: (
  candidates: string[],
  index: number,
  filterType: ["1", "0"] | ["0", "1"]
) => (candidate: string) => boolean = (candidates, index, filterType) => {
  const criteria =
    candidates.reduce(
      (acc, line) => (line.substring(index, index + 1) === "1" ? acc + 1 : acc),
      0
    ) >=
    candidates.length / 2
      ? filterType[0]
      : filterType[1];

  return (candidate) => candidate.substring(index, index + 1) === criteria;
};

const filterCandidates = (
  candidates: string[],
  index: number,
  filterType: ["1", "0"] | ["0", "1"]
): string => {
  if (candidates.length === 1) {
    return candidates[0];
  }
  const candidateFilter = getCandidateFilter(candidates, index, filterType);
  return filterCandidates(
    candidates.filter(candidateFilter),
    index + 1,
    filterType
  );
};
const oxygenRating = parseInt(filterCandidates(input, 0, ["1", "0"]), 2);
const CO2Rating = parseInt(filterCandidates(input, 0, ["0", "1"]), 2);

const partTwo = oxygenRating * CO2Rating;
console.log(`Part two: ${partTwo}`);
