use std::fs;
use itertools::Itertools;
use rayon::prelude::*;

fn solve(test: i64, nums: Vec<i64>, part2: bool) -> i64 {
    let ops: &[char] = if part2 { &['+', '*', '|'] } else { &['+', '*'] };

    let operations: Vec<Vec<&char>> = std::iter::repeat(ops).take(nums.len()).multi_cartesian_product().collect();
    for op in operations {
        let mut res: i64 = nums[0];
        for i in 0..op.len()-1 {
            if *op[i] == '+' {
                res += nums[i + 1];
            }
            else if *op[i] == '*' {
                res *= nums[i + 1];
            }
            else {
                let num = nums[i+1];
                res = (res * 10u64.pow(num.ilog10() + 1) as i64) + num;
            }
        }
        if res == test {
            return test;
        }
    }
    0
}

fn main() {
    let input: String = fs::read_to_string("day-07/data.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect();

    let part1: i64 = lines.clone().par_iter()
    .filter_map(|line| {
        let parts: Vec<&str> = line.split(": ").collect();
        let test: i64 = parts[0].parse().unwrap();
        let nums: Vec<i64> = parts[1].split(" ").map(|x| x.parse().unwrap()).collect();
        Some(solve(test, nums, false))
    }).sum();

    println!("Part 1: {}", part1);

    let part2: i64 = lines.par_iter()
    .filter_map(|line| {
        let parts: Vec<&str> = line.split(": ").collect();
        let test: i64 = parts[0].parse().unwrap();
        let nums: Vec<i64> = parts[1].split(" ").map(|x| x.parse().unwrap()).collect();
        Some(solve(test, nums, true))
    }).sum();

    println!("Part 2: {}", part2);
}
