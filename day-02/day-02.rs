use std::fs;

fn is_safe(nums: &[u32]) -> bool {
    // check if it is monotone
    let monotone: bool = nums.windows(2).all(|w: &[u32]| w[0] <= w[1]) || nums.windows(2).all(|w: &[u32]| w[0] >= w[1]);
    if !monotone {
        return false;
    }
    nums.windows(2).map(|n: &[u32]| {
        let (x, y): (u32, u32) = (n[0], n[1]);
        x.abs_diff(y)
    }).collect::<Vec<u32>>().iter().all(|x| *x >= 1 && *x <= 3)
}

fn main() {
    let input: String = fs::read_to_string("day-02/data.txt").unwrap();
    let reports: Vec<Vec<u32>> = input.lines().map(|line: &str| line.split_whitespace().map(|x: &str| x.parse::<u32>().unwrap()).collect()).collect();

    let part1: i32 = reports.iter().map(|x| is_safe(x) as i32).sum();
    let part2: i32 = reports.iter().map(|x| {
        (0..x.len()).any(|i| {
            let mut nums: Vec<u32> = x.clone();
            nums.remove(i);
            is_safe(&nums)
        }) as i32
    }).sum();
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}