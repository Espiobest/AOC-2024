use std::fs;
use regex::Regex;

fn main() {
    let input: String = fs::read_to_string("day-03/data.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect::<Vec<&str>>();
    let line: String = lines.join("");
    let mut part1: i32 = 0;
    let mut part2: i32 = 0;

    let re1: Regex = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    
    re1.captures_iter(&line).for_each(|x| {
        let a: i32 = x[1].parse::<i32>().unwrap();
        let b: i32 = x[2].parse::<i32>().unwrap();
        part1 += a * b;
    });

    let re2: Regex = Regex::new(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))").unwrap();
    let mut enabled: bool = true;

    re2.captures_iter(&line).for_each(|x| {
        let instruction: &str = &x[0];
        if instruction.contains("do()") {
            enabled = true;
        }
        else if instruction.contains("don't()") {
            enabled = false;
        }
        else {
            let a: i32 = x[2].parse::<i32>().unwrap();
            let b: i32 = x[3].parse::<i32>().unwrap();
            if enabled {
                part2 += a * b;
            }
        }
    });

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);

}