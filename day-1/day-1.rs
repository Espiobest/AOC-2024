use std::fs;
use std::io;

fn main() -> io::Result<()> {

    let input = fs::read_to_string("day-1/data.txt").unwrap();

    let mut col1: Vec<u32> = Vec::new();
    let mut col2: Vec<u32> = Vec::new();

    input.lines().for_each(|line| {
        let mut nums = line.split_whitespace().map(|x| x.parse::<u32>().unwrap());
        col1.push(nums.next().unwrap());
        col2.push(nums.next().unwrap());
    });
    
    col1.sort();
    col2.sort();

    let part1: u32 = col1.iter().zip(col2.iter()).map(|(x, y)| x.abs_diff(*y)).sum();
    println!("Part 1: {}", part1);

    let part2: u32 = col1.iter().map(|x| *x * col2.iter().filter(|y| *y == x).count() as u32).sum();
    println!("Part 2: {}", part2);

    Ok(())
}