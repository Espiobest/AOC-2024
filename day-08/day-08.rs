use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let input = fs::read_to_string("day-08/data.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect();
    let grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();

    let mut nodes: HashMap<char, Vec<(i32, i32)>> = HashMap::new();
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] != '.' {
                nodes.entry(grid[i][j]).or_default().push((i as i32, j as i32));
            }
        }
    }

    let mut antinodes: HashSet<(i32, i32)> = HashSet::new();
    let mut antinodes2: HashSet<(i32, i32)> = HashSet::new();

    for (_, coords) in nodes.into_iter() {
        for i in 0..coords.len() {
            for j in i+1..coords.len() {
                let (x1, y1) = coords[i];
                let (x2, y2) = coords[j];

                let dx = x2 - x1;
                let dy = y2 - y1;
                let mut x = x2 + dx;
                let mut y = y2 + dy;

                if x >= 0 && x < grid.len() as i32 && y >= 0 && y < grid[0].len() as i32 {
                    antinodes.insert((x, y));
                }

                antinodes2.insert((x1, y1));
                while x >= 0 && x < grid.len() as i32 && y >= 0 && y < grid[0].len() as i32 {
                    antinodes2.insert((x, y));
                    x += dx;
                    y += dy;
                }

                let dx2 = -dx;
                let dy2 = -dy;
                x = x1 + dx2;
                y = y1 + dy2;

                if x >= 0 && x < grid.len() as i32 && y >= 0 && y < grid[0].len() as i32 {
                    antinodes.insert((x, y));
                }

                antinodes2.insert((x2, y2));
                while x >= 0 && x < grid.len() as i32 && y >= 0 && y < grid[0].len() as i32 {
                    antinodes2.insert((x, y));
                    x += dx2;
                    y += dy2;
                }
            }
        }
    }

    let part1: usize = antinodes.len();
    println!("Part 1: {}", part1);

    let part2: usize = antinodes2.len();
    println!("Part 2: {}", part2);

}