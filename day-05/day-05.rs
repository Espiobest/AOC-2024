use::std::fs;
use::std::cmp::Ordering;

fn main() {
    let input: String = fs::read_to_string("day-05/data.txt").unwrap();
    let lines: Vec<&str> = input.split("\n").collect::<Vec<&str>>();

    let mut rules: Vec<(i32, i32)> = Vec::new();
    let mut numbers: Vec<Vec<i32>> = Vec::new();
    lines.into_iter().for_each(|line| {
        if line.contains("|") {
            let rule: Vec<i32> = line.trim().split("|").map(|x| x.parse::<i32>().unwrap()).collect();
            let a: i32 = rule[0];
            let b: i32 = rule[1];
            rules.push((a, b));
        } 
        else if line.contains(",") {
            numbers.push(line.trim().split(",").map(|x: &str| x.parse::<i32>().unwrap()).collect())
        }
    });

    let mut part1: i32 = 0;
    let mut part2: i32 = 0;

    for mut n in numbers {
        let mut valid: bool = true;
        for rule in &rules {
            let a: i32 = rule.0;
            let b: i32 = rule.1;
            if !n.contains(&a) || !n.contains(&b) {
                continue;
            }
            if n.iter().position(|&x| x == a) > n.iter().position(|&x| x == b) {
                valid = false;
                break;
            }
        }
        if valid {
            part1 += n.get(n.len()/2).unwrap();
        }
        else {
            n.sort_by(|&x, &y| {
                if rules.contains(&(x, y)) {
                    Ordering::Less
                }
                else {
                    Ordering::Greater
                }
            });
            
            part2 += n.get(n.len()/2).unwrap();
        }
    }

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);

}